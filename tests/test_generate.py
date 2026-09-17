from jsonschema_restructuredtext import generate
from tests.model import Car


def test_generate():
    schema = Car.model_json_schema()
    output = generate(schema)

    with open("tests/model.rst", "r") as f:
        expected_output = f.read()

    assert output == expected_output


def test_generate_custom_title():
    schema = Car.model_json_schema()
    output = generate(schema, title="Car (custom title)")

    with open("tests/model_custom-title.rst", "r") as f:
        expected_output = f.read()

    assert output == expected_output
