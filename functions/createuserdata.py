# functions/createuserdata.py
import sqlite3
import os

conn = sqlite3.connect("data/userdata.db") # isso daqui é simples né é o caminho da pasta
cursor = conn.cursor()

# Cria tabela se não existir (executa no import — é seguro)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user TEXT PRIMARY KEY,
    toscaneCoins INTEGER DEFAULT 0,
    goons TEXT DEFAULT 'nenhum'
)
""")
conn.commit() # É basicamente a mesma parada do github só que na database, ele vai executar e dar commit nas mudanças que executou

def ensure_user(user):
    print('buceta de velha')
    """
    Garante que o usuário exista. 
    NÃO faz nada se user for None (apenas retorna False).
    Retorna True se criou, False se já existia ou se user inválido.
    """
    if user is None:
        # não interrompe a execução — apenas retorna falso
        print("ensure_user: chamado com user=None — ignorando")
        return False

    user_key = str(user)

    cursor.execute("SELECT user FROM users WHERE user = ?", (user_key,))
    res = cursor.fetchone()

    if res is None:
        cursor.execute(
            "INSERT INTO users (user, toscaneCoins, goons) VALUES (?, ?, ?)",
            (user_key, 0, "nenhum")
        ) # isso daqui só atualiza pro usuario, é, aquilo cria o basico da database e isso cria o basico do usuario na database
        conn.commit() # e a mesma coisa
        return True

    return False
