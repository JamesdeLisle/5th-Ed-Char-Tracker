class container(object):

    def __init__(self,info):
        self.label = info[0]
        self.statement = info[1]
   
    def returnType(self): 
        return self.type
    
    def returnLabel(self):
        return self.label

    def returnStatement(self):
        return self.statement

    def returnValue(self):
        return self.value

    def setValue(self,value):
        self.value = value 

class contInt(container):

    def __init__(self,info):
        container.__init__(self,info)
        self.type = 'int'
        self.value = 0

class contIntRng(container):

    def __init__(self,info,range):
        container.__init__(self,info)
        self.type = 'intr'
        self.range = range
        self.value = 0

class contIntVal(container):

    def __init__(self,info,allowed):
        container.__init__(self,info)
        self.type = 'intv'
        self.allowed = allowed
        self.value = 0

class contDice(container):

    def __init__(self,info):
        container.__init__(self,info)
        self.type = 'die'
        self.dice_num = 0
        self.dice_type = 0
        self.value = ''

class contStr(container):

    def __init__(self,info):
        container.__init__(self,info)
        self.type = 'str'
        self.value = ''

class contLst(container):

    def __init__(self,info,list):
        container.__init__(self,info)
        self.type = 'lst'
        self.list = list
        self.value = ''

class contMlist(container):

    def __init__(self,info,list):
        container.__init__(self,info)
        self.type = 'mlst'
        self.list = list
        self.value = []

class contListCont(container):

    def __init__(self,info,list):
        container.__init__(self,info)
        self.type = 'lstc'
        self.list = list
        self.value = []

    def returnList(self):
        return self.list



