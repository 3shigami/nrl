from messages.pay_json.crypto import Crypto

def crypto_pay_text():
    btc = Crypto.get_crypto()
    return f"""Банковская карта
Сделайте перевод на кошелек:
{btc}
После совершения перевода прикрепите скриншот чека в бота"""