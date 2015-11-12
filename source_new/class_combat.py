from collections import OrderedDict
from dialogue import *
from tabulate import tabulate


class combat:

    def __init__(self,inventory,basic,attributes):
        
        self.combat = {}
        armor,shield = inventory.equipped.getAC() 

        if armor == 0:
            self.combat['ac'] = 10 + shield + attributes.getModifier('dexterity')
        else:
            self.combat['ac'] = armor + shield
       
        self.combat['proficiency'] = basic.getProficiency()
        self.combat['initiative'] = attributes.getModifier('intelligence')
        self.combat['spell-save'] = 8 + self.combat['proficiency'] + attributes.getModifier('intelligence')
        self.combat['spell-attack'] = self.combat['proficiency'] + attributes.getModifier('intelligence')

    def returnTable(self):

        return tabulate([[key,value] for key,value in self.combat.iteritems()])
