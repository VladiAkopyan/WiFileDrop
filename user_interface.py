from customtkinter import *


FONT_FAMILY = 'San Francisco'
FONT_SIZE_TITLE = 32
FONT_SIZE = 14


class MyApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry('900x700')
        self.title('WiFileDrop')
        self.resizable(False, False)
        self.attributes('-topmost', True)

        CTkLabel(self, text="WiFileDrop", font=(FONT_FAMILY, FONT_SIZE_TITLE, 'bold')).grid(column=0, row=0, padx=10, pady=10)

