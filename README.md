# jsonschema-restructuredtext

Generate reStructuredText documentation from JSON Schema files. The main goal is to generate
documentation that is easy to read and understand.

Can be used as a command line tool or as a library.

## Installation

```bash
pipx install jsonschema-restructuredtext
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
  --footer / --no-footer          Add a footer with a link to the project.
                                  [default: footer]
  --empty-columns / --no-empty-columns
                                  Remove empty columns from the output, useful
                                  when deprecated or examples are not used.
                                  [default: empty-columns]
  --resolve / --no-resolve        [Experimental] Resolve $ref pointers.
                                  [default: no-resolve]
  --debug / --no-debug            Enable debug output.  [default: no-debug]
  --examples-format [text|yaml|json]
                                  Format of the examples in the output.
                                  [default: text]
  --version                       Show the version and exit.
  --help                          Show this message and exit.

# Example
$ jsonschema-restructuredtext schema.json > schema.rst
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

---


---

### Example 2

In [tests/model.py](tests/model.py) you can see a more complex example of a model that is exported as a JSON Schema.

The output can be seen in [tests/model.md](tests/model.md).
