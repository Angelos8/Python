from distutils import command
import tkinter as tk
import random


def dice_roll():
    lbl_result["text"] = str(random.randint(1, 6))


window = tk.Tk()

window.rowconfigure([0,1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)


btn_roll = tk.Button(text="Roll", command= dice_roll) 
btn_roll.grid(row=0,column=0, sticky="nsew")

lbl_result = tk.Label()
lbl_result.grid(row=1, column=0)

window.mainloop()