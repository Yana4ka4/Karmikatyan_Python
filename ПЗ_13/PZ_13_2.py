# Вариант 12. В двумерном списке найти отрицательные элементы, сформировать из них новый
# массив. Вывести размер полученного массива.

spisok = [
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
]

negatives = list(filter(lambda x: x < 0, [num for stroka in spisok for num in stroka]))

print(negatives)
print("Размер:", len(negatives))


