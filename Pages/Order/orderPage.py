import tkinter as tk

from CONFIG import *
from Pages.Page import Page

class OrderPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tk.Label(self, text="Order").pack()
    

if __name__ == '__main__':
    pass