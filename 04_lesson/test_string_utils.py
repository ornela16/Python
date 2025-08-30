import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python") ] )
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""), ("   ", "   "), ("-.","-.") ] )
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(None)
def capitalize_empty(in_string):
    if not isinstance(in_string):
        raise TypeError("Параметр 'in_string' должен быть строкой")
        res == string.capitalize_empty(None)
    assert string_utils.capitalize_empty(in_string) == TypeError


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [ (" skypro", "skypro"),
        (" python", "python") ] )
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [ ("  skypro", "skypro"),
        (" 333", "333"), (" +7","+7"), (" ","") ] )
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, result", [ ("test","t",True),
    ("Python","h",True), ("lesson","s",True), ("678","6",True) ] )
def test_contains_positive(input_str, input_symbol, result):
    res = string_utils.contains(input_str, input_symbol)
    assert  res == result

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, result", [ ("test","b",False),
    (" ","a",False), ("555","s",False), ("-symbol",",",False), ("007","2",False)])
def test_contains_negative(input_str, input_symbol, result):
    res = string_utils.contains(input_str, input_symbol)
    assert  res == result


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, result", [ ("Skyprof","f","Skypro"),("python","thon","py"),
    ("01 сентября","0","1 сентября") ] )
def test_delete_symbol_positive(input_str, input_symbol, result):
    res = string_utils.delete_symbol(input_str, input_symbol)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, result", [ ("Skypro","f","Skypro"),(" ","t"," "),
    ("123","a","123") ] )
def test_delete_symbol_negative(input_str, input_symbol, result):
    res = string_utils.delete_symbol(input_str, input_symbol)
    assert res == result
