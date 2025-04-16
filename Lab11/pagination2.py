import psycopg2

def paginate_phonebook(limit):
    offset = 0

    while True:
        conn = psycopg2.connect(
            host="localhost",
            dbname="labwork",
            user="postgres",
            password="2006Dos$"
        )
        cur = conn.cursor()

        cur.execute("SELECT * FROM get_phonebook_page(%s, %s);", (limit, offset))
        rows = cur.fetchall()

        print(f"\n📄 Page (offset={offset})")
        for row in rows:
            print(row)

        cur.close()
        conn.close()

        command = input("\n[N]ext, [P]revious, [E]xit: ").strip().lower()
        if command == 'n':
            offset += limit
        elif command == 'p' and offset >= limit:
            offset -= limit
        elif command == 'e':
            break
        else:
            print("❗ Unknown command")

if __name__ == "__main__":
    paginate_phonebook(limit=2)
