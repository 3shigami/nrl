from aiogram import types

card_markup = types.InlineKeyboardMarkup(row_width=1)

card_markup.add(types.InlineKeyboardButton("✅Я ОПЛАТИЛ", callback_data="card_payd"))
card_markup.add(types.InlineKeyboardButton("❌ОТМЕНА", callback_data="unpayd"))
