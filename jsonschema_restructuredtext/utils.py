import re

def create_section(punc: str, anchor: str, header: str) -> str:
    """
    Create rst section header.
    """

    output = f".. _{anchor}:\n"
    output += f"\n{header}\n"
    output += punc * len(header) + "\n"

    return output

def create_enum(schema: dict) -> str:
    """
    Create markdown/rst for enum values.
    """

    output = "**Possible Values:** "
    output += " or ".join([f"`{value}`" for value in schema["enum"]]) + "\n\n"

    return output


def create_const(schema: dict) -> str:
    """
    Create markdown/rst value for const values.
    """

    return f"**Possible Values:** {schema.get('const', '?')}\n\n"


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
            key=lambda item: "[deprecated]"
            in str(item[1].get("description", "")).lower()
            or item[1].get("deprecated", False),
        )
    )

    return properties

def strip_inside_backticks(text):
    """
    Remove leading and trailing spaces inside backticks.
    """
    return re.sub(r'`(.*?)`', lambda match: f"`{match.group(1).strip()}`", text)

def dashify(text):
    """
    Replace spaces and underscores with dashes and make lowercase.
    """
    return re.sub(r'[_ ]', '-', text).lower()
