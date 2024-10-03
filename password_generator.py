#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
tot=nr_letters+nr_numbers+nr_symbols
letcount, numcount, symcount =0,0,0
while tot>0:
    rando=random.randint(1,3)
    if rando==1 and letcount<nr_letters:
        random_letter = random.randint(0,len(letters)-1)
        print(letters[random_letter],end="")
        letcount+=1
        tot-=1
    if rando==2 and symcount<nr_symbols:
        random_symbol = random.randint(0,len(symbols)-1)
        print(symbols[random_symbol],end="")
        symcount+=1
        tot-=1
    if rando==3 and numcount<nr_numbers:
        random_number = random.randint(0,len(numbers)-1)
        print(numbers[random_number],end="")
        numcount+=1
        tot-=1
