import json
import re


def create_section(punc: str, anchor: str, header: str) -> str:
    """
    Create rst section header.
    """

    output = "\n----\n\n"
    output += f".. _{anchor}:\n"
    output += f"\n{header}\n"
    output += punc * len(header) + "\n"

    return output


def format_literal(value) -> str:
    """
    Render a JSON value as an RST inline literal: strings keep their quotes,
    numbers, booleans and null are bare, and all of them render as monospace.
    """
    return f"``{json.dumps(value)}``"


def format_literal_list(values) -> str:
    """
    Render a list of JSON values as comma-separated RST inline literals.
    """
    return ", ".join(format_literal(value) for value in values)


def create_enum(schema: dict) -> str:
    """
    Create markdown/rst for enum values.
    """

    return f"**Possible Values:** {format_literal_list(schema['enum'])}\n\n"


def create_const(schema: dict) -> str:
    """
    Create markdown/rst value for const values.
    """

    return f"**Possible Values:** {format_literal(schema['const'])}\n\n"


def sort_properties(schema: dict) -> dict:
    """
    Sort the properties in the schema by required, making the deprecated properties last.
    """
    properties = schema["properties"]

    # Sort the properties by required
    properties = dict(
        sorted(
            properties.items(),
            key=lambda item: item[0] not in schema.get("required", []),
        )
    )

    # Sort the properties by deprecated
    properties = dict(
        sorted(
            properties.items(),
            key=lambda item: (
                "[deprecated]" in str(item[1].get("description", "")).lower()
                or item[1].get("deprecated", False)
            ),
        )
    )

    return properties


def strip_inside_backticks(text):
    """
    Remove leading and trailing spaces inside backticks.

    Passes non-string input through unchanged; every caller is expected to
    supply a formatted string, but this keeps a formatting miss elsewhere
    from turning into a crash here.
    """
    if not isinstance(text, str):
        return text
    return re.sub(r"`(.*?)`", lambda match: f"`{match.group(1).strip()}`", text)


def dashify(text):
    """
    Replace spaces and underscores with dashes and make lowercase.
    """
    return re.sub(r"[_ ]", "-", text).lower()
