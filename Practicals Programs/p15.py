#  Writing a program to create a csv file
import csv

def create_csv(filename):
    data = [
        {'Name': 'Sri Ram', 'Age': 28, 'City': 'New York'},
        {'Name': 'White Wolf', 'Age': 32, 'City': 'Los Angeles'},
        {'Name': 'Black HAwk', 'Age': 22, 'City': 'Chicago'}]
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'City'])
        writer.writeheader()
        writer.writerows(data)
    print(f"{filename} created successfully.")
create_csv('people.csv')
def read_csv(filename):
    # Reading data from the CSV file
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

read_csv('people.csv')
