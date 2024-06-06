from aiogram import types

pay_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

pay_markup.add(types.KeyboardButton("💳Карта"))
pay_markup.add(types.KeyboardButton("💎Криптовалюта"))
