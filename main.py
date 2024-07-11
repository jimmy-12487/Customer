import tkinter as tk

from CONFIG import *
from Pages.Main.mainPage import MainPage
from Pages.Customer.customerPage import CustomerPage
from Pages.Order.orderPage import OrderPage
from Pages.Schedule.schedulePage import SchedulePage

class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.__setupDisplay()
        self.__setupPages()
        self.__setupButtons()
    
        self.__enableCurrentPage()
    
    def __setupDisplay(self):
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_LOCATION_X}+{WINDOW_LOCATION_Y}')
        self.resizable(width=0, height=0)
        
    def __setupPages(self):
        self.pages = {}
        self.pages['main'] = MainPage(master=self)
        self.pages['customer'] = CustomerPage(master=self)
        self.pages['schedule'] = SchedulePage(master=self)
        self.pages['order'] = OrderPage(master=self)
        
        self.currentPageName = 'main'
        
        
    def __setupButtons(self):
        self.buttonFrame = tk.Frame(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT).place(x=0, y=WINDOW_HEIGHT-MENU_BUTTON_HEIGHT)
        buttons = [tk.Button(
                        self.buttonFrame, 
                        width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, 
                        text=CODE_TO_DISPLAY_TABLE[pagename], command=lambda x=pagename: self.__changeCurrentPage(x)
                    ) for pagename in ['main', 'schedule', 'order', 'customer']]

        for i, btn in enumerate(buttons):
            btn.place(x=i*MENU_BUTTON_WIDTH, y=WINDOW_HEIGHT-MENU_BUTTON_HEIGHT,
                      width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT)
    
    def __enableCurrentPage(self):
        self.pages[self.currentPageName].place(x=WINDOW_LOCATION_X, y=WINDOW_LOCATION_Y)
    
    def __disableCurrentPage(self):
        self.pages[self.currentPageName].place_forget()
    
    def __setCurrentPageName(self, newPageName):
        self.currentPageName = newPageName        
    
    def __changeCurrentPage(self, newPageName):
        self.__disableCurrentPage()
        self.__setCurrentPageName(newPageName)
        self.__enableCurrentPage()
    
    def RunMain(self):
        try:
            self.mainloop()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main = Main()
    
    try:
        main.RunMain()
    except:
        pass