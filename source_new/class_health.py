from collections import OrderedDict
from dialogue import *
from tabulate import tabulate
from dice import *
import copy

class health:

    def __init__(self):
        
        self.names = OrderedDict([('hit-dice',['What are your hit dice','die']),\
                ('max-health',['What is your maximum health','int']),\
                ('temporary-health',['Do you currently have any temporary health','int']),\
                ('current-health',['What is you current health','int'])])

        self.health = OrderedDict((key,0) for key in self.names)
        self.changeAllHealth()

    def changeAllHealth(self):
        
        self.health = dispAskForAllDict(self.health,self.names)

    def returnTable(self):
        
        out = copy.deepcopy(self.health)
        out['hit-dice'] = out['hit-dice'][2]
        return tabulate([[key,value] for key,value in out.iteritems()],tablefmt='grid')

    def returnListOfNames(self):

        return [ key[0] for key in self.names.iteritems() ]

    def addTemporaryHealth(self):

        self.health['temporary-health'] = self.health['temporary-health'] + int(dispSingleEntry('How much temporary-health would you like to add: ','int'))

    def clearTemporaryHealth(self):

        self.health['temporary-health'] = 0

    def takeDamage(self):

        damage = int(dispSingleEntry('How much damage do you take: ','int'))
        temporary = int(self.health['temporary-health'])
        current = int(self.health['current-health'])
       
        if temporary != 0:
            if temporary - damage > 0:
                self.health['temporary-health'] = temporary - damage
            else:
                self.health['current-health'] = current - (damage - temporary)
                self.health['temporary-health'] = 0
        else:
            self.health['current-health'] = current - damage

    def setHealth(self,kind):

        self.health[kind] = dispAskForAllDict({kind:0},self.names)[kind]
     
    def addHitDice(self,basic):
        
        num = int(dispSingleEntry('How much hit-dice would you like to add: ','int'))

        if num + self.health['hit-dice'][0] > basic.returnLevel():
            self.health['hit-dice'][0] = basic.returnLevel()
        else:
            self.health['hit-dice'][0] = num + self.health['hit-dice'][0] 

    def heal(self):

        points = int(dispSingleEntry('How many points do you heal: ','int'))
        current = int(self.health['current-health'])
        maximum = int(self.health['max-health'])

        if points + current > maximum:
            self.health['current-health'] = maximum
        else:
            self.health['current-health'] = current + points

    def shortRest(self,attributes):

        num_rolled = int(dispSingleEntry('How many dice do you want to use: ','int'))
        num_dice = int(self.health['hit-dice'][0])
        type_dice = int(self.health['hit-dice'][1])
        hit_healed = 0
        current = int(self.health['current-health'])
        maximum = int(self.health['max-health'])
        
        if num_rolled >= num_dice:
            for tik in range(0,num_dice):
                hit_healed += roll(type_dice) + attributes.getModifier('constitution') 
            self.health['hit-dice'][0] = 0
            self.health['hit-dice'][2] = '%dd%d' % (self.health['hit-dice'][0],self.health['hit-dice'][1] )
        else:
            for tik in range(0,num_rolled):
                hit_healed += roll(type_dice) + attributes.getModifier('constitution')
            self.health['hit-dice'][0] = num_dice - num_rolled
            self.health['hit-dice'][2] = '%dd%d' % (self.health['hit-dice'][0],self.health['hit-dice'][1] )
        
        if hit_healed + current > maximum:
            self.health['current-health'] = maximum
        else:
            self.health['current-health'] = current + hit_healed
    
     
