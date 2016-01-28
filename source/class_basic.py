from dialogue import *
from class_container import *
from class_table import *
from class_statset import *

class basic:

    def __init__(self):
        
        self.statSet = statset()
        self.statSet.addStat(contStr(['name','What is your name']))
        self.statSet.addStat(contStr(['gender','What is your gender']))
        self.statSet.addStat(contStr(['race','What is your race']))
        self.statSet.addStat(contStr(['class','What is your class']))
        self.statSet.addStat(contInt(['level','What is your level']))
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

    def changeBasic(self):
 
        self.statSet.updateAll()
        self.refreshTable()
        
    def changeName(self):

        self.statSet.updateSingleStat('name')
        self.refreshTable()
