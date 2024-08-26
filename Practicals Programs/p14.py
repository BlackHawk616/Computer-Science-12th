#  Write a program to delete a data from student.dat

import pickle

def delete_record(path):
    rollno = int(input("Enter roll number to delete: "))
    found = False

    with open(path, 'rb') as file:
        records = []
        try:
            while True:
                record = pickle.load(file)
                if record['roll'] != rollno:
                    records.append(record)
                else:
                    found = True
        except EOFError:
            pass  # End of file reached

    with open(path, 'wb') as file:
        for record in records:
            pickle.dump(record, file)

    if found:
        print("Record deleted successfully.")
    else:
        print("Roll number not found.")

delete_record("student.dat")
