from art import logo #don't need to specify extension

#const
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
TOTAL_ALPHABET_LETTERS = 26

#functions
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in ALPHABET:
            current_char_index = ALPHABET.index(char)
            encrypted_char_index = current_char_index + shift

            if encrypted_char_index > TOTAL_ALPHABET_LETTERS - 1: #[25] == 26th
                encrypted_char_index -= TOTAL_ALPHABET_LETTERS #list index starts at 0
        
            encrypted_char = ALPHABET[encrypted_char_index]
            encrypted_text += encrypted_char

        else:
            encrypted_text += char

    return encrypted_text

#maintain the same calculation from the encrypt function
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char in ALPHABET:
            current_char_index = ALPHABET.index(char)
            original_char_index = current_char_index - shift

            if original_char_index < 0:
                original_char_index += TOTAL_ALPHABET_LETTERS
        
            decrypted_char = ALPHABET[original_char_index]
            decrypted_text += decrypted_char
        
        else:
            decrypted_text += char

    return decrypted_text

#declarations && program
try_again = "Y"

print(logo)

while try_again == "Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        user_text = input("What message do you want to encrypt?\n").lower()
        user_shift = int(input("Type the shift number:\n"))
        encrypted_message = encrypt(text=user_text, shift=user_shift)
        print(f"The encrypted message is: {encrypted_message}")

    elif direction == "decode":
        user_text = input("What message do you want to decrypt?\n").lower()
        user_shift = int(input("Type the shift number:\n"))
        decrypted_message = decrypt(text=user_text, shift=user_shift)
        print(f"The decrypted message is: {decrypted_message}")
    
    else:
        print("You entered something other than 'encode' or 'decode'.")

    try_again = input("Type 'Y' if you want to go again. Otherwise type 'N': ").upper()
    print("\n")
