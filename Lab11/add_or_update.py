import psycopg2

def insert_or_update_user(name, phone):
    conn = psycopg2.connect(
        host="localhost",
        dbname="labwork",
        user="postgres",
        password="2006Dos$"
    )
    cur = conn.cursor()

    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ User '{name}' added or updated with phone '{phone}'")
    

# Пример вызова
if __name__ == "__main__":
    insert_or_update_user("Sayat", "87778889900")
