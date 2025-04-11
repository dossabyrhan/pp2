import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="labwork",
    user="postgres",  
    password="2006Dos$"  
)
cur = conn.cursor()

name = input("Enter name: ")
phone = input("Enter phone number: ")

cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))

conn.commit()
cur.close()
conn.close()
print("Data inserted successfully!")
