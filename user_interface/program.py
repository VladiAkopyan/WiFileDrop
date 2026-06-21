from customtkinter import *
import json


FONT_FAMILY = 'San Francisco'
FONT_SIZE_TITLE = 32
FONT_SIZE = 14
FONT_COLOR_ERROR = '#E74C3C'
FONT_COLOR_WARNING = '#F39C12'
FONT_COLOR_SUCCESS = '#2ECC71'
SYSTEM_THEME = 'Dark'


class MyApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry('900x700')
        self.title('WiFileDrop')
        self.resizable(False, False)
        self.attributes('-topmost', True)
        set_appearance_mode(SYSTEM_THEME)



