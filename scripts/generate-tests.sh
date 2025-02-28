#!/bin/bash

set -euo pipefail

TEST_DIR="$(dirname "$0")/../tests/schema-examples"

# Generate reStructuredText files for each test case
for file in "$TEST_DIR"/*.json; do
    echo "Generating reStructuredText for $file"
    jsonschema-restructuredtext "$file" > "${file%.json}.rst"
done

# Generate markdown file for Python example
echo "Generating reStructuredText for Python example"
python3 "$TEST_DIR"/../model.py | jsonschema-restructuredtext - > "$TEST_DIR/../model.rst"

echo "Generating reStructuredText for Python example with custom title and no footer"
python3 "$TEST_DIR"/../model.py | jsonschema-restructuredtext --title "Car (custom title)" - > "$TEST_DIR/../model_custom-title.rst"
