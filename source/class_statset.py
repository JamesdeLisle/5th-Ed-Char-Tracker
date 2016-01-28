from class_container import *
from dialogue import *

class statset:

    def __init__(self):

        self.list_of_stats = []

    def addStat(self,stat):

        self.list_of_stats.append(dialogue(stat))

    def returnList(self):

        return self.list_of_stats

    def updateList(self,input_list):

        self.list_of_stats = input_list

    def updateSingleStat(self,name):

        for idx,entry in enumerate(self.list_of_stats):
            if entry.label == name:
                self.list_of_stats[idx] = dialogue(self.list_of_stats[idx])
    
    def updateAll(self):

        self.list_of_stats = dialogue(contListCont(['all','Choose the stat you wish to change'],self.cont)).returnValue()

    def setSingleStat(self,name,value):

        for idx,entry in enumerate(self.list_of_stats):
            if entry.label == name:
                self.list_of_stats[idx].setValue(value)
