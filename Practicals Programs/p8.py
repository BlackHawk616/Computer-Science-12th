# Writing a python program ti generate number between 1 to 6 and check whether the user won the lottery or not 
import random

def lottery():

    user = int(input("Enter The Number Between 1 to 6 : "))

    while user >= 1 and user <= 6:

        l = random.randint(1,6)

        if user == l:
            print("You Won The Lottery")
            break

        else:
            print("Sorry You Lost The Lottery")
            print("The Lucky Number was ", l)
            break

lottery()