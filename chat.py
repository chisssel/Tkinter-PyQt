import tkinter as tk

def send():
    if entry.get():
        chat.insert(tk.END, f"Вы: {entry.get()}\n")
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Чат")

chat = tk.Text(root, height=20, width=50)
chat.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

btn_chat = tk.Button(root, text="Отправить", command=send)
btn_chat.pack(pady=5)

root.mainloop()