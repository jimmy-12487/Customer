import tkinter as tk

from CONFIG import *
from Pages.Page import Page

class SchedulePage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tk.Label(self, text="Schedule").pack()
    

if __name__ == '__main__':
    pass