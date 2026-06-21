from customtkinter import *
from scripts.work_with_json import *
from .messages import *


FONT_FAMILY = 'San Francisco'
FONT_SIZE_TITLE = 32
FONT_SIZE = 14

TITLE = (FONT_FAMILY, FONT_SIZE_TITLE, 'bold')
TEXT = (FONT_FAMILY, FONT_SIZE, 'bold')


class RegistrationApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry('700x500')
        self.title("WiFileDrop - Регистрация")
        self.resizable(False, False)
        self.attributes('-topmost', True)


        self.title_registration_welcome = CTkLabel(self, text='Регистрация',
                                                   font=TITLE)
        self.title_registration_welcome.pack(side='top', pady=70)


        self.input_user_name = CTkEntry(self, placeholder_text='Введите ваше имя',
                                        font=TEXT,
                                        width=300)
        self.input_user_name.pack(side='top', pady=30)


        self.button_continue = CTkButton(self, text='Продолжить',
                                         font=TEXT,
                                         command=self.upload_user_name)
        self.button_continue.pack(side='top', pady=30)


    def upload_user_name(self):
        try:
            new_user_name = self.input_user_name.get()
            update_value('USER-NAME', new_user_name)
            message_success('Успешная регистрация', 'Ваши данные успешно записаны!')
        except FileNotFoundError:
            message_error('Произошла ошибка', 'Файл для записи данных поврежден, либо отсутствует')
