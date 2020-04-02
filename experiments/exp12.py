import mysql.connector

from faker import Faker
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="faker",
  passwd="faker",
  database="mydatabase"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE student (roll_no INT,name VARCHAR(255),attendance INT,marks INT)")

for i in range(5):
    x = (random.randint(1,100),Faker().name(),random.randint(100,300),random.randint(20,100))
    data = "INSERT INTO student VALUES(%s,%s,%s,%s)"
    mycursor.execute(data,x)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT * FROM student")

data = mycursor.fetchall()

for i in data:
    print(i)

mycursor.execute("UPDATE student SET name = 'Naruto Uzumaki' WHERE roll_no = 1")

mycursor.execute("SELECT * FROM student")

data = mycursor.fetchall()
for i in data:
    print(i)

mycursor.execute("DELETE FROM student WHERE roll_no = 15")

mycursor.execute("SELECT * FROM student")

data = mycursor.fetchall()
print()
for i in data:
    print(i)