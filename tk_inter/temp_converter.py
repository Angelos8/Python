
import tkinter as tk

#convert F to C
def f_to_c():
    fahrenheit = float(ent_temp.get())
    lbl_result["text"] = f'{(fahrenheit - 32) *(5/9)} ℃'
#window
window = tk.Tk()
window.title("Temperature Converter")
#frame
frame = tk.Frame(relief=tk.SUNKEN,width=200,height=100)
frame.pack()
#entry fahrenheit temp and label
ent_temp = tk.Entry(master = frame, fg = "crimson", bg = "black",width = 15)
ent_temp.grid(row=0,column=0)
# fahrenheit = ent_temp.get() #variable saves input


input_temp_label = tk.Label(master = frame, text=f"\N{DEGREE FAHRENHEIT}")
input_temp_label.grid(row=0, column=0,sticky='e')

btn_converter = tk.Button(master = frame, text =f"\N{RIGHTWARDS BLACK ARROW}", command = f_to_c)
btn_converter.grid(row=0, column=1,padx=10)

lbl_result = tk.Label(master=frame)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()