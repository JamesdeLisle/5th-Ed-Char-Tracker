from collections import OrderedDict
from dialogue import *
from tabulate import tabulate
import copy

class health:

    def __init__(self):
        
        self.names = OrderedDict([('hit-dice',['What are your hit dice','die']),\
                ('max-health',['What is your maximum health','int']),\
                ('temporary-health',['Do you currently have any temporary health','int']),\
                ('current-health',['What is you current health','int'])])

        self.health = OrderedDict((key,0) for key in self.names)
        self.changeAllHealth()

    def changeAllHealth(self):
        
        self.basic = dispAskForAllDict(self.health,self.names)

    def changeSingleBasic(self,kind):

        self.basic[kind] = dispSingleEntry('Please enter a new value for your %s: ' % (kind.upper()) ,'string')
        
    def getProficiency(self):
        
        level = int(self.basic['level'])

        if level < 5: return 2
        elif 4 < level < 9: return 3
        elif 8 < level < 13: return 4
        elif 12 < level < 17: return 5
        elif 16 < level < 21: return 6

    def returnTable(self):
        
        out = copy.deepcopy(self.health)
        out['hit-dice'] = out['hit-dice'][2]
        return tabulate([[key,value] for key,value in out.iteritems()],tablefmt='grid')
 

