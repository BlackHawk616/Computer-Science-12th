# Write a program too insert n record in a binary file student.dat

import pickle
def record(path):
    f = open(path, "wb")
    n = int(input("Enter the number of records: "))
    for i in range(n):

        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))
        marks = int(input("Enter marks: "))
        student = {"name": name, "roll": roll, "marks": marks}
        pickle.dump(student, f)


record("Text Files/student.dat")
