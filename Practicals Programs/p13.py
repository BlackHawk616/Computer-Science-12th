import pickle

def update(path):
    rollno = int(input("Enter roll number to update: "))
    found = False
    
    with open(path, 'rb') as file:
        records = []
        try:
            while True:
                record = pickle.load(file)
                if record['roll'] == rollno:
                    record['name'] = input("Enter new name: ")
                    record['marks'] = int(input("Enter new marks: "))
                    found = True
                records.append(record)
        except EOFError:
            pass
    
    if not found:
        print("Roll number not found.")
        return

    with open(path, 'wb') as file:
        for record in records:
            pickle.dump(record, file)
    
    print("Record updated successfully.")

update("student.dat")
