# Вариант 12. Составить функцию, которая выполнит суммирования числового ряда.

def sum(n):
  total = 0
  for i in range(n):
    number = int(input("Введите число: "))
    total += number
  return total

while True:   # обработка исключений
  try:
    n = int(input("Введите количество чисел: "))
    total = sum(n)
    print(f"Сумма: {total}")
    break
  except ValueError:
    print('Неправильный ввод')