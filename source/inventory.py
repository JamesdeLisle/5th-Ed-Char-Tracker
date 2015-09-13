from tabulate import tabulate
from dialogue import *
import pickle

class inventory:

    def __init__(self):

        self.allStuff = {}
        self.allStuff['weapon'] = []
        self.allStuff['armor'] = []
        self.allStuff['magical'] = []
        self.allStuff['adventure'] = []
        self.allStuff['tool'] = []
        self.allStuff['food'] = []
        self.allStuff['misc'] = []

    def addItem(self,item):

       self.allStuff[item.kind].append(item)
    
    def removeItem(self,item):
        
        for kind in self.allStuff:
            for tik2 in range(len(self.allStuff[kind])):
                if self.allStuff[kind][tik2].sub_kind == item:
                    self.allStuff[kind].pop(tik2)
                    break


    def getDictOfNames(self):

        dictOfNames = {}
        for kind in self.allStuff:
            for item in self.allStuff[kind]:
                if item.sub_kind in dictOfNames:
                    dictOfNames[item.sub_kind] = dictOfNames[item.sub_kind] + 1
                else:
                    dictOfNames[item.sub_kind] = 1
        
        return dictOfNames

class item(object):

    def __init__(self,properties):
        
        self.weight = properties['weight']
        self.kind = properties['kind']
        
class weapon(item):

    def __init__(self,properties):

        item.__init__(self,properties)
        self.properties = properties['props']
        self.sub_kind = properties['sub-kind']
        self.proficiency_type = properties['proficiency-type']
        self.damage = properties['damage']
        self.damage_type = properties['damage-type']
        self.equipped_flag = properties['equipped-flag']

class armor(item):

    def __init__(self,properties):

        item.__init__(self,properties)
        self.sub_kind = properties['sub-kind']
        self.proficiency_type = properties['proficiency-type']
        self.armor_class = properties['armor-class']
        self.dexterity_bonus = properties['dexterity-bonus']
        self.stealth_type = properties['stealth-type']
        self.minimum_strength = properties['minimum-strength']
        self.equipped_flag = properties['equipped-flag']

class magicalitem(item):

    def __init__(self,properties):
        
        item.__init__(self,properties)
        self.sub_kind = properties['sub-kind']
        self.attribute_bonuses = properties['attribute-bonuses']
        self.note = properties['note']
        self.equipped_flag = properties['equipped-flag']

class adventuringgear(item):

    def __init__(self,properties):
        
        item.__init__(self,properties)
        self.sub_kind = properties['sub-kind']
        self.note = properties['note']
        self.name = properties['name']

class tool(item):

    def __init__(self,properties):

        item.__init__(self,properties)
        self.sub_kind = properties['sub-kind']
        self.note = properties['note']
        self.name = properties['name']

class food(item):

    def __init__(self,properties):

        item.__init__(self,properties)
        self.sub_kind = properties['sub-kind']
        self.note = properties['note']

class misc(item):

    def __init__(self,properties):

        item.__init__(self,properties)
        self.sub_kind = properties['sub-kind']
        self.note = properties['note']

def addItem(self,line):
    
    kind_list = ['weapon','armor','magical item','adventuring gear','tool','food','misc']
    choice = dispSingleList('What kind of item is it?',kind_list)
    kind = kind_list[int(choice)-1]

    weight = dispSingleEntry('What is its weight (in lb) -> ','integer')
    
    properties = {'kind':kind,'weight':weight}

    if kind == 'weapon':
        properties, quantity = dialogueWeapon(properties)
        item = weapon(properties)
    elif kind == 'armor':
        properties, quantity = dialogueArmor(properties)
        item = armor(properties)
    elif kind == 'magical item':
        properties, quantity = dialogueMagicalItem(properties)
        item = magicalitem(properties)
    elif kind == 'adventuring gear':
        properties, quantity = dialogueAdventuringGear(properties)
        item = adventuringgear(properties)
    elif kind == 'tool':
        properties, quantity = dialogueTool(properties)
        item = tool(properties)
    elif kind == 'food':
        properties, quantity = dialogueFood(properties)
        item = food(properties)
    elif kind == 'misc':
        properties, quantity = dialogueMisc(properties)
        item = misc(properties)
    
    for tik in range(int(quantity)):
        self.charState.inventory.addItem(item)

    self.charState.updateEquipped()

def dialogueWeapon(properties):
    
    sub_kind = dispSingleEntry('What kind of weapon is it (e.g. Mace/Flail/Long Sword): ','string')
    properties['sub-kind'] = sub_kind    
    
    proficiency_list = ['simple','martial'] 
    proficiency_type = dispSingleList('What is the weapon proficiency type?',proficiency_list)
    properties['proficiency-type'] = proficiency_list[int(proficiency_type)-1]
 
    dice_list = ['d4','d6','d8','d10','d12','d20']
    dice_type = dispSingleList('What is the damage dice?',dice_list)
    dice_number = dispSingleEntry('How many damage dice is it: ','integer')
    properties['damage'] = '%s%s' % (dice_number,dice_list[int(dice_type)])

    damage_list = ['bludgeoning','slashing','piercing'] 
    damage_type = dispSingleList('What kind of damage does it do?',damage_list)
    properties['damage-type'] = damage_list[int(damage_type)]

    properties_list = ['ammunition','finesse','heavy','light','loading','range','reach','thrown','two-handed','versatile','user-defined']
    props = dispMultipleList('Select from the following weapon properties',properties_list)
    properties['props'] = { key : 0 for key in props }
        
    for entries in props:
        if entries == 'versatile':
            dice_type = dispSingleList("You said this weapon has the 'versatile' property. What is the damage dice?",dice_list)    
            dice_number = dispSingleEntry('How many damage dice is it: ','integer')
            properties['props']['finesse'] = '%s%s' % (dice_number,dice_list[int(dice_type)]) 

    for entries in props:
        if entries == 'range':
            range_value = dispSingleEntry('What is its range (e.g. 30/60) -> ','string')
            properties['props']['range'] = range_value     

    for entries in props:
        if entries == 'user-defined':
            note = dispSingleEntry('You said this weapon has some user-defined property. Please make a note of how it behaves: ','string')
            properties['props']['user-defined'] = note 
    
    quantity = dispSingleEntry('How many of this item are you adding to your inventory: ','integer')
        
    affirm_list = ['yes','no']
    equipped_flag = dispSingleList('Do you want ot equip this item now?' ,affirm_list)
    if equipped_flag:
        properties['equipped-flag'] = True
    else:
        properties['equipped-flag'] = False 

    return properties, quantity
    

