from src.item import Item
import pytest


@pytest.mark.parametrize('name, price, quantity, total', [('Смартфон', 100, 1, 100),
                                                          ('Ноутбук', 1000, 3, 3000),
                                                          ('Кабель', 10, 5, 50),
                                                          ('Мышка', 50, 5, 250),
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
