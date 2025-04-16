import psycopg2

def search_phonebook(pattern):
    conn = psycopg2.connect(
        host="localhost",
        dbname="labwork",
        user="postgres",
        password="2006Dos$"
    )
    cur = conn.cursor()

    query = """
        SELECT * FROM PhoneBook
        WHERE name ILIKE %s OR phone ILIKE %s;
    """
    param = f"%{pattern}%"
    cur.execute(query, (param, param))
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    conn.close()

if __name__ == "__main__":
    search_phonebook("Dan")
