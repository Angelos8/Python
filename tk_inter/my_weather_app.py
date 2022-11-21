import tkinter as tk
import requests

#function that returns temperature
def temperture():
    API_key = 'b539e26f54d6c71ab5bd22983e6584f8'
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_key + "&unit=Metric" + "&q=" + location.get() + "&units=metric"
    weather_data = requests.get(base_url).json()['main']['temp']
    fl_value = float(weather_data)
    c_to_f(fl_value)
    lbl_print_celcius["text"] = f'{weather_data}'
    return lbl_print_celcius["text"]

def c_to_f(val:float):
    lbl_print_fahrenheit["text"] = f'{round((val + 32) *(9/5),2)} '
    return lbl_print_fahrenheit
    

#create window
window = tk.Tk()
window.title("Prototype WeatherApp")
# window.rowconfigure([0,1],weight=0,minsize=50)
# window.columnconfigure([0,1,2],weight=0,minsize=50)

frame = tk.Frame(relief=tk.SUNKEN, height = 500, width=500)
frame.pack()

location_lbl = tk.Label(master=frame, text= "Enter Location")
location_lbl.grid(row=0, column=0, sticky='n')
location = tk.Entry(master=frame, relief=tk.GROOVE, fg= "cyan", bg= "black", width= 40)
location.grid(row=0,column=0, pady=20, padx=5)

#button to get temperature
btn_get_temp  = tk.Button(master = frame, text =f"\N{RIGHTWARDS BLACK ARROW}", command=temperture)
btn_get_temp.grid(row=0, column=1,padx=10)
#celcius
lbl_celcius = tk.Label(frame, text = "Celcius (℃)")
lbl_celcius.grid(row=0, column=2, padx=10)
lbl_print_celcius = tk.Label(frame, text =f''.format(temperture))
lbl_print_celcius.grid(row=0, column=2, sticky='s')
#fahrenheit
lbl_fahrenheit = tk.Label(frame, text = "Fahrenheit (F)")
lbl_fahrenheit.grid(row=1, column=2, pady=20)
lbl_print_fahrenheit = tk.Label(frame, text =f''.format(c_to_f))
lbl_print_fahrenheit.grid(row=1, column=2, sticky='s')


window.mainloop()