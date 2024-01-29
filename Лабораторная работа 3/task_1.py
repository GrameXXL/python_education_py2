class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 1:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом")
        self._duration = duration

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, duration={self.duration!r})"
