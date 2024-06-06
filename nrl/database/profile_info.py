import sqlite3

connection = sqlite3.connect("database/database.db")

cursor = connection.cursor()

class User:
    def __init__(self, id, balance, buys):
        self.id = id
        self.balance = balance
        self.buys = buys

    @classmethod
    def get(cls, id):
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        row = cursor.fetchone()

        if row:
            return User(*row)
        else:
            return None
        