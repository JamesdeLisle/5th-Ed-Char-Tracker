from collections import OrderedDict
from dialogue import *
from tabulate import tabulate

class skills:

    def __init__(self):

        self.associations = {'acrobatics':'dexterity','animal-handling':'wisdom','arcana':'intelligence','athletics':'strength','deception':'charisma',\
            'history':'intelligence','insight':'wisdom','intimidation':'charisma','investigation':'intelligence','medicine':'wisdom',\
            'nature':'intelligence','perception':'wisdom','performance':'charisma','persuasion':'charisma','religion':'intelligence',\
            'sleight-of-hand':'dexterity','stealth':'dexterity','survival':'wisdom'}

        self.proficiencies = OrderedDict((key,False) for key in self.associations)
        self.proficiencies = dispMultipleListExisting('Select or deselect your skill proficiencies: ',self.proficiencies)
        self.skills = OrderedDict((key,0) for key in self.associations)
        
    def calculateSkills(self,basic,attributes):
        
        for key,value in self.proficiencies.iteritems():
            if value:
                self.skills[key] = basic.getProficiency() + attributes.getModifier(self.associations[key])
            else:
                self.skills[key] = attributes.getModifier(self.associations[key])
    
    def returnTable(self):

        return tabulate([[key,value] for key,value in self.skills.iteritems()],tablefmt='grid')

    def changeProficiencies(self):

        self.proficiencies = dispMultipleListExisting('Select or deselect your skill proficiencies: ',self.proficiencies)


    
