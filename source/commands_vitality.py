from dice import *
from display import *
from character import *
from tabulate import tabulate

def takeDamage(self,damage):
    
    temporary = int(self.charState.vitality['temporary-health'])
    current = int(self.charState.vitality['current-health'])

    if temporary != 0:
        if (temporary - int(damage)) > 0:
            self.charState.vitality['temporary-health'] = temporary - int(damage)
        else: 
            self.charState.vitality['current-health'] = current - (int(damage) - temporary) 
            self.charState.vitality['temporary-health'] = 0
    else:       
        self.charState.vitality['current-health'] = current - int(damage)
            
def addTemporaryHealth(self,points):
    
    self.charState.vitality['temporary-health'] = int(self.charState.vitality['temporary-health']) + int(points)

def clearTemporaryHealth(self,points):

    self.charState.vitality['temporary-health'] = 0

def heal(self,points):
    
    current = int(self.charState.vitality['current-health'])
    max_points = int(self.charState.vitality['max-health'])
 
    if (int(points) + current) <= max_points:
        self.charState.vitality['current-health'] = current + int(points)
    else:
        self.charState.vitality['current-health'] = max_points

def setMaxHitPoints(self,points):

    self.charState.vitality['max-health'] = int(points)

def restShort(self,number):

    num_dice = int(self.charState.vitality['hit-dice'][0])
    type_dice = int(self.charState.vitality['hit-dice'][1])
    hit_healed = 0
    current = int(self.charState.vitality['current-health'])
    maximum = int(self.charState.vitality['max-health'])

    if int(number) >= num_dice:
        for tik in range(0,num_dice):
            hit_healed += roll(type_dice) + getModifier(int(self.charState.attributes['constitution']))
        self.charState.vitality['hit-dice'][0] = 0
        self.charState.vitality['hit-dice'][2] = '%dd%d' % (int(self.charState.vitality['hit-dice'][0]),int(self.charState.vitality['hit-dice'][1]))
    else:
        for tik in range(0,int(number)):
            hit_healed += roll(type_dice) + getModifier(int(self.charState.attributes['constitution']))
        self.charState.vitality['hit-dice'][0] = num_dice - int(number)
        self.charState.vitality['hit-dice'][2] = '%dd%d' % (int(self.charState.vitality['hit-dice'][0]),int(self.charState.vitality['hit-dice'][1]))

    if (current + hit_healed) > maximum:
        self.charState.vitality['current-health'] = maximum
    else:
        self.charState.vitality['current-health'] = current + hit_healed

def addHitDice(self,number):

    current = int(self.charState.vitality['hit-dice'][0])
    if int(number) + current > int(self.charState.basic['level']):
        self.charState.vitality['hit-dice'][0] = int(self.charState.basic['level'])
        self.charState.vitality['hit-dice'][2] = '%dd%d' % (int(self.charState.vitality['hit-dice'][0]),int(self.charState.vitality['hit-dice'][1])) 
    else:
        self.charState.vitality['hit-dice'][0] = current + int(number)
        self.charState.vitality['hit-dice'][2] = '%dd%d' % (int(self.charState.vitality['hit-dice'][0]),int(self.charState.vitality['hit-dice'][1]))

def restExtended(self):

    addHitDice(self,int(self.charState.basic['level'])/2)
