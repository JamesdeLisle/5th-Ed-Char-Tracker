import readline
import code
from inventory import *
from character_generator import *

def getModifier(attribute):

    return (attribute-10)/2

def getProficiency(level):
    
    proficiency = 0
    if level < 5:
        proficiency = 2
    elif  4 < level < 9:
        proficiency = 3
    elif 8 < level < 13:
        proficiency = 4
    elif 12 < level < 17:
        proficiency = 5
    elif 16 < level < 21:
        proficiency = 6

    return proficiency

def calculateSkills(attributes,proficient_skills,basic):
    
    skills = {} 
    skill_dependencies = {'acrobatics':'dexterity','animal-handling':'wisdom','arcana':'intelligence','athletics':'strength','deception':'charisma',\
            'history':'intelligence','insight':'wisdom','intimidation':'charisma','investigation':'intelligence','medicine':'wisdom',\
            'nature':'intelligence','perception':'wisdom','performance':'charisma','persuasion':'charisma','religion':'intelligence',\
            'sleight-of-hand':'dexterity','stealth':'dexterity','survival':'wisdom'}

    for key in proficient_skills:
        if proficient_skills[key]: 
            skills[key] = getProficiency(int(basic['level'])) + getModifier(int(attributes[skill_dependencies[key]]))
        else:
            skills[key] = getModifier(int(attributes[skill_dependencies[key]]))

    return skills

def calculateCombat(attributes, basic, equipped):

    combat = {}
    if equipped.armor == []:
        combat['ac'] = 10 + getModifier(int(attributes['dexterity']))
    else:
        combat['ac'] = int(equipped.armor[0].armor_class) + getModifier(int(attributes['dexterity']))

    combat['proficiency'] = getProficiency(int(basic['level']))
    combat['initiative'] = getModifier(int(attributes['dexterity']))
    combat['spell-save'] = 8 + combat['proficiency'] + getModifier(int(attributes['intelligence']))
    combat['spell-attack'] = combat['proficiency'] + getModifier(int(attributes['intelligence']))

    return combat

class equipped:

    def __init__(self,inventory):

        self.weapon = [ item for item in inventory.allStuff['weapon'] if item.equipped_flag]
        self.armor = [ item for item in inventory.allStuff['armor'] if item.equipped_flag] 
        self.magical = [ item for item in inventory.allStuff['magical'] if item.equipped_flag]
    
    def update(self,inventory):
 
        self.weapon = [ item for item in inventory.allStuff['weapon'] if item.equipped_flag]
        self.armor = [ item for item in inventory.allStuff['armor'] if item.equipped_flag] 
        self.magical = [ item for item in inventory.allStuff['magical'] if item.equipped_flag] 

class charstate:

    def __init__(self):
        
        self.basic = initialiseBasic()
        self.attributes = initialiseAttributes()
        self.vitality = initialiseVitality() 
        self.proficient_skills = initialiseProficientSkills()
        self.feats = initialiseFeats()
        self.skills = calculateSkills(self.attributes,self.proficient_skills,self.basic)
        self.inventory = inventory()
        self.equipped = equipped(self.inventory) 
        self.combat = calculateCombat(self.attributes,self.basic,self.equipped)
        self.spells = initialiseSpells()

    def updateEquipped(self):

        self.equipped.update(self.inventory)

    def updateCombat(self):

        self.combat = calculateCombat(self.attributes,self.basic,self.equipped)

    def updateSkills(self):

        self.skills = calculateSkills(self.attributes,self.proficient_skills,self.basic)

