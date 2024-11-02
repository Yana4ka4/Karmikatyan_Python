# Вариант 12. Дано двузначное число. Найти сумму и произведение его цифр.
try:
    while True:  # обработка исключений
        a = int(input("Введите двузначное число: "))
        if a > 9 and a < 100:
            des = a // 10
            ed = a % 10
            summ = des + ed
            multi = des * ed
            print("Сумма цифр числа", a, "равна", summ)
            print("Произведение цифр числа", a, "равна", multi)
            break
        else:
            print("Введите двузначное число! ")
except ValueError:
    print("Введите число!")
