from display import *
from dialogue import *

def initialiseBasic():
    
    basic = {}

    choice = dispSingleEntry('What race are you?: ','string')
    basic['race'] = choice

    choice = dispSingleEntry('What gender are you?: ','string')
    basic['gender'] = choice

    choice = dispSingleEntry('What class are you?: ','string')
    basic['class'] = choice

    choice = dispSingleEntry('What level are you?: ','integer')
    basic['level'] = choice

    choice = dispSingleEntry('What is your name?: ','string')
    basic['name'] = choice

    return basic

def initialiseAttributes():

    attributes = {}
    attribute_list = ['strength','dexterity','constitution','intelligence','wisdom','charisma']

    for attribute in attribute_list:
        choice = dispSingleEntry('What is your %s?: ' % (attribute.upper()),'string')
        attributes[attribute] = choice

    return attributes


def initialiseProficientSkills():

    skills = {'acrobatics':'dexterity','animal-handling':'wisdom','arcana':'intelligence','athletics':'strength','deception':'charisma',\
            'history':'intelligence','insight':'wisdom','intimidation':'charisma','investigation':'intelligence','medicine':'wisdom',\
            'nature':'intelligence','perception':'wisdom','performance':'charisma','persuasion':'charisma','religion':'intelligence',\
            'sleight-of-hand':'dexterity','stealth':'dexterity','survival':'wisdom'}
    
    proficient_skills = { key : False for key,value in skills.iteritems() }

    skills_list = []

    proficient_skills = dispMultipleListExisting('Select or deselect your skill proficiencies: ', proficient_skills)
    
    return proficient_skills

def initialiseVitality():

    vitality = {}
    vitality_list = ['hit-dice','temporary-health','max-health','current-health']
    dice_list = ['d4','d6','d8','d10','d12','d20']
    dice_list_real = [4,6,8,10,12,20]

    for vital in vitality_list:
        if vital == 'hit-dice':
            num_dice = dispSingleEntry('How many HIT DICE do you have?: ','integer')
            type_dice = dispSingleList('What is the HIT DICE TYPE?', dice_list)
            vitality[vital] = [int(num_dice),dice_list_real[int(type_dice)-1],'%dd%d'%(int(num_dice),dice_list_real[int(type_dice)-1])]
        else:
            choice = dispSingleEntry('What is your %s?: ' % (vital.upper()),'string')
            vitality[vital] = choice

    return vitality

def initialiseFeats():

    go_flag = True
    feats = []

    while go_flag:
        
        feat = {}
        choice = dispSingleEntry('Add a Feat. What is the feat called?: ','string')
        feat['name'] = choice
        
        choice = dispSingleEntry('Write a description of the effect of the feat: ','string')
        feat['description'] = choice
        
        affirm_list = ['yes','no']
        dexterity_bonus = dispSingleList('Done. Do you want to add another?',affirm_list)
       
        if int(dexterity_bonus) == 2:
            go_flag = False

    return feats

def initialiseSpells():

    go_flag = True
    spells = {}
    levels = ['level-1','level-2','level-3','level-4','level-5','level-6','level-7','level-8','level-9']

    spells = { level : [] for level in levels }

    while go_flag:

        level = dispSingleList('What level is the spell?', levels)
        
        name = dispSingleEntry('What is the name of the spell?: ','string')
        description = dispSingleEntry('If you want to, write a description of the spells effects: ','string')

        spells['level-%s' % (level)].append({ 'name' : name, 'description' : description })
        
        affirm_list = ['yes','no']
        dexterity_bonus = dispSingleList('Done. Do you want to add another?',affirm_list)
       
        if int(dexterity_bonus) == 2:
            go_flag = False

    return spells












    


