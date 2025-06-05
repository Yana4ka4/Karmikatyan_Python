# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохранять
# информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно. Использовать модуль
# pickle для сериализации и десериализации объектов Python в бинарном формате.

import pickle
from PZ_16_1 import animal1, animal2, animal3

def save_def(animals, file):
    with open(file, 'wb') as f:
        pickle.dump(animals, f)

def load_def(file):
    with open(file, 'rb') as f:
        return pickle.load(f)


save_def([animal1, animal2, animal3], 'animals.pkl')

loaded_animals = load_def('animals.pkl')

for animal in loaded_animals:
    animal.display_info()
