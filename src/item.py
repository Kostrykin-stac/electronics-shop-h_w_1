import csv
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        """
        Геттер для приватного атрибута name.
        Возвращает значение приватного атрибута name.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Сеттер для приватного атрибута name.
        Присваивает значение приватному атрибуту name.
        Если длина переданного значения больше 10 символов, обрезает его до 10 символов.

        :param value: Новое значение для названия товара.
        """
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path) -> None:
        """
        Создает экземпляры класса Item из данных в файле items.csv.
        """
        cls.all.clear()
        file_path = Path(__file__).parent.joinpath("items.csv")
        with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            for row in data:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> float:
        """Преобразует строку с числом в число."""
        return int(float(value))

    def __repr__(self):
        """Возвращает строковое представление объекта
         для отображения в режиме отладки"""
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Возвращает строковое представление
         объекта для отображения пользователю"""
        return self.name
