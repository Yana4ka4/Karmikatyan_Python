# Найти факториал произвольного целого числа.

import tkinter as tk
from tkinter import messagebox

def fact():
    try:
        n = int(entry.get())
        if n < 0:
            raise ValueError
        f = 1
        for i in range(2, n + 1):
            f *= i
        result["text"] = f"Факториал: {f}"
    except:
        messagebox.showerror("Ошибка", "Введите неотрицательное целое число!")

root = tk.Tk()
root.title("Факториал")
root.geometry("250x150")

tk.Label(root, text="Число:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Вычислить", command=fact).pack(pady=5)
result = tk.Label(root, text="")
result.pack()

root.mainloop()
