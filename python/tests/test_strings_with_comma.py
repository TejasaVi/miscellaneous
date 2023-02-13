import pytest
from .string_with_comma import string_with_commas


@pytest.mark.parametrize(
    ("input","expected"),
    [
        ("#",""),
        ("9", "9"),
        ("+9","9"),
        (" 9", "9"),
        ("9 ","9"),
        (" 9 ","9"),
        ("-9","-9"),
        ("9 0","90"),
        ("10", "10"),
        ("100", "100"),
        ("1000", "1,000"),
        ("-1000", "-1,000"),
        ("+1000", "1,000"),
        ("+10 00", "1,000"),
        ("+10#00", ""),
        ("10000", "10,000"),
        ("900000", "9,00,000"),
    ],
)
def test_string_with_commas(input, expected):
    assert string_with_commas(input) == expected
