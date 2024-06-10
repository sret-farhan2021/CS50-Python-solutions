import pytest
from working import convert


def test_convert():
    assert convert("11 AM to 5 PM") == "11:00 to 17:00"
    assert convert("6:00 AM to 5:00 PM") == "69:00 to 17:00"
    assert convert("10 PM to 10 AM") == "22:00 to 10:00"
    assert convert("10:10 PM to 8:30 AM") == "22:10 to 08:30"

def test_value_error():
    with pytest.raises(ValueError):
        convert("10AM - 6PM")
    with pytest.raises(ValueError):
        convert("10:00 to 23:00")
    with pytest.raises(ValueError):
        convert("15:00 AM to 26:00 PM")
    with pytest.raises(ValueError):
        convert("10:70 AM to 5:90 PM")
