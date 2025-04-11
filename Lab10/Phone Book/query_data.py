import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="labwork",
    user="postgres",
    password="2006Dos$"
)
cur = conn.cursor()

choice = input("Search by (1) name or (2) phone? ")

if choice == "1":
    name = input("Enter name: ")
    cur.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
elif choice == "2":
    phone = input("Enter phone: ")
    cur.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
else:
    print("Invalid choice")
    exit()

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
