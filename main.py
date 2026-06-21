from user_interface.program import *
from user_interface.registration import *
import json

def user_name_find():
    with open('./datas/user.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['USER-NAME']

if __name__ == '__main__':
    if user_name_find() == '':
        app = RegistrationApp()
        app.mainloop()
    else:
        app = MyApp()
        app.mainloop()