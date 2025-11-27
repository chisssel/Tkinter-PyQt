import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def plot_graph():
    x = np.linspace(0, 10)
    y = x ** 2

    fig = Figure()
    plot = fig.add_subplot()
    plot.plot(x, y)
    plot.set_title("График y = x^2")

    canvas = FigureCanvasTkAgg(fig)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("График в Tkinter")
root.geometry("800x500")

btn_plot = tk.Button(root, text="Построить график", command=plot_graph)
btn_plot.pack(pady=10)

root.mainloop()