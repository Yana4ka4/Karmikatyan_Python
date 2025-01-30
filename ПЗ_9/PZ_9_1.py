# Вариант 12. Организовать словарь на 10 англо-русских слов, обеспечивающий
# "перевод" английского слова на русский.

slovar = {"horse": "лошадь", "airplane": "самолёт", "pen": "ручка", "green": "зелёный", "house": "дом",
        "car": "машина", "eye": "глаз", "forest": "лес", "table": "стол", "bag": "сумка"}

def perevodik(word):  #делаем функцию перевода
    return slovar.get(word.lower(), "Слово отсутствует")

eng_word = input("Введите английское слово: ")
perevod = perevodik(eng_word)
print(f"Перевод: {perevod}")
