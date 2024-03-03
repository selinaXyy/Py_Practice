import random
import hangman_art
import hangman_words

#declaration
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
correct_letters_ctr = 0
user_lives_ctr = 6
stages = hangman_art.stages
logo = hangman_art.logo #from hangman_art import logo, stages
display = []
displayed_letters = ""
#initialize display list
for letter in chosen_word:
    display.append("_")

#display logo
print(logo)

while correct_letters_ctr < len(chosen_word) and user_lives_ctr > 0:
    guessed_correct_letter = False

    #get user input
    guessed_letter = input("Guess a letter: ").lower()
    print(f"Test: {chosen_word}")

    if guessed_letter in display:
        print(f"You've already guessed {guessed_letter}")
    else:
        for index in range(0, len(chosen_word)):
            if chosen_word[index] == guessed_letter:
                display[index] = guessed_letter
                correct_letters_ctr += 1
                guessed_correct_letter = True
    
        if not guessed_correct_letter:
            #inform user
            print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
            user_lives_ctr -= 1

    #joins all the elements in the list & turns it into a string
    print(f"{' '.join(display)}") #" " serves as seperators
    print(stages[user_lives_ctr])

if not user_lives_ctr == 0:
    print("You won! Congrats!!!")
else:
    print(stages[user_lives_ctr])
    print("You lose.")
    print(f"The correct word is: {chosen_word}")