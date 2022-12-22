from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

# import csv
words_dict = {}
try:
    words_to_learn = pd.read_csv("./data/words_to_learn.csv")
    words_dict = pd.DataFrame.to_dict(words_to_learn,orient="records")
except FileNotFoundError:
    # read the german word csv file

    german_words = pd.read_csv("./data/german_words.csv")
    # convert the dataframe ta new csv file
    german_words.to_csv("./data/words_to_learn.csv", index=False)
    words_to_learn = pd.read_csv("./data/words_to_learn.csv")
    # convert to a list containing elements that are dictionaries
    words_dict = pd.DataFrame.to_dict(words_to_learn,orient="records")
random_word = random.choice(words_dict)

#--------------Random german words------
def correct():
    global random_word, flip_timer, words_dict
    # remove word from the list 
    words_dict.remove(random_word)
    df = pd.DataFrame.from_dict(words_dict)
    df.to_csv("./data/words_to_learn.csv")
    incorrect()

def incorrect():
    global random_word, flip_timer
    # cancel the timer if a button is pressed
    window.after_cancel(flip_timer)
    random_word = random.choice(words_dict)
    canvas.itemconfig(title_word, text=random_word['German'],fill="Black")
    canvas.itemconfig(language_word, text=random_word['German'],fill="Black")
    canvas.itemconfig(front_card, image=front_img)
    # reset the timer 
    flip_timer = window.after(3000,func=english_meaning)

def english_meaning():
    global random_word
    canvas.itemconfig(front_card, image=back_img)
    canvas.itemconfig(title_word,text="English", fill="White")
    canvas.itemconfig(language_word,text=random_word["English"], fill="White")
    pass





#--------------UI------------------------
# window and canvas
window = Tk()
window.title("Flash Cards")
flip_timer = window.after(3000,english_meaning)
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
canvas = Canvas(width=800,height=526, background=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
front_card = canvas.create_image(400,263,image=front_img)
title_word = canvas.create_text(400,150, text="German",fill="black",font=('Ariel',40,'italic'))
language_word = canvas.create_text(400,263,text=f"{random_word['German']}", fill="black",font=('Ariel',60,'bold'))
# buttons
wrong_img = PhotoImage(file="./images/wrong.png")
right_img = PhotoImage(file="./images/right.png")
wrong = Button(image=wrong_img, command=incorrect)

wrong.grid(row=1,column=0)
right = Button(image=right_img, command=correct)
right.grid(row=1,column=1)



window.mainloop()