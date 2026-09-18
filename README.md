# jsonschema-restructuredtext

Generate reStructuredText documentation from JSON Schema files. The main goal is to generate
documentation that is easy to read and understand.

Can be used as a command line tool or as a library.

> [!NOTE]
> This tool is not intended for general use (yet), and may produce undesirable output
> for arbitrary schemas outside of the FDSN use cases.

## Installation

```bash
pip install git+https://github.com/FDSN/jsonschema-restructuredtext.git@main
```

## Usage

To use `jsonschema-restructuredtext` as a CLI, just pass the filename as an argument and redirect
the output to a file.

```bash
$ jsonschema-restructuredtext --help
Usage: jsonschema-restructuredtext [OPTIONS] FILENAME

  Load FILENAME and output a reStructuredText version.

  Use '-' as FILENAME to read from stdin.

Options:
  -t, --title TEXT                Do not use the title from the schema, use
                                  this title instead.
  --resolve / --no-resolve        [Experimental] Resolve $ref pointers.
                                  [default: no-resolve]
  --suppress-undocumented / --no-suppress-undocumented
                                  Suppress output of definitions that do not
                                  have title, description, or examples.
                                  [default: no-suppress-undocumented]
  --section-punctuation TEXT      Provide a comma-separated list of
                                  punctuation values to use for sections.
                                  [default: =, -, ^, ~, +, *, #, .]
  --debug / --no-debug            Enable debug output.  [default: no-debug]
  --version                       Show the version and exit.
  --help                          Show this message and exit.

# Example
$ jsonschema-restructuredtext --title "My JSON Schema" schema.json > schema.rst
```

## Usage as a library

To use it as a library, load your JSON schema file as Python `dict` and pass it to generate.
The function will return a string with the reStructuredText.

```python
import jsonschema_restructuredtext

with open('schema.json') as f:
    schema = json.load(f)

rst = jsonschema_restructuredtext.generate(schema)
```

## Features

The goal is to support the latest JSON Schema specification, `2020-12`. However,
this project does not currently support all features, but it should support:

  - Required fields
  - String patterns
  - Enumerations
  - Default values
  - Descriptions and titles
  - Nested objects using `$defs` or `definitions`
  - Nested objects and arrays get their own sub-table, with breadcrumbs showing the path back to the root (arrays of objects are not yet expanded this way)
  - Basic `oneOf`, `anyOf`, `allOf` functionality
  - Arrays
  - Integers with minimum, maximum values and exclusives
  - Boolean values
  - Deprecated fields (using the `deprecated` option, additionally searches for case-insensitive `deprecated` in the field description)
  - Examples formatted as JSON

## Caveats
  - Custom definitions are expected to be in the same file as the schema that uses them,
    in the `definitions` or `$defs` parameter at the root of the document.

## Development

Create a virtual environment and install the project editable, along with its dev
dependencies (the `dev` group defined in `pyproject.toml`):

```bash
python3 -m venv venv
venv/bin/python -m pip install -e . --group dev
```

`--group dev` requires `pip>=25.1`; on an older `pip`, upgrade first with
`venv/bin/python -m pip install --upgrade pip`.

Activate the virtual environment, then run the tests and linter:

```bash
source venv/bin/activate
pytest
ruff check .
```

---

## Examples

### Example 1 Input

Given the following JSON Schema:
```json
{
  "$id": "https://example.com/movie.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "description": "A representation of a movie",
  "type": "object",
  "required": ["title", "director", "releaseDate"],
  "properties": {
    "title": {
      "type": "string"
    },
    "director": {
      "type": "string"
    },
    "releaseDate": {
      "type": "string",
      "format": "date"
    },
    "genre": {
      "type": "string",
      "enum": ["Action", "Comedy", "Drama", "Science Fiction"]
    },
    "duration": {
      "type": "string"
    },
    "cast": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "additionalItems": false
    }
  }
}
```

### Example 1 Output
Running `jsonschema-restructuredtext --title "Example JSON Schema" movie-schema.json`
generates the following reStructuredText:

```
----

.. _def-example-json-schema:

Example JSON Schema
===================
A representation of a movie

Type: `object`

.. csv-table::
   :header: "Property", "Type", "Required", "Description"

   ":ref:`title <prop-title>`", "`string`", "Required", ""
   ":ref:`director <prop-director>`", "`string`", "Required", ""
   ":ref:`releaseDate <prop-releasedate>`", "`string`", "Required", ""
   ":ref:`genre <prop-genre>`", "`string`", "Optional", ""
   ":ref:`duration <prop-duration>`", "`string`", "Optional", ""
   ":ref:`cast <prop-cast>`", "`array`", "Optional", ""

----

.. _prop-title:

**title**

:Type: `string`
:Required: Required
:Possible Values: string

----

.. _prop-director:

**director**

:Type: `string`
:Required: Required
:Possible Values: string

----

.. _prop-releasedate:

**releaseDate**

:Type: `string`
:Required: Required
:Possible Values: Format: `date`

----

.. _prop-genre:

**genre**

:Type: `string`
:Required: Optional
:Possible Values: ``"Action"``, ``"Comedy"``, ``"Drama"``, ``"Science Fiction"``

----

.. _prop-duration:

**duration**

:Type: `string`
:Required: Optional
:Possible Values: string

----

.. _prop-cast:

**cast**

:Type: `array`
:Required: Optional
:Possible Values: string
```

### Credit

This project is a cannibalization of:
https://github.com/elisiariocouto/jsonschema-markdown
