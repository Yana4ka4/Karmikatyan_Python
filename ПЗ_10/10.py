# Вариант 12. В магазинах имеются следующие товары. Магнит – молоко, соль, сахар, печенье, сыр.
# Пятерочка – мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар, печенье. Лента
# – печенье, молоко, сыр, сметана.
# Определить:
# 1. в каких магазинах нельзя приобрести сметану.
# 2. какие товары из магазина Магнит отсутствуют в магазине Перекресток.
# 3. какие товары из магазина Лента отсутствуют в магазине Магнит.

magnit = {"молоко", "соль", "сахар", "печенье", "сыр"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар", "печенье"}
lenta = {"печенье", "молоко", "сыр", "сметана"}

if "сметана" not in magnit:
    print("В Магните нет сметаны")
if "сметана" not in pyaterochka:
    print("В Пятерочке нет сметаны")
if "сметана" not in perekrestok:
    print("В Перекрестке нет сметаны")
if "сметана" not in lenta:
    print("В Ленте нет сметаны")


print(f"В Магните есть, а в Перекрестке нет: {magnit - perekrestok}")
print(f"В Ленте есть, а в Магните нет: {lenta - magnit}")
