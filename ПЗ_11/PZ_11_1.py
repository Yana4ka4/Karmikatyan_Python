# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность
# из целых положительных и отрицательных чисел. Сформировать текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов
# Максимальный элемент
# Среднее арифметическое элементов первой трети

import random
l = [" ".join([str(int(random.randint(-100, 100))) for i in range(10)])]
f3 = open('data.txt', 'w')
f3.writelines(l)
f3.close()

f4 = open('data2.txt', 'w', encoding="utf-8")  # дубликат списка
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()

f3 = open('data.txt')  # разбиваем строку и значения преобразуем в числа
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

f3 = open('data.txt')

f4 = open('data2.txt', 'a', encoding="utf-8")
f4.write('\n')
f4.write(f'Количество элементов: {len(k)}\n')
f4.write(f'Максимальный элемент: {max(k)}\n')

f4.write(f"Среднее арифметическое элементов первой трети: {sum(k[:len(k)//3]) / (len(k)//3)}\n")
f4.close()