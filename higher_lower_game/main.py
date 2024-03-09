import os, random
from game_data import data
from art import logo, vs

#functions
def update_rand_comparands(comparands_list, num_of_comparands):
    comparands = len(comparands_list)

    #adds comparand(s) till it reaches the requirement
    while comparands < num_of_comparands:
        rand_comparand = data[random.randint(0, len(data) - 1)]

        while rand_comparand in comparands_list:
            rand_comparand = data[random.randint(0, len(data) - 1)]
            
        comparands_list.append(rand_comparand)
        comparands += 1

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def game():
    NUM_OF_COMPARANDS = 2

    user_score = 0
    comparands_list = []
    first_game = True
    game_continues = True
    correct_answer = False
    update_rand_comparands(comparands_list, NUM_OF_COMPARANDS)
    comparand_A = comparands_list[0]
    comparand_B = comparands_list[1]

    #start game
    while game_continues:
        clear_terminal()
        print(logo)

        if not first_game:
            if correct_answer:
                user_score += 1
                print(f"You're right! Current Score: {user_score}")
                update_rand_comparands(comparands_list, NUM_OF_COMPARANDS)
                comparand_A = comparands_list[0]
                comparand_B = comparands_list[1]
            else:
                print(f"Sorry, that's wrong. Final score: {user_score}")
                return
        
        print(f"Compare A: {comparand_A['name']}, a(n) {comparand_A['description']}, from {comparand_A['country']}.")
        print(vs)
        print(f"Against B: {comparand_B['name']}, a(n) {comparand_B['description']}, from {comparand_B['country']}.")
        user_answer = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        #checks answer
        if user_answer == "A" and comparand_A['follower_count'] > comparand_B['follower_count']:
            del comparands_list[0]
            correct_answer = True
        elif user_answer == "B" and comparand_B['follower_count'] > comparand_A['follower_count']:
            del comparands_list[1]
            correct_answer = True

        if first_game:
            first_game = False

game()