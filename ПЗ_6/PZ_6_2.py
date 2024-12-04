# Вариант 12. Дан список размера N. Найти два соседних элемента, сумма которых максимальна,
# и вывести эти элементы в порядке возрастания их индексов.

def pairSum(data):
    if len(data) < 2:
       return None

    maxSum = 0
    maxPair = None

    for i in range(len(data) - 1):
        tekushayaSum = data[i] + data[i + 1]
        if tekushayaSum > maxSum:
            maxSum = tekushayaSum
            maxPair = (data[i], data[i + 1])
    return maxPair
import random

N = input("Введите размер списка N: ")
while type(N) != int:  # обработка исключений
    try:
        N = int(N)
    except ValueError:
        N = input("Введите размер списка N: ")

a = [random.randint(1, 100) for i in range(N)]  # список рандомных чисел
print("Сгенерированный список:", a)

result = pairSum(a)
if result:
    print("Пара с макс. суммой:", result)
else:
    print("Список слишком короткий")

