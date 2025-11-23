import sqlite3

conn = sqlite3.connect("data/userdata.db")
cursor = conn.cursor()

def get_balance(user):
    cursor.execute("SELECT toscaneCoins FROM users WHERE user = ?", (user,))
    res = cursor.fetchone()
    if res is None:
        return 0
    return res[0]