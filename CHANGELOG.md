## 0.0.4
- Report a schema with an `enum` but no `type` as type `enum`, instead of `unspecified`,
`object(?)` or `Missing type`

## 0.0.3

- Fix crash when a property references a definition that does not exist
- Fix crash when a property is marked `deprecated`
- Fix crash when a schema's `type` is a list, e.g. `["object", "null"]`
- Fix crash when fewer section punctuation characters are given than nesting levels
- Fix `Required` column marking every property required when any property was required
- Apply the required-first, deprecated-last property ordering that was computed but unused
- Escape quotes in csv-table cells so titles and descriptions cannot break the table
- Show `default` and `const` values that are falsy, such as `0`, `false` and `""`
- Stop modifying the caller's schema, so repeated calls return the same output
- Emit nested property tables and detail blocks flush-left instead of as a blockquote
- Report a `deprecated` property in its detail block
- Fix breadcrumb links for properties nested more than one level deep
- Fall back to a plain literal when a regex pattern would break the regex101 link
- Namespace definition and property anchors separately to avoid duplicate labels
- Fix the schema-example tests, which collected no cases and never ran
- Remove stale markdown fixtures left over from the upstream markdown project
- Drop the unused `pyyaml` dependency
- Fix crash when a property has no `type`, or only a `description`
- Fix crash when a property's `type` is a list, e.g. `["string", "null"]`
- Fix crash when a property is the boolean subschema `true` or `false`
- Fix crash when a `description` is not a string
- Fix `--resolve` recursing forever on a schema with a recursive `$ref`
- Fix `--section-punctuation ""` silently emitting a section header with no underline
- Reject a `--section-punctuation` value that is not a single, valid RST punctuation character
- Fix a duplicate punctuation character in the default section punctuation list
- Recurse into nested tables for a property whose `type` is a list including `object`/`array`, not just a bare `object`/`array`
- Strip the trailing space `csv-table` directives left when a schema/property had no title, which fought the `trailing-whitespace` pre-commit hook and never converged
- Correct the `--suppress-undocumented` help text: it suppresses definitions, not properties
## 0.0.2

- Allow recursion into objects and arrays with sub-tables, adding breadcrumbs for nesting
- Fix reference links
- Format examples as JSON instead of Python dictionaries

## 0.0.1

Initial version based on jsonschema-markdown v0.3.18 by Elisiário Couto
https://github.com/elisiariocouto/jsonschema-markdown
