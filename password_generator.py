#Password Generator Project
import random

#declaration
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#unpacking is typically done with iterable objects such as lists, not individual integer
ctr_for_letters = ctr_for_symbols = ctr_for_numbers = ctr_for_password = 0 
final_password = ""

#get user input
print("Welcome to the Password Generator!")

num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))

#calculation
total_num_of_password = num_of_letters + num_of_symbols + num_of_numbers

while ctr_for_password < total_num_of_password:
    rand_sequence = random.randint(0, 2)

    if rand_sequence == 0 and ctr_for_letters < num_of_letters:
        final_password += random.choice(letters)
        ctr_for_letters += 1
        ctr_for_password += 1

    if rand_sequence == 1 and ctr_for_symbols < num_of_symbols:
        final_password += random.choice(symbols)
        ctr_for_symbols += 1
        ctr_for_password += 1

    if rand_sequence == 2 and ctr_for_numbers < num_of_numbers:
        final_password += random.choice(numbers)
        ctr_for_numbers += 1
        ctr_for_password += 1

#output
print("Here is your password: " + final_password)