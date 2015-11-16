from collections import OrderedDict
from dialogue import *
from tabulate import tabulate

class journal:

    def __init__(self):

        self.types = OrderedDict([('title',['What would you like to title this page','str']),\
                ('note',['Type your entry','str'])])
        self.pages = []

    def addPage(self):

        self.pages.append(dispAskForAllDict({ key:'' for key,value in self.types},self.types))
    
class page:

    def __init__(self):


