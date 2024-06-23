import json

class Card:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_card():
        with open("messages/pay_json/json_files/card.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
        return data["card"]
    
    def change_card(card):
        with open("messages/pay_json/json_files/card.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

        data["card"] = card
        with open("logs/data.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
