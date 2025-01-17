# writing a python programm to delete a record from student table based  on Roll no connecting python with Mysql using mysql.connector 

import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="school"
)

cursor = conn.cursor()

# Get Roll Number from User
roll_no = input("Enter Roll Number to delete: ")

# SQL Query to delete record
query = "DELETE FROM students WHERE roll_no = %s"
cursor.execute(query, (roll_no,))

# Commit the transaction
conn.commit()

# Check if record was deleted
if cursor.rowcount > 0:
    print(f"Record with Roll No {roll_no} deleted successfully!")
else:
    print("No record found with that Roll Number.")

# Close connection
cursor.close()
conn.close()
