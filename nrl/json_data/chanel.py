import json

class Chanel:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_chanel():
        with open("json_data/json_files/chanel.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
        return data["chanel"]
    