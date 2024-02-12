
import datetime
import doctest


class Vehicle:
    """
    Базовый класс, описывающий транспортное средство.
    """
    TYPE = None

    def __init__(self, brand: str, year_release: int):
        """
        Инициализация базового класса Vehicle.
        :param brand: Бренд транспортного средства (строка)
        :param year_release: Год выпуска транспортного средства (целое число)


        :raise ValueError: Если тип автомобиля не указан
        :raise TypeError: Если бренд не является строкой
        :raise TypeError: Если год выпуска не является целым числом
        :raise ValueError: Если год выпуска не в диапазоне от 1900 до 2024

        Примеры:
        >>> Vehicle = Vehicle("Ford", 2005)
        Traceback (most recent call last):
        ValueError: Не указан тип автомобиля
        >>> Vehicle.TYPE = "Unknown"
        >>> Vehicle = Vehicle(999, 2015)
        Traceback (most recent call last):
        TypeError: Бренд должен быть строкой
        >>> Vehicle.TYPE = "Unknown"
        >>> Vehicle = Vehicle("Mitsubishi", "1987")
        Traceback (most recent call last):
        TypeError: Год выпуска должен быть целым числом
        >>> Vehicle.TYPE = "Unknown"
        >>> Vehicle = Vehicle("Kia", 1899)
        Traceback (most recent call last):
        ValueError: Год выпуска должен быть в диапазоне от 1900 до 2024
        >>> Vehicle.TYPE = "Unknown"
        >>> Vehicle = Vehicle("Ford", 1995)
        """
        if self.TYPE is None:
            raise ValueError('Не указан тип автомобиля')

        if not isinstance(brand, str):
            raise TypeError('Бренд должен быть строкой')
        self.brand = brand

        if not isinstance(year_release, int):
            raise TypeError('Год выпуска должен быть целым числом')
        if not (1900 <= year_release <= 2024):
            raise ValueError('Год выпуска должен быть в диапазоне от 1900 до 2024')
        self.year_release = year_release

    @property
    def age(self) -> int:
        """
        Возраст транспортного средства.

        :return: Возраст транспортного средства в годах

        Примеры:
        >>> Vehicle.TYPE = "Unknown"
        >>> Vehicle = Vehicle("Ford", 2004)
        >>> Vehicle.age
        20
        """
        return datetime.datetime.now().year - self.year_release

    def maintenance_cost(self, distance: int, maintenance_cost_per_km: int) -> float:
        """
        Рассчет общей стоимости обслуживания ТС для указанного расстояния в километрах.

        :param distance: Расстояние, которое необходимо пройти
        :param maintenance_cost_per_km: Стоимость обслуживания за каждый километр

        :return: Общая стоимость обслуживания

        Пример:
        >>> Vehicle.TYPE = "Unknown"
        >>> Vehicle = Vehicle("Ford", 1950)
        >>> Vehicle.maintenance_cost(300, 15)
        4500
        """
        return distance * maintenance_cost_per_km

    def __str__(self):
        """
        Возвращает строковое представление транспортного средства.

        :return: Строковое представление транспортного средства

        Пример:
        >>> Vehicle.TYPE = "Unknown"
        >>> Vehicle = Vehicle("Ford", 1950)
        >>> print(Vehicle)
        Unknown автомобиль: Ford 1950 года выпуска
        Возраст автомобиля: 74
        """
        return f"{self.TYPE} автомобиль: {self.brand} {self.year_release} года выпуска\nВозраст автомобиля: {self.age}"

    def __repr__(self):
        """
        Возвращает строковое представление класса транспортное средство.

        :return: Строковое представление класса транспортное средство

        Пример:
        >>> Vehicle.TYPE = "Unknown"
        >>> Vehicle = Vehicle("Ford", 1990)
        >>> print(repr(Vehicle))
        Vehicle(type='Unknown', brand='Ford', year_release=1990)
        """
        return f"{self.__class__.__name__}(type={self.TYPE!r}, brand={self.brand!r}, year_release={self.year_release})"


class Car(Vehicle):
    """
    Дочерний класс, описывающий легковой автомобиль.

    Примеры:
    >>> car = Car("Toyota", 1995, 5)
    >>> print(car)
    Легковой автомобиль: Toyota 1995 года выпуска
    Возраст автомобиля: 29
    """
    TYPE = "Легковой"

    def __init__(self, brand: str, year_release: int, seating_capacity: int):
        """
        Инициализация объекта легкового автомобиля.

        :param brand: Бренд автомобиля
        :param year_release: Год выпуска автомобиля
        :param seating_capacity: Количество мест в автомобиле

        :raise TypeError: Если количество мест не является целым числом

        Примеры:
        >>> car = Car("Toyota", 1995, "2")
        Traceback (most recent call last):
        TypeError: Количество мест должно быть целым числом
        >>> car = Car("Toyota", 1995, 2)
        """
        super().__init__(brand, year_release)
        if not isinstance(seating_capacity, int):
            raise TypeError('Количество мест должно быть целым числом')
        self.seating_capacity = seating_capacity    # Количество мест в автомобиле
        self._passenger_count = 0   # Безопасное изменение количества пассажиров только через метод

    @property
    def passenger_count(self) -> int:
        """
        Получение количества пассажиров в автомобиле.

        :return: Количество пассажиров в автомобиле

        Примеры:
        >>> car = Car("Lada", 2003, 4)
        >>> car.passenger_count = "7"
        Traceback (most recent call last):
        TypeError: Количество пассажиров должно быть целым числом
        >>> car.passenger_count = 7
        Traceback (most recent call last):
        ValueError: Количество пассажиров превышает количество мест
        >>> car.passenger_count = 4
        >>> car.passenger_count
        4
        """
        return self._passenger_count

    @passenger_count.setter
    def passenger_count(self, passenger_count: int):
        """
        Установка количества пассажиров в автомобиле.

        :param passenger_count: Количество пассажиров

        :raise TypeError: Если количество пассажиров не целое число
        :raise ValueError: Если количество пассажиров превышает количество мест

        """
        if not isinstance(passenger_count, int):
            raise TypeError('Количество пассажиров должно быть целым числом')
        if passenger_count > self.seating_capacity:
            raise ValueError('Количество пассажиров превышает количество мест')
        self._passenger_count = passenger_count

    def __repr__(self):
        """
        Возвращает строковое представление класса легкового автомобиля.

        :return: Cтроковое представление класса легкового автомобиля

        Примеры:
        >>> car = Car("Lada", 2001, 5)
        >>> car.passenger_count=3
        >>> print(repr(car))
        Car(type='Легковой', brand='Lada', year_release=2001, seating_capacity=5, passenger_count=3)
        """
        return f"{super().__repr__()[:-1]}, seating_capacity={self.seating_capacity!r}, passenger_count={self._passenger_count!r})"


