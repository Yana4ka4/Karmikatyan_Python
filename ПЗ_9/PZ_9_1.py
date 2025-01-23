dict = {
    "apple": "яблоко",
    "book": "книга",
    "cat": "кот",
    "dog": "собака",
    "house": "дом",
    "car": "машина",
    "sun": "солнце",
    "moon": "луна",
    "water": "вода",
    "tree": "дерево"
}

def translate(word):   #перевод
    return dict.get(word.lower(), "Слово отсутствует")

eng_word = input("Введите английское слово: ")
translation = translate(eng_word)
print(f"Перевод: {translation}")
