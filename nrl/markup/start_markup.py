from aiogram import types

start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

start_markup.add(types.KeyboardButton("🛒Заказать"), types.KeyboardButton("👤Профиль"))
start_markup.add(types.KeyboardButton("📋Правила"), types.KeyboardButton("👨‍💻Оператор"))
start_markup.add(types.KeyboardButton("💵Пополнить баланс"), types.KeyboardButton("✅Отзывы"))