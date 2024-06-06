from aiogram import types

crypto_markup = types.InlineKeyboardMarkup(row_width=1)

crypto_markup.add(types.InlineKeyboardButton("✅Я ОПЛАТИЛ", callback_data="crypto_payd"))
crypto_markup.add(types.InlineKeyboardButton("❌ОТМЕНА", callback_data="unpayd"))
