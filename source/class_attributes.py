from collections import OrderedDict
from dialogue import *

class attributes:

    def __init__(self):
        
        self.names = ['strength','dexterity','constitution','intelligence','wisdom','charisma']
        self.attributes = OrderedDict((key,0) for key in self.names)
        self.changeAllAttributes()

    def changeAllAttributes(self):
        
        self.attributes = dispAskForAllDictInteger(self.attributes)

    def changeSingleAttribute(self,kind):

        self.attributes[kind] = dispSingleEntry('Please enter a new value for your %s: ' % (kind.upper()) ,'integer')
        
    def getModifier(self,kind):

        return (self.attributes[kind]-10)/2 

    
