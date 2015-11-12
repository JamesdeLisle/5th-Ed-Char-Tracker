from class_basic import *
from class_attributes import *
from class_health import *
from class_skills import *
from class_inventory import *
from class_combat import *

class charstate:

    def __init__(self):
        
        self.basic = basic()
        self.attributes = attributes()
        self.health = health()
        self.skills = skills()
        self.skills.calculateSkills(self.basic,self.attributes)
        self.inventory = inventory()
        self.combat = combat(self.inventory,self.basic,self.attributes)

