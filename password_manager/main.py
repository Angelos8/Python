from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [chr(letter) for letter in range(65,123) if letter >96 or letter<91]
    numbers = [str(num) for num in range(0,10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # range for each list
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # create lists containing letters, symbols and numbers
    random_letters = [random.choice(letters) for i in range(nr_letters)]
    random_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for i in range(nr_numbers)]
    # merge lists and shuffle
    random_letters += random_numbers + random_symbols
    random.shuffle(random_letters)
    # create password string
    password = "".join(random_letters)
    password_input.insert(0,password)
    #print(password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # read inputs
    website = website_input.get()
    email_username = email_input.get()
    password = password_input.get() 
    # create a dictionary for the input values
    input_data = {
        # website will be a key to an inner dictionary
        website:{
            "email":email_username,
            "password":password
        }
    }
    # pop up message
    if len(website) !=0 and len(password) !=0 and email_username !=0:
        confirm = messagebox.askokcancel(title=website, message=f"You entered:\n"
                                        f"Email: {email_username}\npassword: {password}\n Are these details correct?")
        if confirm == True:
            # open data.json to read from IF IT EXISTS
            try:
                with open("data.json",mode="r") as data_file:
                    read_data = json.load(data_file)
            except FileNotFoundError:
                # if file does not exist then it will create one
                with open("data.json", mode="w") as data_file:
                    # save data in file
                    json.dump(input_data,data_file, indent=4)
            else:
                # read_data object gets the input_data added
                read_data.update(input_data)
                # now save the updated data to the json file
                with open("data.json", mode="w") as data_file:
                    # save data in file
                    json.dump(read_data,data_file, indent=4)

            website_input.delete(0,END)
            password_input.delete(0,END)
    else:
        messagebox.showerror(title= "Missing details!",message="Website and password cannot be empty!")

# ---------------------------- SEARCH PASSOWRD ------------------------------- #

def search_password():
    website = website_input.get()
    # look up website in the json file
    try:
        with open("data.json", "r") as data_file:
            # load data from file
            read_data = json.load(data_file)
            try:
            #if website in read_data.keys():
                messagebox.showinfo(title=website, message= f'email:        {read_data[website]["email"]}\npassword: {read_data[website]["password"]}')
            except:
                messagebox.showinfo(message=f"No details for {website} exist")
    except FileNotFoundError:
        messagebox.showerror(message="No Data File Found")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
# canvas
canvas = Canvas(height=200,width=200,background="black")
canvas.grid(row=0,column=1)
img = PhotoImage(file="logo.png")
# create_image(position_x, position_y, image= image_var)
canvas.create_image(100,100,image=img)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username = Label(text="Email/Username:")
email_username.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries
website_input = Entry(width=32)
website_input.grid(row=1,column=1,columnspan=2, sticky=W)
email_input = Entry(width=52)
email_input.grid(row=2,column=1, columnspan=2, sticky=W)
password_input = Entry(width=32)
password_input.grid(row=3,column=1, sticky=W)
# start with the cursor in the website entry
website_input.focus()
# buttons
generate_password = Button(text="Generate Password", command= generate_password)
generate_password.grid(row=3,column=2, sticky=W)
search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1,column=2,sticky=W)
add = Button(text="Add", width=44, command=save)
add.grid(row=5,column=1,columnspan=2, sticky=W)


window.mainloop()

