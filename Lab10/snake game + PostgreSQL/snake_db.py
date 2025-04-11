import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        dbname="labwork",
        user="postgres",
        password="2006Dos$"
    )

def get_user(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
        result = cur.fetchone()
        return user_id, result
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id, (0, 1)
