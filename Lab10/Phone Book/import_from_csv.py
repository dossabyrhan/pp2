import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    dbname="labwork",
    user="postgres",
    password="2006Dos$"
)
cur = conn.cursor()

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", row)

conn.commit()
cur.close()
conn.close()
