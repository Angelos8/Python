############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.




#libraries
import art
import random
import ace_card as ace
print(art.logo)

#deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#players
#name = input("Enter your name: ")
name = "Angelos"
player = []
dealer = []
game_on = False

#function that checks sum
def sum_over_21(function):
    if function > 21:
        return True


#give cards to contestants
for index in range(2):
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))

#ace = 1 or 11
player = ace.ace_card(player)

if sum_over_21(sum(player)) == True:
    print(f'{name} your cards {player} and current score: {sum(player)} you loose!')
elif sum(player) == 21:
    print(f'{name} your cards {player} and current score: {sum(player)} you win!')
else:
    #show hands
    print(f'{name} your cards {player} and current score: {sum(player)}')
    print(f"Dealer's first card: [{dealer[0]}]")
    choice = input("Get another card: Yes or No \n").lower()

    #game
    while not game_on:
        #pass
        if choice == "no":
            #check if dealer's sum < 17:
            if sum(dealer) < 17:
                dealer.append(random.choice(cards))
            if sum_over_21(sum(dealer)) == True:
                print(f"Dealer's score is {sum(dealer)} You win!")
                game_on = True
            else:
                if sum(player) > sum(dealer):
                    print(f"Dealer's cards {dealer} and current score: {sum(dealer)}")
                    print("You win!")
                elif sum(player) < sum(dealer):
                    print(f"Dealer's cards {dealer} and current score: {sum(dealer)}")
                    print("You loose!")
                else:
                    print("It's a draw!")
                    print(f"Dealer's cards {dealer} and current score: {sum(dealer)}")
                game_on = True
         #draw another card        
        else: 
            player.append(random.choice(cards))
            dealer.append(random.choice(cards))
            print(f'{name} your cards {player} and current score: {sum(player)}')
            print(f"Dealer's first hand: [{dealer[0]}]")

            if sum_over_21(sum(player)) == True:
                print(f"your score is {sum(player)} You loose!")
                game_on = True
            elif sum_over_21(sum(dealer)) == True:
                print(f"Dealer's score is {sum(dealer)} You win!")
                game_on = True
            else:
                choice = input("Get another card: Yes or No ").lower()

