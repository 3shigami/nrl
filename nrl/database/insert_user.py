import sqlite3

connection = sqlite3.connect("database/database.db")

cursor = connection.cursor()
class User_insert:
    def __init__(self, id):
        self.id = id
        self.balance = 0
        self.buys = 0

    @classmethod
    def create(cls, id):
        # Проверка существования пользователя в базе данных
        cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
        row = cursor.fetchone()

        if row:
            return False
        else:
            # Создание нового пользователя
            cursor.execute("INSERT INTO users (id, balance, buys) VALUES (?, ?, ?)", (id, 0, 0))
            connection.commit()


            # Возврат созданного пользователя
            return User_insert(id)
