import json

def user_name_find():
    with open('./datas/user.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['USER-NAME']

def user_name_send(data):
    with open('./datas/user.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)