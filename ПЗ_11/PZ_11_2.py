# Вариант 12. Из предложенного текстового файла (text18-12.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно вставив после каждой строки строку из символов «*».

f = open("text18-12.txt", "r", encoding="utf-8")
text = f.read()
f.close()

print("Содержимое файла:")
print(text)

count = text.count(' ')
print("Количество пробелов:", count)


lines = text.split('\n')     # новый файл
f = open("stars.txt", "w", encoding="utf-8")
for line in lines:
    f.write(line + "\n")
    f.write("**********\n")
f.close()
