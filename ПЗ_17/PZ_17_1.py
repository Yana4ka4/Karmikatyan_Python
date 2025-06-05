# Вариант 10

import tkinter as tk
from tkinter import ttk, messagebox

def send_message():
    name = name_entry.get()
    email = email_entry.get()
    message = message_text.get("1.0", tk.END).strip()
    subject = subject_combobox.get()

    if not name or not email or not message:
        messagebox.showwarning("Предупреждение", "Пожалуйста, заполните все поля.")
    else:
        messagebox.showinfo("Успешно", "Сообщение успешно отправлено!")


# окно
root = tk.Tk()
root.title("Contact Form")
root.geometry("400x450")
root.configure(bg="#D3D3D3")

# контейнер
frame = tk.Frame(root, bg="#D3D3D3", padx=20, pady=20)
frame.pack(expand=True, fill='both')

# шапочка
title = tk.Label(frame, text="Contact Form", font=("Helvetica", 18, "bold"), bg="#D3D3D3", anchor="w")
title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))

subtitle = tk.Label(frame, text="Please fill all entries.", font=("Helvetica", 10), bg="#D3D3D3", anchor="w")
subtitle.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 10))

# линия
line = tk.Frame(frame, bg="black", height=1, width=300)
line.grid(row=2, column=0, columnspan=2, sticky="we", pady=5)

# метки и поля ввода
tk.Label(frame, text="Name :", bg="#D3D3D3", anchor="e", width=10).grid(row=3, column=0, sticky="e", pady=5, padx=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=3, column=1, sticky="w")

tk.Label(frame, text="Email :", bg="#D3D3D3", anchor="e", width=10).grid(row=4, column=0, sticky="e", pady=5, padx=5)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=4, column=1, sticky="w")

tk.Label(frame, text="Message :", bg="#D3D3D3", anchor="ne", width=10).grid(row=5, column=0, sticky="ne", pady=5, padx=5)
message_text = tk.Text(frame, width=30, height=5)
message_text.grid(row=5, column=1, sticky="w")

# выпадающий список
tk.Label(frame, text="Subject :", bg="#D3D3D3", anchor="e", width=10).grid(row=6, column=0, sticky="e", pady=5, padx=5)
subject_combobox = ttk.Combobox(frame, values=["Product Inquiry", "Support", "Feedback", "Other"], width=28)
subject_combobox.set("Product Inquiry")
subject_combobox.grid(row=6, column=1, sticky="w")

# отправка
send_btn = tk.Button(frame, text="Send", width=10, bg="#4F4F4F", fg="white", font=("Helvetica", 10, "bold"), command=send_message)
send_btn.grid(row=7, column=0, columnspan=2, pady=20)

root.mainloop()
