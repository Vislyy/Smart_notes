import json

def write_in_file(data):
    with open("notes_data/notes_info.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def read_from_file():
    try:
        with open("notes_data/notes_info.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except:
        return {}