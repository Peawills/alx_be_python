import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="olayemiolaa1",
    database="student_db"
)

print(mydb.get_server_info())