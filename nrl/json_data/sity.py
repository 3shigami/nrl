import json

class SityReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_sity():
        with open("json_data/json_files/stocks.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
        return data["sity"]
    

print(SityReader.get_sity())