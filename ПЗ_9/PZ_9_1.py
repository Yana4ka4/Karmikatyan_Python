# Вариант 12. Организовать словарь на 10 англо-русских слов, обеспечивающий
# "перевод" английского слова на русский.

dict = {
    "horse": "лошадь",
    "plane": "самолёт",
    "pen": "ручка",
    "dog": "собака",
    "house": "дом",
    "car": "машина",
    "sun": "солнце",
    "forest": "лес",
    "table": "стол",
    "bag": "сумка"
}

def translate(word):  #делаем функцию перевода
    return dict.get(word.lower(), "Слово отсутствует")

eng_word = input("Введите английское слово: ")
translation = translate(eng_word)
print(f"Перевод: {translation}")
