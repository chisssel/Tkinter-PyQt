import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(
        title="Выберите файл"
    )
    if file_path:
        label_result.config(text=f"Выбран файл: {file_path}")

root = tk.Tk()
root.title("Диалог выбора файла")
root.geometry("800x400")

btn_open = tk.Button(root, text="Выбрать файл", command=open_file)
btn_open.pack(pady=20)

label_result = tk.Label(root, text="Файл не выбран")
label_result.pack()

root.mainloop()