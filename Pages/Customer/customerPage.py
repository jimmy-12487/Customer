import tkinter as tk

from CONFIG import *
from Pages.Customer.customerUtils import *
from Pages.Page import Page

class TitleFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack()
        
class LabelFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__resetDisplay()
        self.pack()
    
    def __resetDisplay(self):
        self.displayLabels = [dict(CUSTOMERPAGE_LABELS_TEMPLATE) for _ in range(NUM_CUSTOMER_PER_PAGE)]
        self.displayButtons = [dict(CUSTOMERPAGE_BUTTONS_TEMPLATE) for _ in range(NUM_CUSTOMER_PER_PAGE)]
    
    def __clearDisplay(self):
        for displayLabel in self.displayLabels:
            for label in displayLabel.values():
                if not isinstance(label, tk.Label):
                    continue
                    
                label.grid_forget()
                label.destroy()
        
        for displayButton in self.displayButtons:
            for button in displayButton.values():
                if not isinstance(button, tk.Button):
                    continue
            
                button.grid_forget()
                button.destroy()
                
        self.__resetDisplay()
    
    def __updateData(self, customerData, pageIndex):
        for index in range(NUM_CUSTOMER_PER_PAGE):    
            customerIndex = pageIndex * NUM_CUSTOMER_PER_PAGE + index
            data = CUSTOMERPAGE_EMPTY_LABELS if customerIndex >= len(customerData) else customerData[customerIndex]
            for key in CUSTOMERPAGE_LABELS_TITLES:
                self.displayLabels[index][key] = tk.Label(self, text=data[key])
        
    def __updateDisplay(self):
        
        for index, data in enumerate(self.displayLabels):
            if any(label is None for label in data.values()):
                continue
            
            for keyIndex, label in enumerate(data.values()):
                label.grid(
                    row=index * CUSTOMERPAGE_LABELS_ROWSPAN, column=keyIndex * CUSTOMERPAGE_LABELS_COLSPAN,
                    rowspan=CUSTOMERPAGE_LABELS_ROWSPAN, columnspan=CUSTOMERPAGE_LABELS_COLSPAN
                )
    
    def UpdateFrame(self, customerData, pageIndex):
        self.__clearDisplay()
        self.__updateData(customerData, pageIndex)
        self.__updateDisplay()
        '''
        
        '''
            

            
            
class CustomerPage(Page):
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.__checkFile()
        self.__setupData()
        
        self.__setupLabelFrame()
        self.UpdatePage()
        
    def __checkFile(self):
        CheckFile()
        self.customerData = LoadFile()
    
    def __setupData(self):
        self.pageIndex = 0

    def __setupLabelFrame(self):
        self.labelFrame = LabelFrame(master=self)
        
    def UpdatePage(self):
        self.labelFrame.UpdateFrame(self.customerData, self.pageIndex)

if __name__ == '__main__':
    pass