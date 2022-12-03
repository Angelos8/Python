# import turtle module
import turtle as tr
import pandas as pd

# screen 
screen = tr.Screen()
screen.bgcolor('black')
screen.title("U.S. States Game")

# import image 
image = 'blank_states_img.gif'
# turn turtle into the image shape
tr.bgpic(image)

# read csv file
states_data = pd.read_csv("50_states.csv")
#print(states_data.state)
states = states_data.state.to_list()

# save all correct answers
correct_guesses = []

count = 0
score = 0
while count < 5:
    # how to use textinput https://www.geeksforgeeks.org/turtle-textinput-function-in-python/
    answer_state = str(screen.textinput(title = f"{score}/50 States Correct", prompt="What's another State? Type exit to stop")).title()

    # check if user answer is a state
    if answer_state == "Exit":
        break
    elif answer_state in correct_guesses:
        pass
    elif answer_state in states:
        score +=1
        correct_guesses.append(answer_state)
        # get coordinates of state on the map
        x = int(states_data[states_data.state == answer_state].x)
        y = int(states_data[states_data.state == answer_state].y)
        # pen up and make turtle invisible 
        tr.penup()
        tr.hideturtle()
        # move turtle to the coordinates on the map
        tr.setposition(x=x,y=y)
        # write the guessed state's name
        tr.write(answer_state)
    count +=1
# create dictionary 

dict = {}
#save the unguessed states to a csv
for guess in correct_guesses:
    states.remove(guess)

if len(states) != 0:
    dict.update({'Missed States': states})
    df = pd.DataFrame.from_dict(dict)
    df.to_csv("missed-states.csv")

print(f'guesses len: {len(correct_guesses)} and left states len: {len(states)}\n')
# exit screen
screen.bye()

