from database.profile_info import User

def message_text(id):
    user = User.get(id)
    msg = f"""Ваш профиль
➖➖➖➖➖➖➖➖➖➖➖➖➖
🆔Ваш ID: {id}
🛍Количество покупок: {user.buys}
💰Ваш баланс: {user.balance} RUB
➖➖➖➖➖➖➖➖➖➖➖➖➖
💸Персональная скидка: 0%"""
    
    return msg
