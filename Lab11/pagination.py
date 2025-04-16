import psycopg2

def paginate_phonebook(limit, offset):
    conn = psycopg2.connect(
        host="localhost",
        dbname="labwork",
        user="postgres",
        password="2006Dos$"
    )
    cur = conn.cursor()

    # вызываем функцию из PostgreSQL
    cur.execute("SELECT * FROM get_phonebook_page(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

if __name__ == "__main__":
    # Пример: выводим первые 3 записи (LIMIT 3 OFFSET 0)
    paginate_phonebook(3, 0)
