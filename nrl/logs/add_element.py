import json


class Add_to:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_element(id, element):
        with open("logs/data.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
        sp = data.get(str(id))
        if sp == None:
            sp = []
            sp.append(element)
        else:
            sp.append(element)
        data[str(id)] = sp
        with open("logs/data.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
