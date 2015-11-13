from collections import OrderedDict
from dialogue import *
from tabulate import tabulate

class basic:

    def __init__(self):
        
        self.names = OrderedDict([('race',['What is you race (e.g. elf, dwarf, human)','str']),\
                ('gender',['What is your gender','str']),\
                ('class',['What is your class (e.g. wizard, fighter)','str']),\
                ('level',['What is your level','int']),\
                ('name',['What is your name','str'])])

        self.basic = OrderedDict((key,0) for key in self.names)
        self.changeAllBasic()

    def changeAllBasic(self):
        
        self.basic = dispAskForAllDict(self.basic,self.names)

    def changeSingleBasic(self,kind):

        self.basic[kind] = dispSingleEntry('Please enter a new value for your %s: ' % (kind.upper()) ,'str')

    def getProficiency(self):
        
        level = int(self.basic['level'])

        if level < 5: return 2
        elif 4 < level < 9: return 3
        elif 8 < level < 13: return 4
        elif 12 < level < 17: return 5
        elif 16 < level < 21: return 6
 
    def getValue(self,thing):

        return self.basic[thing]
    
    def returnTable(self):

        return tabulate([ [key,value] for key,value in self.basic.iteritems()],tablefmt='grid')

    def returnListOfNames(self):

        return [ key[0] for key in self.names.iteritems() ]
    
    def returnLevel(self):

        return int(self.basic['level'])

            
        
