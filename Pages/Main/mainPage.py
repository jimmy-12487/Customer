import tkinter as tk

from CONFIG import *
from Pages.Page import Page

class MainPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tk.Label(self, text="Main").pack()
    

if __name__ == '__main__':
    pass