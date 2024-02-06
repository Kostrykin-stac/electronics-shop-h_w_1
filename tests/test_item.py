import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.mark.parametrize("name, price, quantity", [("Смартфон", 100, 1),
                                                   ("Ноутбук", 1000, 3),
                                                   ('Кабель', 10, 5),
                                                   ('Мышка', 50, 5),
                                                   ('Клавиатура', 75, 5)
                                                   ])
def test_instantiate_from_csv(name, price, quantity):
    Item.instantiate_from_csv('../src/items.csv')
    found = False
    for item in Item.all:
        if item.name == name and item.price == price and item.quantity == quantity:
            found = True
            break
    assert found, f"Item with name '{name}', price '{price}', and quantity '{quantity}' not found in Item.all"


def test_instantiate_csv_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/error.csv')


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('src/item.csv')


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


@pytest.mark.parametrize("item1, item2, expected_quantity", [
    (Item("Ноутбук", 1000, 3), Item("Телефон", 500, 2), 5),
    (Item("Мышка", 200, 4), Item("Клавиатура", 300, 2), 6),
])
def test_add_item_objects(item1, item2, expected_quantity):
    result = item1 + item2
    assert result == expected_quantity, f"Добавление предметов объектов не вернуло ожидаемое количество. Result: {result}, Expected: {expected_quantity}"


@pytest.mark.parametrize(
    "item_name, item_price, item_quantity, phone_name, phone_price, phone_quantity, expected_result", [
        ("Смартфон", 10000, 20, "iPhone 14", 120000, 5, 25),
        ("Ноутбук", 50000, 10, "Samsung Galaxy", 80000, 3, 13),
    ])
def test_add(item_name, item_price, item_quantity, phone_name, phone_price, phone_quantity, expected_result):
    item = Item(item_name, item_price, item_quantity)
    phone = Phone(phone_name, phone_price, phone_quantity, 2)
    assert item + phone == expected_result
