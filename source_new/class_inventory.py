from collections import OrderedDict
from dialogue import *

class inventory:

    def __init__(self):

        self.classes = ['weapon','armor','magical','adventuring-gear','tool','misc']
        self.inventory = { key : [] for key in self.classes }
        self.equipped = equipped()

    def addItem(self,item_type):
        
        if item_type == 'weapon':
            item = weapon()
            self.inventory[item_type].append(item)
            if item.properties['equipped']: self.equipped.equipItem(item)
            else: pass
        elif item_type == 'armor':
            item = armor()
            self.inventory[item_type].append(item)
            if item.properties['equipped']: self.equipped.equipItem(item)
            else: pass
        elif item_type == 'magical':
            item = magical()
            self.inventory[item_type].append(item)
            if item.properties['equipped']: self.equipped.equipItem(item)
            else: pass
        elif item_type == 'adventuring-gear':
            self.inventory[item_type].append(adventuringgear())
        elif item_type == 'tool':
            self.inventory[item_type].append(tool())
        elif item_type == 'misc':
            self.inventory[item_type].append(misc())

class equipped:

    def __init__(self):

        self.weapons_left_hand = []
        self.weapons_right_hand = []
        self.armor = []
        self.shield = []
        self.magical = [] 
        self.lists = { 'weapon':['left-hand','right-hand'],\
                'armor':['armor','shield'],\
                'magical':['left-hand','right-hand','neck'] }
        

    def equipItem(self,item):

        if item.properties['class'] == 'weapon':
            occupation = [len(self.weapons_left_hand),len(self.weapons_right_hand)]
            if item.properties['qualities']['two-handed']:
                if occupation == [0,0]:
                    self.weapons_left_hand.append(item)
                else:
                    if dispAskForAllDict({'replace':False},{'replace':['You already have a weapon equipped. Would you like to replace it with the new item','bool']})['replace']:
                        self.weapons_left_hand = []
                        self.weapons_right_hand = []
                        self.weapons_left_hand.append(item)
                    else:
                        pass
            else:
                if occupation == [0,0]:
                    self.weapons_left_hand.append(item)
                elif occupation == [1,0] or occupation == [0,1]:
                    if self.weapons_left_hand[0].properties['two-handed']:
                        if dispAskForAllDict({'replace':False},{'replace':['You already have a two handed weapon equipped. Do you want to replace it with the new weapon','bool']})['replace']:
                            self.weapons_left_hand = []
                            self.weapons_right_hand = []
                            self.weapons_left_hand.append(item)
                        else:
                            pass
                    else:
                        if dispAskForAllDict({'replace':False},{'replace':['You already have one weapon equipped. Do you want to dual wield','bool']})['replace']:
                            if occupation == [1,0]: self.weapons_right_hand.append(item)
                            else: self.weapons_left_hand.append(item)
                        else:
                            self.weapons_left_hand = []
                            self.weapons_right_hand = []
                            self.weapons_left_hand.append(item)

        elif item['class'] == 'armor':
            occupation = [len(self.armor),len(self.shield)]
            if item['type'] == 'Shield' or item['type'] == 'shield':
                if occupation == [0,0]:
                    self.shield.append(item)
                else:
                    if dispAskForAllDict({'replace':False},{'replace':['You already have a shield equipped. Would you like to replace it with the new item','bool']})['replace']:
                        self.weapons_left_hand = []
                        self.weapons_right_hand = []
                        self.weapons_left_hand.append(item)
                    else:
                        pass
            else:
                if occupation == [0,0]:
                    self.armor.append(item)
                else:
                    if dispAskForAllDict({'replace':False},{'replace':['You already have armor equipped. Would you like to replace it with the new item','bool']})['replace']:
                        self.weapons_left_hand = []
                        self.weapons_right_hand = []
                        self.weapons_left_hand.append(item)
                    else:
                        pass
            
        elif item['class'] == 'magical':
            self.magical.append(item)
    
    def getAC(self):
        
        occupation = [len(self.shield),len(self.armor)]
    
        if occupation == [0,0]: return 0,0 
        elif occupation == [1,0]: return self.armor[0].properties['armor-class'],0
        elif occupation == [0,1]: return 0,self.shield[0].properties['armor-class']
        else: return self.shield[0].properties['armor-class'] + self.armor[0].properties['armor-class']
    
        
