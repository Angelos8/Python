import random
from check_string import check_string
from hangman_art import logo, stages
from hangman_words import word_list
from check_string import check_string

chosen_word = random.choice(word_list)

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')


end_of_game = False
lives = 6
empty_spaces = 0
display = []
guess_string = ''

for i in range(len(chosen_word)):
  display.append('_')
  empty_spaces += 1
  

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if check_string(guess,guess_string) == True:
        print("Letter already used")
    else:
        guess_string += guess
        found = False
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
                empty_spaces -= 1
                found = True
        if found == False:
            lives -=1
            print(stages[lives])
        
    if empty_spaces == 0 and lives > 0:
        print("You win!")
        print(f'empty spaces = {empty_spaces}')
        end_of_game = True
    elif lives == 0 and empty_spaces > 0:
        print("You loose!")
        print(f'word: {chosen_word}')
        end_of_game = True
    print(display)
    print(f'Guessed letters: {guess_string}\n')
