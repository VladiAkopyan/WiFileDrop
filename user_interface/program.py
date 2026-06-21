from customtkinter import *
from scripts.work_with_json import *


FONT_FAMILY = 'San Francisco'
FONT_SIZE_TITLE = 32
FONT_SIZE = 14

TITLE = (FONT_FAMILY, FONT_SIZE_TITLE, 'bold')
TEXT = (FONT_FAMILY, FONT_SIZE, 'bold')

FONT_COLOR_ERROR = '#E74C3C'
FONT_COLOR_WARNING = '#F39C12'
FONT_COLOR_SUCCESS = '#2ECC71'
SYSTEM_THEME = 'Dark'
USER_NAME = find_value('USER-NAME')


class MyApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry('900x700')
        self.title('WiFileDrop')
        self.resizable(False, False)
        self.attributes('-topmost', True)
        set_appearance_mode(SYSTEM_THEME)

        self.title_welcome_text = CTkLabel(self, text=f'Добро пожаловать, {USER_NAME}!',
                                           font=TITLE)
        self.title_welcome_text.grid(column=0, row=0, padx=30, pady=30)

