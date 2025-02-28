import pytest

from jsonschema_restructuredtext.converter.rst import _format_example


@pytest.mark.parametrize(
    "example, format_type, expected",
    [
        ({"key": "value"}, "yaml", "```yaml\nkey: value\n\n```"),
        ("example string", "yaml", "```yaml\nexample string\n```"),
        ({"key": "value"}, "json", '```json\n{\n  "key": "value"\n}\n```'),
        ("example string", "json", "```json\nexample string\n```"),
        ({"key": "value"}, "text", "```\n{'key': 'value'}\n```"),
        ({"key": "value"}, "invalid_format", "```\n{'key': 'value'}\n```"),
    ],
)
def test_generate_examples_format(example, format_type, expected):
    formatted = _format_example(example, format_type)
    assert formatted == expected
