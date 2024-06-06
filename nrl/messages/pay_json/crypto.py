import json

class Crypto:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_crypto():
        with open("messages/pay_json/json_files/crypto.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
        return data["btc"]
    