import csv


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
        file_path = '/home/maxim/PycharmProjects/electronics-shop-h_w_1/src/items.csv'
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                #name = row['name']
                #price = cls.string_to_number(row['price'])
                #quantity = int(row['quantity'])
                #cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> float:
        """
        Преобразует строку с числом в число.

        :param value: Строка с числом.
        :return: Число.
        """
        return float(value)
