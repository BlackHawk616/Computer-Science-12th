# Write a Program to read records from binary file student.dat

import pickle

def read(path):
    with open(path, "rb") as f:
                
                student = pickle.load(f)
                print(student)

read("Text Files/student.dat")