import json

import click

import jsonschema_restructuredtext

def parse_comma_separated(ctx, param, value):
    if not value:
        return []

    # Since 'multiple=True', the input will be a tuple; combine all inputs into a single string
    combined = ",".join(value)

    # Split on commas to create a list
    return [item.strip() for item in combined.split(",")]

@click.command()
@click.argument("filename", type=click.File("r"))
@click.option(
    "-t",
    "--title",
    type=str,
    help="Do not use the title from the schema, use this title instead.",
)
@click.option(
    "--resolve/--no-resolve",
    is_flag=True,
    default=False,
    show_default=True,
    help="[Experimental] Resolve $ref pointers.",
)
@click.option(
    "--suppress-undocumented/--no-suppress-undocumented",
    is_flag=True,
    default=False,
    show_default=True,
    help="Suppress output of properties that do not have title, description, or examples.",
)
@click.option(
    "--section-punctuation",
    multiple=True,
    default=jsonschema_restructuredtext.constants.DEFAULT_SECTION_PUNCTUATION,
    show_default=True,
    callback=parse_comma_separated,
    help="Provide a comma-separated list of punctuation values to use for sections.",
)
@click.option(
    "--debug/--no-debug",
    is_flag=True,
    default=False,
    show_default=True,
    help="Enable debug output.",
)
@click.version_option(package_name="jsonschema_restructuredtext")
def cli(filename, title, resolve, suppress_undocumented, section_punctuation, debug):
    """
    Load FILENAME and output a reStructuredText version.

    Use '-' as FILENAME to read from stdin.
    """

    file_contents = json.loads(filename.read())

    kwargs = {
        "replace_refs": resolve,
        "suppress_undocumented": suppress_undocumented,
        "section_punctuation": section_punctuation,
        "debug": debug,
    }

    if title:
        kwargs["title"] = title

    # Convert the file contents to restructuredtext
    rst = jsonschema_restructuredtext.generate(file_contents, **kwargs)

    # Output the restructuredtext
    click.echo(rst, nl=False)
