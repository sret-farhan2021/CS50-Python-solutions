from plates import is_valid


def test_begintwoletters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False


def test_length():
    assert is_valid("ABCS50") == True
    assert is_valid("AC") == True
    assert is_valid("HELLOCS50") == False

def test_num():
    assert is_valid("AXD222") == True
    assert is_valid("AJS22A") == False
    assert is_valid("ASA022") == False


def test_punct():
    assert is_valid("AC50!") == False
