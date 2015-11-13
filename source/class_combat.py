from collections import OrderedDict
from dialogue import *
from tabulate import tabulate


class combat:

    def __init__(self,inventory,basic,attributes):
        
        self.combat = {}
        self.calculateCombat(inventory,basic,attributes) 

    def returnTable(self):

        return tabulate([[key,value] for key,value in self.combat.iteritems()],tablefmt='grid')

    def calculateCombat(self,inventory,basic,attributes):

        armor,shield = inventory.equipped.getAC() 

        if armor == 0:
            self.combat['ac'] = 10 + shield + attributes.getModifier('dexterity')
        else:
            self.combat['ac'] = armor + shield
       
        self.combat['proficiency'] = basic.getProficiency()
        self.combat['initiative'] = attributes.getModifier('intelligence')
        self.combat['spell-save'] = 8 + self.combat['proficiency'] + attributes.getModifier('intelligence')
        self.combat['spell-attack'] = self.combat['proficiency'] + attributes.getModifier('intelligence')
