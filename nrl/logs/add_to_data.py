import json


class Add_user:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_user(id):
        with open("logs/data.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

        data[str(id)] = []
        with open("logs/data.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
