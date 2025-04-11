import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="labwork",
    user="postgres",
    password="2006Dos$"
)
cur = conn.cursor()

choice = input("Delete by (1) name or (2) phone? ")

if choice == "1":
    name = input("Enter name: ")
    cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
elif choice == "2":
    phone = input("Enter phone: ")
    cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
else:
    print("Invalid choice")
    exit()

conn.commit()
cur.close()
conn.close()
print("Deleted successfully.")
