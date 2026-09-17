import contextlib
import json
import sys
import urllib.parse

from loguru import logger

from jsonschema_restructuredtext.constants import DEFAULT_SECTION_PUNCTUATION
from jsonschema_restructuredtext.utils import (
    create_const,
    create_enum,
    create_section,
    dashify,
    sort_properties,
    strip_inside_backticks,
)


def _format_type(property_type) -> str:
    """
    Format a `type` value (string, list of strings, or missing) as a single
    display string, e.g. `["string", "null"]` -> "string or null".
    """
    if property_type is None:
        return "unspecified"
    if isinstance(property_type, list):
        return " or ".join(str(t) for t in property_type)
    return str(property_type)


def _is_object_or_array(property_type) -> bool:
    """
    True if `property_type` is, or includes, "object" or "array".
    """
    types = property_type if isinstance(property_type, list) else [property_type]
    return any(t in ("object", "array") for t in types)


def _definition_anchor(key: str) -> str:
    """
    Anchor for a schema/definition section header, kept in its own namespace
    (prefixed) so it cannot collide with a property anchor of the same name.
    """
    return f"def-{dashify(key)}"


def _property_anchor(json_path: list) -> str:
    """
    Anchor for a property's detail block, kept in its own namespace
    (prefixed) so it cannot collide with a definition anchor of the same name.
    """
    return f"prop-{dashify('-'.join(json_path))}"


def _get_schema_header(
    schema: dict,
    ref_key: str,
    description_fallback: str,
    section_punctuation: list = DEFAULT_SECTION_PUNCTUATION,
    schema_level: int = 0,
) -> str:
    """
    Get the title and description of the schema.

    If nested, all headings are increased by one level.
    """

    rst = ""
    title = schema.get("title", ref_key)

    # Clamp to the last available punctuation character if the caller
    # provided fewer characters than there are nesting levels (or none at all).
    if section_punctuation:
        punctuation = section_punctuation[
            min(schema_level, len(section_punctuation) - 1)
        ]
    else:
        punctuation = "="

    # Add the section and description of the schema
    rst += create_section(punctuation, _definition_anchor(ref_key), title)
    description = str(schema.get("description", description_fallback)).strip(" \n")
    rst += description
    rst += "\n\n"

    schema_type = _format_type(schema.get("type", "object(?)"))
    rst += f"Type: `{schema_type}`\n\n"

    return rst


def generate(
    schema: dict,
    title: str = "JSON Schema",
    replace_refs: bool = False,
    suppress_undocumented: bool = False,
    section_punctuation: list = DEFAULT_SECTION_PUNCTUATION,
    debug: bool = False,
) -> str:
    """
    Generate a reStructuredText string from a given JSON schema.

    Args:
        schema: The JSON schema to generate reStructuredText from.
        title: The title of the reStructuredText document.
        replace_refs: This feature is experimental. Whether to replace JSON references with their resolved values.
        suppress_undocumented: Whether to suppress definitions that have no title, description, or examples.
        section_punctuation: Punctuation characters to use for each nesting level of section headers.
        debug: Whether to print debug messages.

    Returns:
        str: The generated reStructuredText string.
    """
    # Set the log level
    if debug:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.remove()
        logger.add(sys.stderr, level="INFO")

    if replace_refs:
        import jsonref

        _schema: dict = jsonref.replace_refs(schema)  # type: ignore
    else:
        _schema = schema

    rst = ""

    # Add the title and description of the schema
    rst += _get_schema_header(
        _schema,
        title,
        "JSON Schema missing a description, provide it using the `description` key in the root of the JSON document.",
        section_punctuation,
        schema_level=0,
    )

    defs = _schema.get("definitions", _schema.get("$defs", {}))
    rst += _create_definition_table([], _schema, defs, [])

    if defs:
        for key, definition in defs.items():
            if suppress_undocumented and not any(
                definition.get(k) for k in ["title", "description", "examples"]
            ):
                continue

            rst += _get_schema_header(
                definition,
                key,
                "No description provided for this model.",
                section_punctuation,
                schema_level=1,
            )
            rst += _create_definition_table(
                [key], definition, defs, [_definition_anchor(key)]
            )

    res = rst.strip(" \n")
    res += "\n"

    return res


def _csv_cell(value) -> str:
    """
    Quote a value for use as a csv-table cell, escaping embedded double quotes.
    """
    return '"' + str(value).replace('"', '""') + '"'


