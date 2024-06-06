import json

class Get_sp:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_elements(id):
        with open("logs/data.json", "r", encoding="UTF-8") as f:
            data = json.load(f)

        return data.get(str(id))
    


