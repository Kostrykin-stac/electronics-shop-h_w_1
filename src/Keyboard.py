from src.item import Item


class Lang:
    def __init__(self):
        self.__language = 'EN'
        super().__init__()

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        self.__language = language

    def change_lang(self):
        if self.__language.upper() == 'RU':
            self.__language = 'EN'
        elif self.__language.upper() == 'EN':
            self.__language = 'RU'
        return self

    def __str__(self):
        return f'Language: {self.language}'


class Keyboard(Item, Lang):
    def __init__(self, name: str, price: float, quality: int) -> None:
        super().__init__(name, price, quality)
        Lang.__init__(self)

    def __str__(self) -> str:
        return f'{self.name}'