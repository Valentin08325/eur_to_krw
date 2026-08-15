import tkinter as tk
from tkinter import ttk

def convert():
   result = entryInt.get()
   Eur = float(result * 1639.32)
   final =  output_string.set(f"{Eur} KRW")
   return final

window = tk.Tk()
window.title("GUI")
window.geometry("400x200")

title_label = ttk.Label(master = window, text = "EUR to KRW", font="Calibri 20 bold")
title_label.pack(pady = 5)

input_frame = ttk.Frame(master = window)
entryInt= tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt)
button = ttk.Button(master = input_frame, text = "Button", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 15)

output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "output", font="Calibri 15 bold", textvariable = output_string)
output_label.pack(pady = 5)

window.mainloop()