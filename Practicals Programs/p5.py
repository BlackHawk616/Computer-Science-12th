# Writing a python program to check whether the number is prime or not
def prime(num):
    if num % 2 == 0:
        print("It is a prime number")
    else:
        print("Its not a prime number")
s =  int(input("Enter The Number You Want To Check"))
prime(s)