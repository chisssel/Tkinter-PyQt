import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress_bar.config(value = 0)
    for i in range(100):
        progress_bar.config(value = i)
        root.update_idletasks()
        time.sleep(0.025)

root = tk.Tk()
root.title("Прогрессбар")

progress_bar = ttk.Progressbar(root, length=300)
progress_bar.pack(pady=20)

btn_start = tk.Button(root, text="Запуск", command=start_progress)
btn_start.pack(pady=10)

root.mainloop()