# Write a program to save some UID and pass in csv file And ask user to enter UID and pass, if The Combination Matches mit should print "Login SuccessFull" else "Please Check Your Credentials"

import csv

def save_credentials(uid, password):
    with open('credentials.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([uid, password])

def check_credentials(uid, password):
    with open('credentials.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == uid and row[1] == password:
                return True
    return False

def main():
    while True:
        print("1. Save Credentials")
        print("2. Login")
        choice = input("Enter your choice: ")
        if choice == '1':
            uid = input("Enter UID: ")
            password = input("Enter Password: ")
            save_credentials(uid, password)
        elif choice == '2':
            uid = input("Enter UID: ")
            password = input("Enter Password: ")
            if check_credentials(uid, password):
                print("Login Succesfull")
            else:
                print("Please check your credentials")
        else:
            print("Invalid choice")

main()