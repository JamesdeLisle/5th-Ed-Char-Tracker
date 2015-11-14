from collections import OrderedDict
from dialogue import *
from tabulate import tabulate

class attributes:

    def __init__(self):
        
        self.names = OrderedDict([('strength',['What is you strength','int']),\
                ('dexterity',['What is your dexterity','int']),\
                ('constitution',['What is your constitution','int']),\
                ('intelligence',['What is your intelligence','int']),\
                ('wisdom',['What is you wisdom','int']),\
                ('charisma',['What is your charisma','int'])])

        self.attributes = OrderedDict((key,0) for key in self.names)
        self.changeAllAttributes()

    def changeAllAttributes(self):
        
        self.attributes = dispAskForAllDict(self.attributes,self.names)

    def changeSingleAttribute(self,kind):

        self.attributes[kind] = int(dispSingleEntry('Please enter a new value for your %s: ' % (kind.upper()) ,'int'))
        
    def getModifier(self,kind):

        return (self.attributes[kind]-10)/2 

    def returnTable(self):

        return tabulate([[key,value,self.getModifier(key)] for key,value in self.attributes.iteritems()],tablefmt='grid')

    def returnListOfNames(self):

        return [ key[0] for key in self.names.iteritems() ]
    
