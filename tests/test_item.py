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


@pytest.mark.parametrize("name, price, quantity", [("Смартфон с длинным названием", 100, 1),
                                                   ("Ноутбук с длинным названием", 1000, 3),
                                                   ("Кабель с длинным названием", 10, 5),
                                                   ("Мышка с длинным названием", 50, 5),
                                                   ("Клавиатура с длинным названием", 75, 5)
                                                   ])
def test_name_setter(name, price, quantity):
    item = Item("", price, quantity)
    item.name = name
    assert item.name == name[:10]


@pytest.mark.parametrize("name, price, quantity, total", [("Смартфон", 100, 1, 100), ("Ноутбук", 1000, 3, 3000),
                                                          ('Кабель', 10, 5, 50), ('Мышка', 50, 5, 250),
                                                          ('Клавиатура', 75, 5, 375)])
def test_calculate_total_price(name, price, quantity, total):
    item = Item(name, price, quantity)
    assert item.calculate_total_price() == total


@pytest.mark.parametrize("name, price, quantity, pay_rate, discount_price", [('Смартфон', 100, 1, 0.8, 80),
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


@pytest.mark.parametrize("name, price, quantity", [("Смартфон", 100, 1),
                                                   ("Ноутбук", 1000, 3),
                                                   ("Кабель", 10, 5),
                                                   ("Мышка", 50, 5),
                                                   ("Клавиатура", 75, 5)
                                                   ])
def test_repr(name, price, quantity):
    item = Item(name, price, quantity)
    assert repr(item) == f"Item('{name}', {price}, {quantity})"


@pytest.mark.parametrize("name, price, quantity, expected_str", [("Смартфон", 100, 1, 'Смартфон'),
                                                                 ("Ноутбук", 1000, 3, 'Ноутбук'),
                                                                 ("Кабель", 10, 5, 'Кабель'),
                                                                 ("Мышка", 50, 5, 'Мышка'),
                                                                 ("Клавиатура", 75, 5, 'Клавиатура'),
                                                                 ])
def test_str(name, price, quantity, expected_str):
    item = Item(name, price, quantity)
    assert str(item) == expected_str
