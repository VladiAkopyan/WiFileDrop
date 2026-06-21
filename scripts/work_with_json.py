import json

def find_value(key):
    with open('./datas/user.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data.get(key, None)


def update_value(key, new_value):
    with open('./datas/user.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    data[key] = new_value

    with open('./datas/user.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)