class Truck(Vehicle):
    """
    Дочерний класс, описывающий грузовой автомобиль.

    Примеры:
    >>> truck = Truck("Volvo", 2015, 30)
    >>> print(truck)
    Грузовой автомобиль: Volvo 2015 года выпуска
    Возраст автомобиля: 9
    """
    TYPE = "Грузовой"

    def __init__(self, brand: str, year_release: int, cargo_capacity: int):
        """
        Инициализация объекта грузового автомобиля.

        :param brand: Бренд грузового автомобиля
        :param year_release: Год выпуска грузового автомобиля
        :param cargo_capacity: Грузоподъемность грузового автомобиля

        :raise ValueError: Если грузоподъемность не является целым числом

        Примеры:
        >>> truck = Truck("Volvo", 2015, 30.5)
        Traceback (most recent call last):
        TypeError: Грузоподъемность должна быть целым числом
        >>> truck = Truck("Volvo", 2015, 30)
        """
        super().__init__(brand, year_release)
        if not isinstance(cargo_capacity, int):
            raise TypeError("Грузоподъемность должна быть целым числом")
        self.cargo_capacity = cargo_capacity    # Грузоподъемность
        self._cargo_weight = 0   # Безопасное изменение веса груза только через метод

    @property
    def cargo_weight(self) -> (int, float):
        """
        Получение веса груза в грузовом автомобиле.

        :return: Вес груза в грузовом автомобиле

        Примеры:
        >>> truck = Truck("Volvo", 2015, 30)
        >>> truck.cargo_weight = "20"
        Traceback (most recent call last):
        TypeError: Вес груза должен быть вещественным или целым числом
        >>> truck.cargo_weight = 30.5
        Traceback (most recent call last):
        ValueError: Вес груза превышает грузоподъемность
        >>> truck.cargo_weight = 29.5
        >>> truck.cargo_weight
        29.5
        """
        return self._cargo_weight

    @cargo_weight.setter
    def cargo_weight(self, cargo_weight: (int, float)):
        """
        Присваивание веса груза в грузовом автомобиле.

        :param cargo_weight: Вес груза

        :raise TypeError: Если вес груза не является целым или вещественным числом
        :raise ValueError: Если вес груза превышает грузоподъемность

        """
        if not isinstance(cargo_weight, (int, float)):
            raise TypeError('Вес груза должен быть вещественным или целым числом')
        if cargo_weight > self.cargo_capacity:
            raise ValueError('Вес груза превышает грузоподъемность')
        self._cargo_weight = cargo_weight

    @property
    def load_capacity_utilization(self) -> float:
        """
        Получение процента загрузки грузовика.

        :return: Процент загрузки грузовика

        Пример:
        >>> truck = Truck("Volvo", 2015, 105)
        >>> truck.cargo_weight = 60.3
        >>> truck.load_capacity_utilization
        57.43
        """
        return round((self.cargo_weight / self.cargo_capacity) * 100, 2)

    def maintenance_cost(self, distance: int, maintenance_cost_per_km: int, cargo_handling_fee=1.0) -> float:
        """
        Рассчет общей стоимости обслуживания для указанного расстояния с учетом обработки груза.
        Метод перегружен так как добавляется параметр - Дополнительная плата за обработку груза

        :param distance: Расстояние, которое необходимо пройти
        :param maintenance_cost_per_km: Стоимость обслуживания за каждый километр
        :param cargo_handling_fee: Дополнительная плата за обработку груза

        :return: Общая стоимость обслуживания

        Пример:
        >>> truck = Truck("Volvo", 2015, 500)
        >>> truck.cargo_weight = 400
        >>> truck.maintenance_cost(200, 8, 2)
        2400
        """
        base_cost = super().maintenance_cost(distance, maintenance_cost_per_km)
        additional_cost = self.cargo_weight * cargo_handling_fee
        return base_cost + additional_cost

    def __repr__(self):
        """
        Возвращает строковое представление класса грузового автомобиля.

        :return: Cтроковое представление класса грузового автомобиля

        Примеры:
        >>> truck = Truck("MAN", 2001, 50)
        >>> truck.cargo_weight = 30.1
        >>> print(repr(truck))
        Truck(type='Грузовой', brand='MAN', year_release=2001, cargo_capacity=50, cargo_weight=30.1)
        """
        return f"{super().__repr__()[:-1]}, cargo_capacity={self.cargo_capacity!r}, cargo_weight={self._cargo_weight!r})"


if __name__ == "__main__":
    # Write your solution here
    doctest.testmod()
