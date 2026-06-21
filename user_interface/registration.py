from customtkinter import *
import json


FONT_FAMILY = 'San Francisco'
FONT_SIZE_TITLE = 32
FONT_SIZE = 14


class RegistrationApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry('700x500')
        self.title("WiFileDrop - Регистрация")
        self.resizable(False, False)
        self.attributes('-topmost', True)


        self.title_registration_welcome = CTkLabel(self, text='Регистрация',
                                                   font=(FONT_FAMILY, FONT_SIZE_TITLE, 'bold'))
        self.title_registration_welcome.pack(side='top', pady=20)


        self.input_user_name = CTkEntry(self, placeholder_text='Введите ваше имя',
                                        font=(FONT_FAMILY, FONT_SIZE, 'bold'),
                                        width=300)
        self.input_user_name.pack(side='top', pady=30)


        self.button_continue = CTkButton(self, text='Продолжить')