def _create_definition_table(
    json_path: list,
    schema: dict,
    defs: dict,
    path_anchors: list,
    seen: frozenset = frozenset(),
) -> str:
    """
    Create a table of the properties in the schema.

    Returns: reStructuredText table with the following columns
    - Property name
    - Type
    - Required
    - Description

    Nested object/array properties get their own table below the field's
    detail block, with a breadcrumb showing the path back to the root.

    `json_path` holds the display name for each ancestor and `path_anchors`
    the matching anchor to link to; they are the same length. The first
    ancestor of a top-level definition's table is the definition itself
    (anchored via `_definition_anchor`), while every other ancestor is a
    property (anchored via `_property_anchor`).

    `seen` holds `id()` of every schema already being expanded along the
    current path. With `--resolve`, a recursive `$ref` is inlined by jsonref
    into a schema that (eventually) contains itself, which would otherwise
    recurse without end; `seen` lets us stop and note the cycle instead.
    """

    logger.debug(f"Creating definition table for schema: {schema}")
    seen = seen | {id(schema)}

    if "enum" in schema:
        logger.debug("Creating enum reStructuredText")
        return create_enum(schema)

    if "const" in schema:
        logger.debug("Creating const reStructuredText")
        return create_const(schema)

    rst = ""

    # Add a warning before the table to indicate if additional properties are allowed
    if not schema.get("additionalProperties", True):
        rst += "⚠️ Additional properties are not allowed.\n\n"

    if not schema.get("properties"):
        return rst

    # Boolean subschemas (`true`/`false`) are valid JSON Schema but not dicts;
    # normalize them so the rest of this function can assume a dict. `true`
    # imposes no constraints, `false` never validates.
    normalized_properties = {
        name: (
            details
            if isinstance(details, dict)
            else ({} if details else {"description": "Never valid.", "type": "never"})
        )
        for name, details in schema["properties"].items()
    }
    schema = {**schema, "properties": normalized_properties}

    # Use the sort_properties function to maintain the order
    sorted_properties = sort_properties(schema)

    table_items = []
    item_details = []

    for property_name, property_details in sorted_properties.items():
        property_type = property_details.get("type")

        logger.debug(f"Processing {property_name} of type {property_type}")
        logger.debug(f"Property details: {property_details}")

        type_formatted, possible_values = _get_property_details(
            property_type, property_details, defs
        )

        type_formatted = strip_inside_backticks(type_formatted)
        possible_values = strip_inside_backticks(possible_values)

        logger.debug(
            f"Finished processing {property_name} of type {property_type}: {possible_values}"
        )

        default = property_details.get("default")
        description = str(property_details.get("description", "")).strip(" \n")

        required = (
            "Required" if property_name in schema.get("required", []) else "Optional"
        )

        # Create an item anchor (with context) for referencing from table to item detail
        item_anchor = _property_anchor(json_path + [property_name])

        # Short description is either title or first sentence of description
        if property_details.get("title"):
            short_description = property_details.get("title")
        else:
            short_description = description.split(".")[0]

        # Trim and add link if short description is longer than 32 characters
        if len(short_description) > 32:
            short_description = short_description[:32] + f" :ref:`More <{item_anchor}>`"

        # Add backticks for each example, and join them with a comma and a space into a single string
        examples = ", ".join(
            [
                f"``{json.dumps(example)}``"
                for example in property_details.get("examples", [])
            ]
        )

        item = {
            "property": _csv_cell(f":ref:`{property_name} <{item_anchor}>`"),
            "type": _csv_cell(type_formatted),
            "required": _csv_cell(required),
            "description": _csv_cell(short_description),
        }

        table_items.append(item)

        # Generate item detail
        item_detail = f"\n----\n\n.. _{item_anchor}:\n\n"

        # Contextual (breadcrumb) header to field details
        # e.g. "Root > Parent > Field"
        # The path is italic with the last item in bold
        breadcrumb = [
            f":ref:`{name} <{anchor}>`" for name, anchor in zip(json_path, path_anchors)
        ]
        breadcrumb.append(f"**{property_name}**")
        item_detail += " > ".join(breadcrumb) + "\n\n"

        if description:
            item_detail += f"{description}\n\n"

        item_detail += f":Type: {type_formatted}\n"

        item_detail += f":Required: {required}\n"

        if property_details.get("deprecated"):
            item_detail += f":Deprecated: {property_details['deprecated']}\n"

        if default is not None:
            item_detail += f":Default: `{json.dumps(default)}`\n"

        if possible_values:
            item_detail += f":Possible Values: {possible_values}\n"

        if examples:
            item_detail += f":Examples: {examples}\n"

        item_details.append(item_detail)

        # If field type is object or array, add a table of its properties
        # by recursively calling this function.
        # This probably doesn't work for arrays yet, since arrays describe
        # their members via `items`, not `properties`.
        if _is_object_or_array(property_type):
            if id(property_details) in seen:
                item_details.append("\n*(recursive reference; not expanded further)*\n")
            else:
                sub_table = _create_definition_table(
                    json_path + [property_name],
                    property_details,
                    defs,
                    path_anchors + [item_anchor],
                    seen,
                )
                if sub_table:
                    item_details.append("\n" + sub_table)

    # Generate the header row
    capitalized_columns = [
        f'"{col.replace("_", " ").capitalize()}"' for col in table_items[0]
    ]

    # Generate the table
    table_title = schema.get("title", "")
    rst += (
        f".. csv-table:: {table_title}\n".rstrip() + "\n"
        f"   :header: {', '.join(capitalized_columns)}\n\n"
    )

    # Generate the item rows
    for item in table_items:
        rst += f"   {', '.join(item.values())}\n"

    return rst + "".join(item_details)


