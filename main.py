import random
import string

def password_generator():
    password_numbers = []
    password_letters = []
    password_symbols = []
    symbols = ['~', '!', '@', '#', '$', '%', '^', '(', ')', '_', '+', '=', '[', ']',
               '{', '}', ';', "/", ',', '.', '<', '>', '|', '`']
    letter_input = int(input("How many letters do you want?"))
    number_input = int(input("How many numbers do you want?"))
    symbol_input = input("Do you want symbols?, yes/no ")
    lower_upper_alphabet = string.ascii_letters
    for letter in range(letter_input):
        random_letter = random.choice(lower_upper_alphabet)
        password_letters.append(random_letter)
    for number in range(number_input):
        random_number = random.randint(0, 9)
        password_numbers.append(random_number)
    if symbol_input == 'yes':
        number_of_symbols = int(input("How many symbols? "))
        for i in range(number_of_symbols):
            random_symbol = random.randint(0, 24)
            password_symbols.append(symbols[random_symbol])

    if symbol_input == 'no':
        pass

    password = list(password_numbers + password_letters + password_symbols)
    my_password = "".join(map(str, password))

    return ''.join(random.sample(my_password, len(my_password)))


print("Your password is: ", password_generator())
