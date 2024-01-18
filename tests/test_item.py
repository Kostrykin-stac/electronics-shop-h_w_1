import pytest
from src.item import Item


@pytest.mark.parametrize("name, price, quantity", [("Смартфон", 100, 1), ("Ноутбук", 1000, 3),
                                                   ('Кабель', 10, 5), ('Мышка', 50, 5),
                                                   ('Клавиатура', 75, 5)])
def test_instantiate_from_csv(name, price, quantity):
    item = Item(name, price, quantity)
    assert item.name == name
    assert item.price == price
    assert item.quantity == quantity


@pytest.mark.parametrize("name, value, expected_result", [
    ("Смартфон", "ДлинноеНазвание", "ДлинноеНаз"),
    ("Ноутбук", "Коротко", "Коротко")
])
def test_name_setter(name, value, expected_result):
    item = Item(name, 100, 1)
    item.name = value
    assert item.name == expected_result


@pytest.mark.parametrize("name, price, quantity, total", [("Смартфон", 100, 1, 100), ("Ноутбук", 1000, 3, 3000),
                                                          ('Кабель', 10, 5, 50), ('Мышка', 50, 5, 250),
                                                          ('Клавиатура', 75, 5, 375)])
def test_calculate_total_price(name, price, quantity, total):
    item = Item(name, price, quantity)
    assert item.calculate_total_price() == total


@pytest.mark.parametrize("name, price, quantity, pay_rate, discount_price",
                         [('Смартфон', 100, 1, 0.8, 80),
                          ('Ноутбук', 1000, 3, 0.8, 800),
                          ('Кабель', 10, 5, 0.8, 8),
                          ('Мышка', 50, 5, 0.8, 40),
                          ('Клавиатура', 75, 5, 0.8, 60)])
def test_apply_discount(name, price, quantity, pay_rate, discount_price):
    item = Item(name, price, quantity)
    Item.pay_rate = pay_rate
    item.apply_discount()
    assert item.price == discount_price


@pytest.mark.parametrize("value, expected", [("10.0", 10.0), ("5.0", 5.0)])
def test_string_to_number(value, expected):
    assert Item.string_to_number(value) == expected