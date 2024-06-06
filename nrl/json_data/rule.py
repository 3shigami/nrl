import json

class RuleReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_rule():
        with open("json_data/json_files/rule.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
        return data["rule"]
    