def _get_property_ref(ref, defs):
    # JSON pointer tokens are percent-decoded, then have ~1/~0 unescaped to / and ~.
    ref = urllib.parse.unquote(ref.split("/")[-1]).replace("~1", "/").replace("~0", "~")
    if ref in defs:
        t = defs[ref].get("type")
        return (
            f"`{t}`" if t else "Missing type",
            f":ref:`{ref} <{_definition_anchor(ref)}>`",
        )
    else:
        return "Missing type", "Missing definition"


def get_property_if_ref(property_details: dict, defs) -> tuple:
    """
    Check if the property is a reference.
    """

    # Check if the property is a reference
    ref_from_property = property_details.get("$ref")
    if ref_from_property:
        return _get_property_ref(ref_from_property, defs)

    # Check if the property is a reference in additionalProperties
    ref_from_additional_properties = (
        property_details["additionalProperties"].get("$ref")
        if isinstance(property_details.get("additionalProperties"), dict)
        else None
    )
    if ref_from_additional_properties:
        return _get_property_ref(ref_from_additional_properties, defs)

    return None, None


def _handle_array_like_property(
    property_type: str, property_details: dict, defs: dict, is_array=False
):
    """
    Handle properties that are array-like.
    """
    # TODO: Refactor this function to be more readable, handle arrays in a separate function

    array_type = (
        "oneOf"
        if "oneOf" in property_details
        else (
            "anyOf"
            if "anyOf" in property_details
            else "allOf"
            if "allOf" in property_details
            else None
        )
    )

    if array_type is None:
        logger.warning(
            f"Array-like property without oneOf, anyOf or allOf: {property_type} {property_details}"
        )
        # TODO: Support for items, prefixItems, contains, minContains, maxContains, uniqueItems, unevaluatedItems
        # https://json-schema.org/understanding-json-schema/reference/array
        return f"`{_format_type(property_type)}`", ""

    array_separator = {"oneOf": " or ", "anyOf": " and/or ", "allOf": " and "}

    # Work on a copy so the caller's schema is never mutated.
    subschemas = list(property_details[array_type])
    removed_null = False
    with contextlib.suppress(ValueError):
        subschemas.remove({"type": "null"})
        removed_null = True

    types = []
    details = []

    for value in subschemas:
        ref_type, ref_details = get_property_if_ref(value, defs)
        if ref_type or ref_details:
            types.append(ref_type)
            details.append(ref_details)
        else:
            ref_type, ref_details = _get_property_details(
                value.get("type"), value, defs
            )
            types.append(ref_type)
            details.append(ref_details)

    # FIXME: Hacky way to handle arrays with null values
    return_type = None
    if is_array:
        return_type = "`array`"
        if removed_null:
            return_type = "`array` or `null`"
    else:
        if removed_null:
            types.append("`null`")

    # Arrays should return the type as array
    # Other array-like properties should return the types of the nested oneOf, anyOf or allOf
    if return_type:
        return return_type, array_separator[array_type].join(sorted(details))
    else:
        # Dedeuplicate list of types, join them with null at the end if present
        types = sorted(set(types))
        if "`null`" in types:
            types.remove("`null`")
            types.append("`null`")
        return " or ".join(types), array_separator[array_type].join(sorted(details))


