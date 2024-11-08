while True: # обработка исключений
    try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        C = int(input("Введите число C: "))

        if A > 0 and B > 0 and C > 0:
            print("Высказывание истинно")
            break
        else:
            print("Высказывание ложно")
    except ValueError:
        print("Введите число!")
