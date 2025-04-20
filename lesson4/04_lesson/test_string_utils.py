import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тестирование метода capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"), # Проверка чисел
    ("", ""),             # Пустая строка
    ("   ", "   "),       # Строка из пробелов
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Тестирование метода trim
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  кот", "кот"),
    ("   hello", "hello"),
    ("world", "world"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("кот", "кот"),          # Нет начальных пробелов
    ("", ""),                # Пустая строка
    ("     ", ""),           # Только пробелы
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Тестирование метода contains
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),      # Символ присутствует
    ("SkyPro", "y", True),      # Символ присутствует
    ("test", "t", True),        # Символ повторяется дважды
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),     # Символ отсутствует
    ("", "", False),            # Пустые аргументы
    ("SkyPro", "s", False),     # Различие регистров
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# Тестирование метода delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),               # Успешное удаление символа
    ("SkyPro", "Pro", "Sky"),               # Успешное удаление подстроки
    ("Test", "T", "est"),                   # Первая буква
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "z", "SkyPro"),              # Символ отсутствует
    ("", "a", ""),                         # Пустая строка
    ("SkyPro", "SKYPRO", "SkyPro"),         # Регистр важен
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

