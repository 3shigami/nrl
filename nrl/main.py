from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile, Message, ContentType
from messages.profile import message_text
from markup.start_markup import start_markup
from database.insert_user import User_insert
from json_data.rule import RuleReader
from json_data.operator import Operator
from json_data.chanel import Chanel
from messages.pay import pay_txt
from markup.pay_markup import pay_markup
from markup.card import card_markup
from messages.card_pay_text import card_pay_text
from markup.crypto import crypto_markup
from messages.crypto_pay_text import crypto_pay_text
from scripts.download_order import PhotoDownloader
from json_data.sity import SityReader
from json_data.stocks import StocksReader
from database.uptade_balance import Balance
from logs.add_element import Add_to
from logs.get_elements import Get_sp
from logs.add_to_data import Add_user

def check_int(n):
    try:
        f = int(n)
        return True
    except:
        return False

API_TOKEN = '6797564906:AAHlTmkQT15l7scH7O1FpyYbdSa6DSilByA'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
payok = dict()
user_shop = dict()
user_stocks = dict()
payy = dict()
balance1 = dict()
buy = dict()
user_buy = dict()

buttons = ["👤Профиль", "📋Правила", "👨‍💻Оператор", "✅Отзывы", "💵Пополнить баланс", "💳Карта", "💎Криптовалюта", "🛒Заказать", "🏡Вернутся в главное меню"]


@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(message: types.Message):
    
    User_insert.create(message.chat.id)
    Add_user.add_user(message.chat.id)
    photo = InputFile("pics/first_pic.jpg")

    await message.answer_photo(caption=""""Добро пожаловать в AK-47 SHOP!
 
  Платим нашим курьерам по 2000 Р/г 

🚀 Работай с нами на топовых условиях! 🚀
Рассматриваем внесение ,в качестве залога для работы курьером, Ваш товар.

Мы делаем упор на свежесть и качество адресов! Большой выбор моментальных кладов во всех городах Абхазии! Ежедневная работа курьеров и большой спрос не дает стоять пустым витринам и подолгу лежать кладам на своих местах!
Требуются курьеры в города:
СУХУМ🔥🔥🔥
ГАГРА🔥🔥🔥
ГАДАУТА
ПИЦУНДА
ОЧАМЧИРА
НОВЫЙ АФОН""", photo=photo, reply_markup=start_markup)



@dp.message_handler() #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   if message.chat.type == 'private':
        if message.text == '👤Профиль':
           await message.answer(message_text(message.chat.id))
        elif message.text == '📋Правила':
           await message.answer(RuleReader.get_rule())

        elif message.text == '👨‍💻Оператор':
            await message.answer(Operator.get_operator())

        elif message.text == '✅Отзывы':
            await message.answer(Chanel.get_chanel())

        elif message.text == '💵Пополнить баланс':
            await message.answer(pay_txt(), reply_markup=pay_markup)

        elif message.text == '💳Карта':
            await message.answer(card_pay_text(), reply_markup=card_markup)

        elif message.text == '💎Криптовалюта':
            await message.answer(crypto_pay_text(), reply_markup=card_markup)

        elif message.text == '🛒Заказать':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            f = SityReader.get_sity()
            for i in f:
                markup.add(f.get(i))

            markup.add("🏡Вернутся в главное меню")

            await message.answer("Пожалуйста выберете ваш город", reply_markup=markup)

            user_shop[message.chat.id] = True


        if message.text == '🏡Вернутся в главное меню':
            photo = InputFile("pics/first_pic.jpf")

            await message.answer_photo(caption="kello", photo=photo, reply_markup=start_markup)


        elif message.text not in buttons and user_shop.get(message.chat.id):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            f = StocksReader.get_stocks(message.text)
            spis = Get_sp.get_elements(id=message.chat.id)
            for i in f:
                if i in spis:
                    pass
                else:
                    markup.add(types.KeyboardButton(i))


            buy[message.chat.id] = {
                "sity": message.text,
                "socks": "None"
            }
            markup.add("🏡Вернутся в главное меню")

            await message.answer("Пожалуйста выберете интересующий вас товар", reply_markup=markup)
            user_shop[message.chat.id] = False
            user_stocks[message.chat.id] = True

        

        elif message.text not in buttons and user_stocks.get(message.chat.id) and message.text != '🏡Вернутся в главное меню' and not(check_int(message.text)):
            

            sp = buy.get(message.chat.id)

            sp["socks"] = message.text

            buy[message.chat.id] = sp


            await message.answer("⚡️⚡️⚡️", reply_markup=start_markup)

            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("✅Оплатить", callback_data='pay_shop'))
            markup.add(types.InlineKeyboardButton("🏡Вернутся в меню", callback_data='back'))
            await message.answer("При оплате товара вы берете всю отвественность на себя и все такое хз че тут писать", reply_markup=markup)


        elif message.text not in buttons and payy.get(message.chat.id).get('ms'):
            m_d = payy[message.chat.id]
            m_d["ms"] = False
            payy[message.chat.id] = m_d
            balance1[message.chat.id] = int(message.text)
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(types.InlineKeyboardButton("Зачислить", callback_data="yes"))
            markup.add(types.InlineKeyboardButton("Изменить сумму", callback_data="change"))
            await message.answer(f"Вы уверены что хотите зачислить этому пользователю {message.text} RUB", reply_markup=markup)


      



