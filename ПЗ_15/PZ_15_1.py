# Приложение ТЕЛЕМАСТЕРСКАЯ для автоматизированного контроля работ по
# ремонту бытовой техники. БД должна содержать таблицу Ремонт телевизоров,
# имеющую следующую структуру записи: Марка телевизора, Завод-изготовитель, Цена,
# Дата ремонта, Документ, Мастер, Сумма оплаты.

from data import data
import sqlite3 as sq

with sq.connect('tv_workshop.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS tv_data")
    cur.execute("""CREATE TABLE IF NOT EXISTS tv_data(
        brand TEXT NOT NULL,
        manufacturer TEXT NOT NULL,
        price INTEGER NOT NULL,
        repair_date TEXT NOT NULL,
        document TEXT NOT NULL,
        master TEXT NOT NULL,
        payment INTEGER NOT NULL
    )""")
    cur.executemany("INSERT INTO tv_data VALUES(?, ?, ?, ?, ?, ?, ?)", data) # заполняем таблицу данными

    print("\nРемонты, выполненные Ивановым:")
    cur.execute("SELECT * FROM tv_data WHERE master = 'Иванов'")
    for row in cur.fetchall():
        print(row)

    print("\nРемонты от 12.05.2025:")
    cur.execute("SELECT * FROM tv_data WHERE repair_date = '12.05.2025'")
    for row in cur.fetchall():
        print(row)

    cur.execute("DELETE FROM tv_data WHERE brand = 'Haier Smart'")
    print("\nУдалён ремонт Haier Smart")

    cur.execute("UPDATE tv_data SET payment = 13000 WHERE brand = 'Samsung QLED'")
    print("\nОбновлена сумма оплаты для Samsung QLED")

    cur.execute("UPDATE tv_data SET master = 'Козлов' WHERE master = 'Петрова'")
    print("\nПетрова заменена на Козлова")

    print("\nТаблица после изменений:")
    for row in cur.execute("SELECT * FROM tv_data"):
        print(row)

