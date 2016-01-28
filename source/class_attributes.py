from dialogue import *
from class_container import *
from class_table import *
from class_statset import *

class attributes:

    def __init__(self):

        self.statSet = statset()
        self.statSet.addStat(contInt(['strength','What is your strength']))
        self.statSet.addStat(contInt(['dexterity','What is your dexterity']))
        self.statSet.addStat(contInt(['constitution','What is your constitution']))
        self.statSet.addStat(contInt(['intelligence','What is your intelligence']))
        self.statSet.addStat(contInt(['wisdom','What is your wisdom']))
        self.statSet.addStat(contInt(['charisma','What is your charisma']))
        self.table = table(self.getTableData())
    
    def getTableData(self):

        source = []
        headers = []
        for item in self.statSet.returnList():
            source.append(item.returnValue())
            headers.append(item.returnLabel())
        
        return source,headers
    
    def refreshTable(self):
        
        self.table = table(self.getTableData())

    def changeAttribute(self):
 
        self.statSet.updateAll()
        self.refreshTable() 
         
