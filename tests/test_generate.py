from jsonschema_restructuredtext import generate
from tests.model import Car


def test_generate():
    schema = Car.model_json_schema()
    output = generate(schema)

    with open("tests/model.rst", "r") as f:
        expected_output = f.read()

    assert output == expected_output

