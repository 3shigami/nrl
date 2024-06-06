import sqlite3

class Balance:
    def __init__(self, id):
        self.id = id

    def add_to_balance(self, amount):
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()

        cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, self.id))
        connection.commit()
        connection.close()


    def get_balance(id):
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()

        cursor.execute("SELECT balance FROM users WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None