from dialogue import *
from class_container import *
from class_table import *
from class_statset import *

class health:

    def __init__(self):
        
        self.statSet = statset()
        self.statSet.addStat(contDice(['hit-dice','What are your hit dice']))
        self.statSet.addStat(contInt(['max-health','What is your maximum health']))
        self.statSet.addStat(contInt(['temporary-health','Do you currently have any temporary health']))
        self.statSet.addStat(contInt(['current-health','What is your current health']))
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

    def changeHealth(self):
 
        self.statSet.updateAll()
        self.refreshTable() 
