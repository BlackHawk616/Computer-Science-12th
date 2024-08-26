# Writing a program to input a character and check whether it is Alphabet, Numeric or Any Special Character

def check(char):

    if char.isalpha():
        print("Its An Alphabet")
    elif char.isdigit():
        print("Its A Number")
    else:
        print("Its A Special Character")
    
c = input("Enter The Character :- ")

check(c)