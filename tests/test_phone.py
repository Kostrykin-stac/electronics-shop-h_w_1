import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


def test___init__(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone1) == 'iPhone 14'


@pytest.fixture
def testing_data():
    phone = Phone("iPhone 14", 120000, 5, 2)
    return phone


def test_number_of_sim(testing_data):
    phone = testing_data
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
        phone.number_of_sim = 1.2
