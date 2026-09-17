import json
import os

import pytest

import jsonschema_restructuredtext

SCHEMA_EXAMPLES_DIR = "tests/schema-examples"


def get_test_cases():
    test_cases = []
    for filename in sorted(os.listdir(SCHEMA_EXAMPLES_DIR)):
        if filename.endswith(".json"):
            json_path = os.path.join(SCHEMA_EXAMPLES_DIR, filename)
            rst_path = os.path.join(
                SCHEMA_EXAMPLES_DIR, filename.replace(".json", ".rst")
            )
            test_cases.append((json_path, rst_path))
    return test_cases


@pytest.mark.parametrize("json_path, rst_path", get_test_cases())
def test_schema_examples(json_path, rst_path):
    with open(json_path, "r") as f:
        schema = json.load(f)

    with open(rst_path, "r") as f:
        expected_output = f.read()

    output = jsonschema_restructuredtext.generate(schema)
    assert output == expected_output
