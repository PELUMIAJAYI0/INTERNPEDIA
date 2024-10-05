#password generator
import random
import string
import pyperclip

def generate_password(length, uppercase = True, lowercase = True, digits = True, special_char = True):
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits
    
    if special_char:
        characters += string.punctuation
    
    # Ensure that the password contains at least one character from each of the character sets

    if not characters:
        print("Error: Invalid, at least one character type must be selected")
        return None
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password

while True:
    print("---------------------------------------")
    print("...Welcome to The Password Generator...")
    print("---------------------------------------")
    user_name = input("Enter your name---> ").title()
    print(" ")
    print(f"{user_name}, you can customise your password by including what should be in your password")
    print(" ")

    password_length = int(input(f"{user_name}, please enter the length of the password---> "))

    password_uppercase = input(f"{user_name}, should we include uppercase letters? (yes/no)---> ").lower() == "yes"

    password_lowercase = input(f"{user_name}, should we include lowercase letters? (yes/no)---> ").lower() == "yes"

    password_digits = input(f"{user_name}, should we  include digits? (yes/no)---> ").lower() == "yes"

    password_special_characters = input(f"{user_name}, should we include special characters? (yes/no)---> ").lower() == "yes"

    generated_password = generate_password(
        length = password_length,
        uppercase = password_uppercase,
        lowercase= password_lowercase,
        digits= password_digits,
        special_char= password_special_characters)

    if generated_password:
        print("-----------------------------------------------------------------")
        print(f"{user_name}, your Generated Password is---> {generated_password}")
        print("-----------------------------------------------------------------")

        copy = input(f"{user_name}, do you want to copy the generated password (yes/no)---> ").lower()
        if copy == "yes":
            pyperclip.copy(generated_password)
            print("-----------------------------------------------------------------")
            print(f"{user_name}, your password has been copied to the clipboard.")
            print("-----------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------")
            print(f"{user_name}, your password has not been copied to the clipboard.")
            print("-----------------------------------------------------------------")
    else:
        print("Error generating password")

    cont = input("Do you want to continue with our password generator (yes/no)---> ").lower()
    if cont != "yes":
        print("-------------------------------------------")
        print(f"{user_name}, is exiting the password generator. \nThank you for using us, Have a nice day :) ")
        print("-------------------------------------------")
        break
    else:
        continue


