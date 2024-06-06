import json

class StocksReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_stocks(sity):
        with open("json_data/json_files/stocks.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
        return data["stocks"][sity]
    