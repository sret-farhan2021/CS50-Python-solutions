from bank import value

def test_assert():
    assert value("hello world") == 0
    assert value("HeLLo") == 0
