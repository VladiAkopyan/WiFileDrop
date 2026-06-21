from customtkinter import *
import json

def user_name_find():
    with open('./datas/user.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['USER-NAME']


FONT_FAMILY = 'San Francisco'
FONT_SIZE_TITLE = 32
FONT_SIZE = 14
FONT_COLOR_ERROR = '#E74C3C'
FONT_COLOR_WARNING = '#F39C12'
FONT_COLOR_SUCCESS = '#2ECC71'
SYSTEM_THEME = 'Dark'
USER_NAME = user_name_find()


class MyApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry('900x700')
        self.title('WiFileDrop')
        self.resizable(False, False)
        self.attributes('-topmost', True)
        set_appearance_mode(SYSTEM_THEME)

        self.title_welcome_text = CTkLabel(self, text=f'Добро пожаловать, {USER_NAME}!',
                                           font=(FONT_FAMILY, FONT_SIZE_TITLE, 'bold'))
        self.title_welcome_text.grid(column=0, row=0, padx=30, pady=30)

