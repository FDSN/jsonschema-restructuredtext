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
                                  Suppress output of properties that do not
                                  have title, description, or examples.
                                  [default: no-suppress-undocumented]
  --section-punctuation TEXT      Provide a comma-separated list of
                                  punctuation values to use for sections.
                                  [default: =, -, ^, ~, +, *, +, .]
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
  - Nested objects with dot notation (e.g., `parent.child[].property`)
  - Basic `oneOf`, `anyOf`, `allOf` functionality
  - Arrays
  - Integers with minimum, maximum values and exclusives
  - Boolean values
  - Deprecated fields (using the `deprecated` option, additionally searches for case-insensitive `deprecated` in the field description)
  - Supports optional YAML and JSON formatting for examples

## Caveats
  - Custom definitions are expected to be in the same file as the schema that uses them,
    in the `definitions` or `$defs` parameter at the root of the document.

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
The following reStructuredText will be generated:

```
----
.. _example-json-schema:

Example JSON Schema
===================
A representation of a movie

Type: `object`

.. csv-table::
   :header: "Property", "Type", "Required", "Description"

   :ref:`title <title>`, "`string`", "Required", ""
   :ref:`director <director>`, "`string`", "Required", ""
   :ref:`releaseDate <releasedate>`, "`string`", "Required", ""
   :ref:`genre <genre>`, "`string`", "Required", ""
   :ref:`duration <duration>`, "`string`", "Required", ""
   :ref:`cast <cast>`, "`array`", "Required", ""

----

.. _title:

**title**

:Type: string
:Required: Required
:Possible Values: string

----

.. _director:

**director**

:Type: string
:Required: Required
:Possible Values: string

----

.. _releasedate:

**releaseDate**

:Type: string
:Required: Required
:Possible Values: Format: `date`

----

.. _genre:

**genre**

:Type: string
:Required: Required
:Possible Values: `Action` `Comedy` `Drama` `Science Fiction`

----

.. _duration:

**duration**

:Type: string
:Required: Required
:Possible Values: string

----

.. _cast:

**cast**

:Type: array
:Required: Required
:Possible Values: string
```
