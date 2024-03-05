import os
import random
from art import logo

FIRST_TIME_CARD_COUNT = 2
SUBSEQUENT_CARD_COUNT = 1

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)

    return random_card

def add_new_card(card_list, num_of_times):
    for n in range(0, num_of_times):
        random_card = get_random_card()
        card_list.append(random_card)
    
    #if Ace exists in the card list & current score is over 21
    if 11 in card_list and sum(card_list) > 21:
        ace_card_index = card_list.index(11)
        card_list[ace_card_index] = 1

#program && declarations
user_cards = []
dealer_cards = []
user_score = 0
dealer_score = 0
game_continues = False
user_response = "y"

user_response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if user_response == "y":
    game_continues = True
    clear_terminal()
else:
    print("Bye.")

while game_continues:
    #reset records
    user_cards = []
    dealer_cards = []
    user_score = 0
    dealer_score = 0

    print(logo)

    #add cards to user_cards && dealer_cards
    add_new_card(user_cards, FIRST_TIME_CARD_COUNT)
    add_new_card(dealer_cards, FIRST_TIME_CARD_COUNT)
    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)

    if user_score < 21:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        user_response = input("Type 'y' to get another card, type 'n' to pass: ")
    elif user_score == 21:
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print("Congratulations! You got Blackjack on your first draw. 🎉🎉🎉\nYou won!!! 😁")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        game_continues = False

    while user_response == "y" and game_continues:
        add_new_card(user_cards, SUBSEQUENT_CARD_COUNT)
        user_score = sum(user_cards)
        
        if user_score < 21:
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Dealer's first card: {dealer_cards[0]}")
            user_response = input("Type 'y' to get another card, type 'n' to pass: ")
        elif user_score == 21:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print("Blackjack! You win!!! 😃")
            print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
            game_continues = False
        else:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print("You went over. You lose 😭")
            print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
            game_continues = False

    #if user typed 'n'
    while game_continues:
        if dealer_score == 21:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
            print("Lose, dealer has Blackjack 😱")
            game_continues = False

        elif dealer_score >= 17 and dealer_score < 21:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
            
            if user_score == dealer_score:
                print("It's a tie.")
            elif user_score > dealer_score:
                print("You win 😁")
            else:
                print("You lose 😭")
                
            game_continues = False

        elif dealer_score < 17:
            add_new_card(dealer_cards, SUBSEQUENT_CARD_COUNT)
            dealer_score = sum(dealer_cards)        

        else:
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
            print("Dealer went over. You win! 😁")
            game_continues = False

    user_response = input("Do you want to start a new game? Type 'y' or 'n': ")
    if user_response == "y":
        game_continues = True
        clear_terminal()
    
        
        