class weapon:

    def __init__(self):

        self.property_types = OrderedDict([('weight',['What is the items weight','int']),\
                ('type',['What kind of weapon is it (e.g. mace, longsword, staff)','str']),\
                ('proficiency-type',['What is the proficiency type','lst']),\
                ('damage',['What are the damage dice','die']),\
                ('damage-type',['What is the damage type','lst']),\
                ('qualities',['Please select the properties','mlst']),\
                ('quantity',['How many do you want to add','int']),\
                ('equipped',['Do you want to equip this item ','bool'])])
        
        self.lists = {'proficiency-type':['simple','martial'],\
                'damage-type':['bludgeoning','slashing','piercing'],\
                'qualities':['ammunition','finesse','heavy','light','loading','range','reach','thrown','two-handed','versatile','user-defined']}

        self.properties = OrderedDict((key,0) for key in self.property_types)
        self.properties = dispAskForAllDict(self.properties,self.property_types,self.lists)
        
        self.qualities_types = {'versatile':["You said this weapon has the 'versatile' property.",'die'],\
                'range':['What is its range (e.g. 30/60)','int'],\
                'user-defined':['You said this weapon has some user-defined property. Please make a note of how it behaves:  ','str']}
                 
        self.properties['qualities'] = dispAskForAllDictBool(self.properties['qualities'],self.qualities_types)
        self.properties['class'] = 'weapon'
        
            
class armor:

    def __init__(self):
        
        self.property_types = OrderedDict([('weight',['What is the items weight','int']),\
                ('type',['What kind of armour is it (e.g. Chain Mail/Plate/Leather/Shield)','str']),\
                ('proficiency-type',['What is the proficiency type','lst']),\
                ('armor-class',['What is its Armor Class (e.g. 10/11/12)','int']),\
                ('dexterity-bonus',['Do you gain a dexterity bonus','bool']),\
                ('stealth-penalty',['Does this armor give a penalty to your stealth','bool']),\
                ('quantity',['How many of this item are you adding','int']),\
                ('equipped',['Do you want to equip this item','bool'])])
        
        self.lists = {'proficiency-type':['light','medium','heavy']}
                
        self.properties = OrderedDict((key,0) for key in self.property_types)
        self.properties = dispAskForAllDict(self.properties,self.property_types,self.lists)
        self.properties['class'] = 'armor'

class magical:

    def __init__(self):

        self.property_types = OrderedDict([('weight',['What is the items weight','int']),\
                ('type',['What kind of item is it (e.g. Ring, Amulet, Wand)','str']),\
                ('attribute-bonus',['What attribute bonuses does it give','mlst']),\
                ('armor-class-bonus',['What (if any) bonus does it give to your AC','int']),\
                ('quantity',['How many of this item are you adding','int']),\
                ('equipped',['Do you want to equip this item','bool'])])
        
        self.lists = {'attribute-bonus':['strength','dexterity','constitution','intelligence','wisdom','charisma']}
                
        self.properties = OrderedDict((key,0) for key in self.property_types)
        self.properties = dispAskForAllDict(self.properties,self.property_types,self.lists)
        
        self.attribute_bonus_types = {'strength':['You said this item grants a strength bonus, what is the bonus','int'],\
                'dexterity':['You said this item grants a dexterity bonus, what is the bonus','int'],\
                'constitution':['You said this item grants a constitution bonus, what is the bonus','int'],\
                'intelligence':['You said this item grants a intelligence bonus, what is the bonus','int'],\
                'wisdom':['You said this item grants a wisdom bonus, what is the bonus','int'],\
                'charisma':['You said this item grants a charisma bonus, what is the bonus','int']}
        
        self.properties['attribute-bonus'] = dispAskForAllDictBool(self.properties['attribute-bonus'],self.attribute_bonus_types)
        self.properties['class'] = 'magical'

class adventuringgear:
        
    def __init__(self):

        self.property_types = OrderedDict([('weight',['What is the items weight','int']),\
                ('type',['What kind of item is it (e.g. Book/Rope/Clothes)','str']),\
                ('note',['If there is any extra information about this item, please make a note now','str']),\
                ('quantity',['How many of this item are you adding','int'])])
        
        self.properties = OrderedDict((key,0) for key in self.property_types)
        self.properties = dispAskForAllDict(self.properties,self.property_types,self.lists)
        self.properties['class'] = 'adventuring-gear'


class tool:
        
    def __init__(self):

        self.property_types = OrderedDict([('weight',['What is the items weight','int']),\
                ('type',['What kind of item is it (e.g. Alchemist Tools/Forgery Kit/Navigator Tools)','str']),\
                ('note',['If there is any extra information about this item, please make a note now','str']),\
                ('quantity',['How many of this item are you adding','int'])])
        
        self.properties = OrderedDict((key,0) for key in self.property_types)
        self.properties = dispAskForAllDict(self.properties,self.property_types,self.lists)
        self.properties['class'] = 'armor'

class misc:

    def __init__(self):

        self.property_types = OrderedDict([('weight',['What is the items weight','int']),\
                ('type',['What kind of item is it','str']),\
                ('note',['If there is any extra information about this item, please make a note now','str']),\
                ('quantity',['How many of this item are you adding','int'])])
        
        self.properties = OrderedDict((key,0) for key in self.property_types)
        self.properties = dispAskForAllDict(self.properties,self.property_types,self.lists)
        self.properties['class'] = 'misc'










