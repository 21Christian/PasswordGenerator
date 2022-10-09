import random
import string

def password_generator():
    
    # creating the empty lists to append the nubers letters and symbols
    password_numbers = []
    password_letters = []
    password_symbols = []
    
    # list of symbols
    symbols = ['~', '!', '@', '#', '$', '%', '^', '(', ')', '_', '+', '=', '[', ']',
               '{', '}', ';', "/", ',', '.', '<', '>', '|', '`']
    
    # user input
    letter_input = int(input("How many letters do you want?"))
    number_input = int(input("How many numbers do you want?"))
    symbol_input = input("Do you want symbols?, yes/no ")
    
    # generating the upper and lower case letters 
    lower_upper_alphabet = string.ascii_letters
    
    # filling the lists according to user input 
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
    # if the user does not want symbols we simply pass 
    if symbol_input == 'no':
        pass
    
    # creating a list made out of the other lists we created 
    password = list(password_numbers + password_letters + password_symbols)
    
    # creating a string out of the new list 
    my_password = "".join(map(str, password))
       
    # randomly shuffling the created list 
    return ''.join(random.sample(my_password, len(my_password)))


print("Your password is: ", password_generator())