@dp.callback_query_handler()
async def check_button(call: types.CallbackQuery):

    if call.data == 'unpayd':
        photo = InputFile("pics/first_pic.png")
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await call.message.answer_photo(caption="kello", photo=photo, reply_markup=start_markup)
        payok[call.message.chat.id] = False

    elif call.data == 'crypto_payd':
        await call.message.answer("Пожалуйста пришлите чек об оплате в бота, после этого наш оператор проверит ваш чек и деньги будут начислены на ваш баланс")
        payok[call.message.chat.id] = True

    elif call.data == 'card_payd':
        await call.message.answer("Пожалуйста пришлите чек об оплате в бота, после этого наш оператор проверит ваш чек и деньги будут начислены на ваш баланс")
        payok[call.message.chat.id] = True


    elif call.data == 'pay_shop':
        ss = buy.get(call.message.chat.id)
        if ss != None:
            if Balance.get_balance(call.message.chat.id) >= int(ss.get("socks").split(":")[2]):
                await call.message.delete()
                await call.message.answer("Просим прощения, произошла ошибка, за дальшеней информаций просим обратится к оператору, для получения решиня для проблемы", reply_markup=start_markup)








                Add_to.add_element(id=call.message.chat.id, element=ss.get("socks"))

                user = Balance(call.message.chat.id)

                user.add_to_balance(-1 * int(ss.get("socks").split(":")[2]))



            else:
                await call.message.delete()
                await call.message.answer("Покупка отмененная❌, на вашем балансе недостаточно средтсв.\n Пожалуйста пополните баланс")
                await call.message.answer(pay_txt(), reply_markup=pay_markup)
            




    elif "unpay_" in call.data:
        await call.message.delete()
        await call.message.answer("Принято")
        id_user = call.data.replace("unpay_", "")
        
        await bot.send_message(chat_id=id_user, text="извините, но администрация бота не одобрила ваш чек пополнения, если у вас остались вопросы, то обратитесь пожалйста к оператору")


    elif "pay_" in call.data:
        id_user = call.data.replace("pay_", "")
        await call.message.delete()
        await call.message.answer("введите сумму пополнения в RUB")
        payy[call.message.chat.id] = {
            "ms": True,
            "id": id_user
        }

    

    

    elif call.data == 'change':
        await call.message.edit_text("Пожалуйста введите новую сумму пополнения")
        m_d = payy[call.message.chat.id]
        m_d["ms"] = True
        payy[call.message.chat.id] = m_d

    elif call.data == 'yes':
        print(balance1.get(call.message.chat.id))
        await call.message.edit_text("Деньги зачислены на баланс")
        user = Balance(payy.get(call.message.chat.id).get("id"))
        user.add_to_balance(balance1.get(call.message.chat.id))
        await bot.send_message(chat_id=payy.get(call.message.chat.id).get("id"), text=f"На ваш счет успешно зачислено {balance1.get(call.message.chat.id)}")

    



        
@dp.message_handler(content_types=ContentType.PHOTO)
async def handle_photo(message: Message):
    if payok.get(message.chat.id):
        photo_id = message.photo[-1].file_id
        await PhotoDownloader.download_photo(file_path=await bot.download_file_by_id(photo_id), id=message.chat.id)
        await message.answer("Ваш чек успешно получен, ожидайте подтверждения от оператора", reply_markup=start_markup)
        payok[message.chat.id] = False

        for i in [6921452909]:
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(types.InlineKeyboardButton("Оплачено", callback_data=f"pay_{message.chat.id}"))
            markup.add(types.InlineKeyboardButton("Не оплачено", callback_data=f"unpay_{message.chat.id}"))
            await bot.send_photo(caption="Поступила новая заявка на пополнение", photo=InputFile(f"orders/{message.chat.id}.jpg"), chat_id=i, reply_markup=markup)

        

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
