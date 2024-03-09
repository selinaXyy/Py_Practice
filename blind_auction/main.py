import os
from art import logo

#functions
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') #automatically detects user operating system

def create_new_bidder(name, bid):
    new_bidder = {}
    new_bidder["name"] = name
    new_bidder["bid"] = bid

    return new_bidder

def add_to_bidders_list(new_bidder, bidders_list):
    bidders_list.append(new_bidder)

def find_final_winner(bidders_list):
    highest_bid = 0
    winner_name = ""

    for bidder in bidders_list:
        if bidder["bid"] > highest_bid:
            highest_bid = bidder["bid"]
            winner_name = bidder["name"]

    return [winner_name, highest_bid]

#declarations && program
bidders_list = []

print(logo)
print("Welcome to the secret auction program.")

name = input("What is your name?: ")
bid = float(input("What's your bid?: $"))

new_bidder = create_new_bidder(name, bid)
add_to_bidders_list(new_bidder, bidders_list)

more_bidders = input("Are there any other bidders? (Y/N): ").upper()

while more_bidders == "Y":
    clear_terminal()

    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))

    new_bidder = create_new_bidder(name, bid)
    add_to_bidders_list(new_bidder, bidders_list)

    more_bidders = input("Are there any other bidders? (Y/N): ").upper()

clear_terminal()

winner = find_final_winner(bidders_list)
winner_name = winner[0]
winner_bid = "{:.2f}".format(winner[1])

print(f"The winner is {winner_name} with a bid of ${winner_bid}")