def dialogueArmor(properties):

    sub_kind = dispSingleEntry('What kind of armour is it (e.g. Chain Mail/Plate/Leather): ','string')
    properties['sub-kind'] = sub_kind   
   
    proficiency_list = ['light','medium','heavy'] 
    proficiency_type = dispSingleList('What is the armor proficiency type?',proficiency_list)
    properties['proficiency-type'] = proficiency_list[int(proficiency_type)-1]

    armor_class = dispSingleEntry('What is its Armor Class (e.g. 10/11/12): ','integer')
    properties['armor-class'] = armor_class
   
    affirm_list = ['yes','no']
    dexterity_bonus = dispSingleList('Do you get a dexterity bonus?',affirm_list)
    if int(dexterity_bonus) == 1:
        properties['dexterity-bonus'] = True
    else:
        properties['dexterity-bonus'] = False 

    stealth_type = dispSingleList('Does your armour hinder your stealth?',affirm_list)
    if int(stealth_type) == 1:
        properties['stealth-type'] = True
    else:
        properties['stealth-type'] = False
   
    minimum_strength = dispSingleList('Does your armour require a  minimum strength?',affirm_list)
    if int(minimum_strength) == 1:
        min_strength_value = dispSingleEntry('What is the minimum strength required to wear this armour (e.g. 10/11/12): ','integer')
        properties['minimum-strength'] = [True,min_strength_value]
    else:
        properties['minimum-strength'] = [False,0.0]
    
    quantity = dispSingleEntry('How many of this item are you adding to your inventory: ','integer')

    affirm_list = ['yes','no']
    equipped_flag = dispSingleList('Do you want ot equip this item now?' ,affirm_list)
    if equipped_flag:
        properties['equipped-flag'] = True
    else:
        properties['equipped-flag'] = False

    return properties, quantity

def dialogueMagicalItem(properties):

    sub_kind = dispSingleEntry('What kind of magical item is it (e.g. Ring/Amulet/Wheel of Cheesse): ','string')
    properties['sub-kind'] = sub_kind


    attributes_list = ['strength','dexterity','constitution','intelligence','wisdom','charisma']
    atts = dispMultipleList('What attribute bonuses, if any, does this item give you? You will subsequently be asked to enter the values.',attributes_list)
    att_bonuses = []

    for entries in atts:
        bonus = dispSingleEntry('You said this item gives you a bonus to your %s. Enter the bonus now: ' % (entries.capitalize()),'integer')
        att_bonuses.append([entries,bonus])

    properties['attribute-bonuses'] = att_bonuses

    note = dispSingleEntry('If there is any extra information about this item, please make a note now: ','string')
    properties['note'] = note 

    quantity = dispSingleEntry('How many of this item are you adding to your inventory: ','integer')
    
    affirm_list = ['yes','no']
    equipped_flag = dispSingleList('Do you want ot equip this item now?' ,affirm_list)
    if equipped_flag:
        properties['equipped-flag'] = True
    else:
        properties['equipped-flag'] = False

    return properties, quantity

def dialogueAdventuringGear(properties):

    sub_kind = dispSingleEntry('What kind of gear is it (e.g. Book/Rope/Clothes): ','string')
    properties['sub-kind'] = sub_kind
    
    name = dispSingleEntry('Does this item have a special name (leave blank if not): ','string')
    properties['name'] = name

    note = dispSingleEntry('If there is any extra information about this item, please make a note now: ','string')
    properties['note'] = note

    quantity = dispSingleEntry('How many of this item are you adding to your inventory: ','integer')

    return properties, quantity
    
def dialogueTool(properties):

    sub_kind = dispSingleEntry('What kind of tool is it (e.g. Alchemist Tools/Forgery Kit/Navigator Tools): ','string')
    properties['sub-kind'] = sub_kind
    
    name = dispSingleEntry('Does this item have a special name (leave blank if not): ','string')
    properties['name'] = name

    note = dispSingleEntry('If there is any extra information about this item, please make a note now: ','string')
    properties['note'] = note

    quantity = dispSingleEntry('How many of this item are you adding to your inventory: ','integer')

    return properties, quantity

def dialogueFood(properties):

    sub_kind = dispSingleEntry('What kind of food is it (e.g. Apple/Egg/Carbonara): ','string')
    properties['sub-kind'] = sub_kind

    note = dispSingleEntry('If there is any extra information about this item, please make a note now: ','string')
    properties['note'] = note

    quantity = dispSingleEntry('How many of this item are you adding to your inventory: ','integer')

    return properties, quantity

def dialogueMisc(properties):

    sub_kind = dispSingleEntry('What is the item (e.g. Anything): ','string')
    properties['sub-kind'] = sub_kind

    note = dispSingleEntry('If there is any extra information about this item, please make a note now: ','string')
    properties['note'] = note

    quantity = dispSingleEntry('How many of this item are you adding to your inventory: ','integer') 

    return properties, quantity

