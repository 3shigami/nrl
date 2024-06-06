from messages.pay_json.card import Card

def card_pay_text():
    card = Card.get_card()
    return f"""Банковская карта
Сделайте перевод на карту:
{card}
После совершения перевода прикрепите скриншот чека в бота"""