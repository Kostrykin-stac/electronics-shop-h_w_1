from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона в магазине.
    Унаследован от класса Item.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """Создание экземпляра класса Phone."""
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Возвращает количество поддерживаемых сим-карт."""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Устанавливает количество поддерживаемых сим-карт."""
        if int(value) >= 0:
            self.__number_of_sim = int(value)
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        """Возвращает строковое представление объекта для отображения в режиме отладки"""
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """Возвращает строковое представление
        объекта для отображения пользователю"""
        return self.name
