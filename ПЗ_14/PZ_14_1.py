# В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и ДД/ММ/ГГГГ.
# Посчитать количество дат в каждом формате. Поместить в новый текстовый файл все даты февраля
# в формате ДД/ММ/ГГГГ.

import re

with open('dates.txt', 'r', encoding='utf-8') as f:
    text = f.read()

dates_tochka = re.findall(r'\d{2}\.\d{2}\.\d{4}', text)    # ищем в файлике 2 типа форматов
dates_slash = re.findall(r'\d{2}/\d{2}/\d{4}', text)

print("Количество ДД.ММ.ГГГГ:", len(dates_tochka))
print("Количество ДД/ММ/ГГГГ:", len(dates_slash))

february = [d for d in dates_slash if d[3:5] == '02']  # оставляем только февральские даты с слэшем

with open('february_dates.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(february))