def _get_property_details(
    property_type: str, property_details: dict, defs: dict
) -> tuple[str, str]:
    """
    Get the possible values for a property.
    """

    # Check if the property is a reference
    ref_type, ref_details = get_property_if_ref(property_details, defs)
    if ref_type or ref_details:
        return ref_type, ref_details

    if "additionalProperties" in property_details and not isinstance(
        property_details["additionalProperties"], bool
    ):
        logger.warning(
            f"Additional properties not a boolean: {property_details['additionalProperties']}"
        )
        # new_type = property_details["additionalProperties"].get("type")
        # return new_type, new_type

    if "enum" in property_details:
        return (
            f"`{_format_type(property_type)}`",
            " ".join([f"`{str(value)}`" for value in property_details["enum"]]),
        )

    # Handle array-like properties
    if any(key in property_details for key in ["oneOf", "anyOf", "allOf"]):
        t, d = _handle_array_like_property(property_type, property_details, defs)
        if t and d:
            return t, d

    if property_details.get("items") == {}:
        return f"`{_format_type(property_type)}`", "Any type"

    if "items" in property_details:
        if any(key in property_details["items"] for key in ["oneOf", "anyOf", "allOf"]):
            t, d = _handle_array_like_property(
                property_type, property_details["items"], defs, is_array=True
            )
            if t and d:
                return t, d

        ref_type, ref_details = get_property_if_ref(property_details["items"], defs)
        if ref_type or ref_details:
            return f"`{_format_type(property_type)}`", ref_details
        else:
            ref_type, ref_details = _get_property_details(
                property_details["items"].get("type"), property_details["items"], defs
            )
            return f"`{_format_type(property_type)}`", ref_details

    elif "pattern" in property_details:
        pattern = property_details["pattern"]
        # Patterns containing backticks or angle brackets break the inline
        # hyperlink syntax below; fall back to a plain literal for those.
        if any(c in pattern for c in "`<>"):
            res_details = f"``{pattern}``"
        else:
            res_details = f"`{pattern} <https://regex101.com/?regex={urllib.parse.quote_plus(pattern)}>`_"
        return f"`{_format_type(property_type)}`", res_details

    elif "const" in property_details:
        res_details = f"`{property_details.get('const')}`"
        return "`const`", res_details

    elif property_type in ["integer", "number"]:
        # write the range of the integer in the format a <= x <= b
        minimum = property_details.get("minimum")
        maximum = property_details.get("maximum")
        exclusive_minimum = property_details.get("exclusiveMinimum")
        exclusive_maximum = property_details.get("exclusiveMaximum")

        min_details = ""
        max_details = ""
        res_details = ""

        if minimum is not None:
            min_details += f"{minimum} <="
        elif exclusive_minimum is not None:
            min_details += f"{exclusive_minimum} <"

        if maximum is not None:
            max_details += f"<= {maximum}"
        elif exclusive_maximum is not None:
            max_details += f"< {exclusive_maximum}"

        if min_details == "" and max_details == "":
            # fallback to original property_type when no range is specified
            res_details = _format_type(property_type)
        else:
            res_details = f"`{min_details} x {max_details}`"

        # check if multipleOf is present
        multiple_of = property_details.get("multipleOf")
        if multiple_of:
            res_details += f" and multiple of `{multiple_of}`"

        return f"`{_format_type(property_type)}`", res_details

    elif property_details.get("type") == "string":
        _format = property_details.get("format")
        _max_length = property_details.get("maxLength")
        _min_length = property_details.get("minLength")
        if _format:
            return (
                f"`{_format_type(property_type)}`",
                f"Format: `{_format}`",
            )
        elif _max_length or _min_length:
            if _max_length and _min_length:
                return (
                    f"`{_format_type(property_type)}`",
                    f"Length: `{_min_length} <= string <= {_max_length}`",
                )
            elif _max_length:
                return (
                    f"`{_format_type(property_type)}`",
                    f"Length: `string <= {_max_length}`",
                )
            elif _min_length:
                return (
                    f"`{_format_type(property_type)}`",
                    f"Length: `string >= {_min_length}`",
                )
            else:
                return f"`{_format_type(property_type)}`", _format_type(property_type)
        else:
            return f"`{_format_type(property_type)}`", _format_type(property_type)

    else:
        return f"`{_format_type(property_type)}`", _format_type(property_type)
