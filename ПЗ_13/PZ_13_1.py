# Вариант 12. В двумерном списке найти сумму и произведение элементов столбца N (N задать с
# клавиатуры).

from functools import reduce

spisok = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

N = int(input("Введите номер столбца: "))

stolbec = list(map(lambda el: el[N], spisok)) # берем элементы столбика N

stolbec_sum = sum(stolbec)

stolbec_el = reduce(lambda x, y: x * y, stolbec)  # произведение

print("Сумма элементов столбца:", stolbec_sum)
print("Произведение элементов столбца:", stolbec_el)
