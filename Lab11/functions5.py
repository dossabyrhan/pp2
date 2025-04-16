import psycopg2

def delete_user(identifier):
    conn = psycopg2.connect(
        host="localhost",
        dbname="labwork",
        user="postgres",
        password="2006Dos$"
    )
    cur = conn.cursor()

    try:
        cur.execute("CALL delete_user(%s);", (identifier,))
        conn.commit()
        print(f"✅ User with name or phone '{identifier}' deleted.")
    except Exception as e:
        print("❌ Error:", e)
    finally:
        cur.close()
        conn.close()

# Для теста:
if __name__ == "__main__":
    delete_user("Sayat")  # Замени на имя или номер, который хочешь удалить
