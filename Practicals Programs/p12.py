#  Write a program to Implement a searcg operation in a binary file that is to seach studnet details in student.dat
import pickle
def search(path):
    with open(path, "rb") as f:

        r = int(input("Enter The Roll No: "))
        a = pickle.load(f)
        if a["roll"] == r:
            print("Name :- ", a["name"])
            print("Roll No :- ", a["roll"])
            print("marks :- ", a["marks"])

        elif a["roll"] != r:
            print("Roll Number Not Found In Database")

search("Text Files/student.dat")