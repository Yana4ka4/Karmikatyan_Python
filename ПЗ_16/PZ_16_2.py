# Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год выпуска".
# От этого класса унаследуйте класс "Автомобиль" и добавьте в него свойство "тип кузова"

class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Car(Transport):
    def __init__(self, brand, model, year, body):
        super().__init__(brand, model, year)
        self.body = body

    def display_info(self):
        print(f"Бренд: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Тип кузова: {self.body}")


bmw = Car("BMW", "M4", 2018, "Купе")
bmw.display_info()
