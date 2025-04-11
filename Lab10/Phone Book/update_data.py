import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="labwork",
    user="postgres",
    password="2006Dos$"
)
cur = conn.cursor()

name = input("Enter the name of the user you want to update: ")
new_name = input("Enter new name (press Enter to skip): ")
new_phone = input("Enter new phone (press Enter to skip): ")

if new_name:
    cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_name, name))

if new_phone:
    cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, new_name or name))

conn.commit()
cur.close()
conn.close()
print("Update complete.")
