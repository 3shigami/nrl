import json

class Operator:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_operator():
        with open("json_data/json_files/operator.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
        return data["operator"]
    