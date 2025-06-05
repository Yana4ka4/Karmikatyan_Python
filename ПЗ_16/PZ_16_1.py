# Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
# выводит информацию о животном в формате "Имя: имя, Вид: вид"

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print(f"Имя: {self.name}, Вид: {self.species}")


animal1 = Animal("Буся", "Кот")
animal2 = Animal("Рекс", "Собака")
animal3 = Animal("Кеша", "Попугай")
