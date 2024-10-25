try:
    while True:  # обработка исключений
        a = int(input("Введите двузначное число: "))
        if a > 9 and a < 100:
            a = str(a)
            summ = int(a[0]) + int(a[1])
            multi = int(a[0]) * int(a[1])
            print("Сумма цифр числа", a, "равна", summ)
            print("Произведение цифр  числа", a, "равна", multi)
            break
        else:
            print("Введите двузначное число! ")
except ValueError:
    print("Введите число!")