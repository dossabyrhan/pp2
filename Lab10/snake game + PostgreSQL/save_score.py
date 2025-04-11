import psycopg2

def save_score(user_id, score, level):
    conn = psycopg2.connect(
        host="localhost",
        dbname="labwork",
        user="postgres",
        password="2006Dos$"
    )
    cur = conn.cursor()

    cur.execute("SELECT user_id FROM user_score WHERE user_id = %s", (user_id,))
    result = cur.fetchone()

    if result:
        cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
    else:
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))

    conn.commit()
    cur.close()
    conn.close()


