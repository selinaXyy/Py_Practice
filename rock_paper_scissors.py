import random

#declaration
user_choice = ""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
pattern_list = [rock, paper, scissors]

#get user input
user_choice = int(input("What do you choose? \nRock(0), Paper(1), Scissors(2):\n"))

if user_choice == 0 or user_choice == 1 or user_choice == 2:
    #calculation & output
    user_pattern = pattern_list[user_choice]
    print(user_pattern)

    #generates computer choice
    rand_num = random.randint(0,2)
    computer_pattern = pattern_list[rand_num]
    print(f"Computer chose:\n{computer_pattern}")

    #prints game result
    if user_pattern == computer_pattern:
        print("It's a tie!")
    elif user_pattern == pattern_list[0]:
        if computer_pattern == pattern_list[1]:
            print("You lose.")
        else:
            print("You won!!!")
    elif user_pattern == pattern_list[1]:
        if computer_pattern == pattern_list[0]:
            print("You won!!!")
        else:
            print("You lose.")
    else:
        if computer_pattern == pattern_list[0]:
            print("You lose.")
        else:
            print("You won!!!")
else:
    print("You entered something other than 0, 1, or 2.")
#end if

user_choice = input("Play again? (Y/N): ").upper()
while user_choice == "Y":
    #get user input
    user_choice = int(input("What do you choose? \nRock(0), Paper(1), Scissors(2):\n"))

    if user_choice == 0 or user_choice == 1 or user_choice == 2:
        #calculation & output
        user_pattern = pattern_list[user_choice]
        print(user_pattern)

        #generates computer choice
        rand_num = random.randint(0,2)
        computer_pattern = pattern_list[rand_num]
        print(f"Computer chose:\n{computer_pattern}")

        #prints game result
        if user_pattern == computer_pattern:
            print("It's a tie!")
        elif user_pattern == pattern_list[0]:
            if computer_pattern == pattern_list[1]:
                print("You lose.")
            else:
                print("You won!!!")
        elif user_pattern == pattern_list[1]:
            if computer_pattern == pattern_list[0]:
                print("You won!!!")
            else:
                print("You lose.")
        else:
            if computer_pattern == pattern_list[0]:
                print("You lose.")
            else:
                print("You won!!!")
    else:
        print("You entered something other than 0, 1, or 2.")
    #end if

    user_choice = input("Play again? (Y/N): ").upper()
