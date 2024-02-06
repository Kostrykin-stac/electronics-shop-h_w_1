import csv
from pathlib import Path


class InstantiateCSVError(Exception):
    pass


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

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
        Проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае,
        обрезать строку (оставить первые 10 символов)
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
    def instantiate_from_csv(cls, file_path='../src/items.csv'):
        """
        Создает экземпляры класса Item из данных в файле items.csv.
        """
        cls.all.clear()
        file_path = Path(__file__).parent.joinpath(file_path)

        try:
            with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                data = list(reader)
                for row in data:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

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

    def __add__(self, other):
        """Переопределение оператора сложения для
        экземпляров класса Item и Phone."""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError()
