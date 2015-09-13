import readline
import code
from inventory import *

def getModifier(attribute):

    return (attribute-10)/2

def getProficiency(level):
    
    proficiency = 0
    if level < 5:
        proficiency = 2
    elif level < 9:
        proficiency = 3
    elif level < 13:
        proficiency = 4
    elif level < 17:
        proficiency = 5

    return proficiency

def readSaveData():
    
    save_file_name = 'save.dat' 
    save_file = open(save_file_name)
    save_data = {'basic':{},'attributes':{},'proficient_skills':{},'vitality':{}}
    
    lines = save_file.readlines()
    limits = { key : [idx for idx , data in enumerate(lines) if '--%s--' % (key) in data ] for (key) in save_data } 
    lines = { key : lines[limits[key][0]+1:limits[key][1]] for key in save_data }
    
    for key in save_data:
        for line in lines[key]:
            fields = line.strip().split()
            save_data[key][fields[0]] = fields[1]
 
    return  charstate(save_data)

def calculateSkills(attributes,proficient_skills):
    
    skills = {} 
    skill_dependencies = {'acrobatics':'dexterity','animal-handling':'wisdom','arcana':'intelligence','athletics':'strength','deception':'charisma',\
            'history':'intelligence','insight':'wisdom','intimidation':'charisma','investigation':'intelligence','medicine':'wisdom',\
            'nature':'intelligence','perception':'wisdom','performance':'charisma','persuasion':'charisma','religion':'intelligence',\
            'sleight-of-hand':'dexterity','stealth':'dexterity','survival':'wisdom'}

    for key in proficient_skills:
        if proficient_skills[key]: 
            skills[key] = 2 + getModifier(int(attributes[skill_dependencies[key]]))
        else:
            skills[key] = getModifier(int(attributes[skill_dependencies[key]]))

    return skills

def calculateCombat(attributes, basic):

    combat = {}
    combat['ac'] = 10 + getModifier(int(attributes['dexterity']))
    combat['proficiency'] = getProficiency(int(basic['level']))
    combat['initiative'] = getModifier(int(attributes['dexterity']))

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

    def __init__(self,save_data):
        
        self.basic = save_data['basic']
        self.attributes = save_data['attributes']
        self.vitality = save_data['vitality'] 
        self.proficient_skills = save_data['proficient_skills']
        self.skills = calculateSkills(self.attributes,self.proficient_skills)
        self.combat = calculateCombat(self.attributes,self.basic)
        self.inventory = inventory()
        self.equipped = equipped(self.inventory) 

    def updateEquipped(self):

        self.equipped.update(self.inventory)
