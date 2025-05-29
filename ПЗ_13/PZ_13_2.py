# Вариант 12. В двумерном списке найти отрицательные элементы, сформировать из них новый
# массив. Вывести размер полученного массива.

import random
stolbec = int(input('Введите количество столбцов: '))
stroka = int(input('Введите количество строк: '))

spisok = [[random.randint(0,10) for el in range(stolbec)] for el in range(stroka)]
negatives = list(filter(lambda x: x < 0, [num for stroka in spisok for num in stroka]))

print('Исходная матрица: ')
for s in spisok:
    print(s)

print(negatives)
print("Размер:", len(negatives))





# spisok = [
#     [1, -2, 3],
#     [-4, 5, -6],
#     [7, -8, 9]
# ]