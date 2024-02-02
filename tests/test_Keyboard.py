import pytest
from src.Keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard("Example Keyboard", 50.0, 100)


def test_default_language_is_en(keyboard):
    assert keyboard.language == 'EN'


def test_change_language_to_ru(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'


def test_change_language_back_to_en(keyboard):
    keyboard.change_lang()
    keyboard.change_lang()
    assert keyboard.language == 'EN'
