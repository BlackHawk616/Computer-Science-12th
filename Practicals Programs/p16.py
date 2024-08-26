# Write a program to count no of records from csv fileimport csv
import csv

def count_records(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        count = sum(1 for row in reader)
    return count

filename = 'people.csv'
print(count_records(filename))