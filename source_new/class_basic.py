from dialogue import *
from class_container import *
from class_table import *

class basic:

    def __init__(self):
        
        self.name = contStr(['name','What is your name'])
        self.gender = contStr(['gender','What is your gender'])
        self.race = contStr(['race','What is your race'])
        self.clas = contStr(['class','What is your class'])
        self.level = contInt(['level','What is your level'])
        self.cont = [self.name,self.gender,self.race,self.clas,self.level]
        map(lambda entry : dialogue(entry), self.cont)
        self.table = table(self.getTableData())
    
    def getTableData(self):

        source = []
        headers = []
        for item in self.cont:
            source.append(item.returnValue())
            headers.append(item.returnLabel())
        
        return source,headers
  
    def changeBasic(self):
 
        self.cont = dialogue(contListCont(['all','Choose the stat you wish to change'],self.cont)).returnValue()

