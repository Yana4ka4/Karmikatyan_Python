# Вариант 12. Дана строка-предложение на русском языке. Вывести самое короткое
# слово в предложении. Если таких слов несколько, то вывести последнее из них.
# Словом считать набор символов, не содержащий пробелов, знаков препинания и
# ограниченный пробелами, знаками препинания или началом/концом строки.

s = input("Введите текст: ")
lst = s.split()
minimum = s
for el in lst:
    if len(el) < len(minimum):
        minimum = el
print(f"Слово: {minimum} ")
