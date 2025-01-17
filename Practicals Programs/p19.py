# Writing A Python Function to read csv file and dsiplay the row as a list of dictionaries

import csv

def read_csv_file(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Reads the file as a dictionary
        data = list(reader)  # Convert to a list of dictionaries
    
    # Display the list of dictionaries
    for row in data:
        print(row)

# Example usage
read_csv_file("students.csv")


