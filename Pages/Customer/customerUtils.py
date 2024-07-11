import os
import json

CUSTOMER_FILE_PATH = './Pages/Customer/customerFile.json'

CUSTOMERPAGE_LABELS_TITLES = ['name', 'phone']  
CUSTOMERPAGE_LABELS_TEMPLATE = {
    key: None for key in CUSTOMERPAGE_LABELS_TITLES
}
CUSTOMERPAGE_EMPTY_LABELS = {
    key: 'EMPTY' for key in CUSTOMERPAGE_LABELS_TITLES
}
CUSTOMERPAGE_LABELS_ROWSPAN = 1
CUSTOMERPAGE_LABELS_COLSPAN = 2

CUSTOMERPAGE_BUTTONS_TEMPLATE = {
    'delete': None,
    'modify': None
}

CUSTOMERPAGE_BUTTONS_ROWSPAN = 1
CUSTOMERPAGE_BUTTONS_COLSPAN = 1

NUM_CUSTOMER_PER_PAGE = 5


def CheckFile():
    if not os.path.exists(CUSTOMER_FILE_PATH):
        template = [{
            'name': '',
            'phone': '',
        }]
        with open(CUSTOMER_FILE_PATH, 'w') as f:
            json.dump(template, f)

def LoadFile():
    try:
        with open(CUSTOMER_FILE_PATH, 'r') as f:
            return json.load(f)
    except:
        return None