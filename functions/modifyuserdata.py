import sqlite3
from functions.getuserdata import get_balance

c = sqlite3.connect('data/userdata.db')
cursor = c.cursor()

def add_balance(user, amount):

    atual = get_balance(user)

    # Se não existir → começa com zero
    if atual is None:
        atual = 0

    novo = atual + amount

    print(f"[DEBUG] usuario: {user} | atual: {atual} | add: {amount} | novo: {novo}")

    cursor.execute(
        "UPDATE users SET toscaneCoins = ? WHERE user = ?",
        (novo, user)
    )
    c.commit()

    print("[DATABASE] saldo atualizado com sucesso")
