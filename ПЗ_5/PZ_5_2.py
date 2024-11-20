# Вариант 12. Описать функцию SortDec3(A, B, C), меняющую содержимое переменных A, B, C таким образом, чтобы их значения оказались упорядоченными по убыванию (A, B,C — вещественные параметры,
# являющиеся одновременно входными и выходными). С помощью этой функции упорядочить по убыванию два данных набора из трех чисел: (A1, B1, C1) и (A2, B2, C2).

def SortDec3(A, B, C):
  if A < B:
    A, B = B, A
  elif A < C:
    A, C = C, A
  elif B < C:
    B, C = C, B
  return A, B, C

while True:   # обработка исключений
  try:
    A1 = float(input("Введите значение A1: "))   # первый набор
    B1 = float(input("Введите значение B1: "))
    C1 = float(input("Введите значение C1: "))


    A2 = float(input("Введите значение A2: "))  # второй набор
    B2 = float(input("Введите значение B2: "))
    C2 = float(input("Введите значение C2: "))

    A1, B1, C1 = SortDec3(A1, B1, C1)    # делаем наборы по убыванию
    A2, B2, C2 = SortDec3(A2, B2, C2)

    print(f"Набор 1: A1 = {A1}, B1 = {B1}, C1 = {C1}")
    print(f"Набор 2: A2 = {A2}, B2 = {B2}, C2 = {C2}")
    break
  except ValueError:
    print('Неправильный ввод')