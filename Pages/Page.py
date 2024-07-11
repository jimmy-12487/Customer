import tkinter as tk

from CONFIG import *

class Page(tk.Frame):
    '''
        This is an abstract class for all pages
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def PreviousPage(self):
        pass

    def NextPage(self):
        pass
    
if __name__ == '__main__':
    pass