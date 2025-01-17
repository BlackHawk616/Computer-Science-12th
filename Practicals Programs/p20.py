# Writing a python function to insert multiple records into the students table by connecting python with Mysql using interface with python 

import mysql.connector

def insert_students():
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="school"
    )
    cursor = conn.cursor()

    # List of student records (Roll No, Name, Marks)
    students = [
        (101, "Alice", 85),
        (102, "Bob", 78),
        (103, "Charlie", 92)
    ]

    # SQL Query to insert data
    query = "INSERT INTO students (roll_no, name, marks) VALUES (%s, %s, %s)"

    # Executing the query for multiple records
    cursor.executemany(query, students)

    # Commit changes
    conn.commit()
    
    print(f"{cursor.rowcount} records inserted successfully!")

    # Close connection
    cursor.close()
    conn.close()

# Call the function
insert_students()
