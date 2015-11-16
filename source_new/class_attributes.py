from dialogue import *
from class_container import *
from class_table import *

class attributes:

    def __init__(self):
        
        self.strength = contInt(['strength','What is your strength'])
        self.dexterity = contInt(['dexterity','What is your dexterity'])
        self.constitution = contInt(['constitution','What is your constitution'])
        self.intelligence = contInt(['intelligence','What is your intelligence'])
        self.wisdom = contInt(['wisdom','What is your wisdom'])
        self.charisma = contInt(['charisma','What is your charisma'])
        self.cont = [self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma]
        map(lambda entry : dialogue(entry), self.cont)
        self.table = table(self.getTableData())

    def getTableData(self):

        source = []
        headers = ()
        for item in self.cont:
            source.append([item.returnLabel(),item.returnValue()])
        
        return source,headers

    def changeAttribute(self):
 
        self.cont = dialogue(contListCont(['all','Choose the stat you wish to change'],self.cont)).returnValue()

     
