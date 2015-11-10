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
        choice = dispSingleEntry('What is your %s?: ' % (attribute),'string')
        attributes[attribute] = choice

    return attributes


def initialiseProficientSkills():

    proficient_skills = {}

    skills = {'acrobatics':'dexterity','animal-handling':'wisdom','arcana':'intelligence','athletics':'strength','deception':'charisma',\
            'history':'intelligence','insight':'wisdom','intimidation':'charisma','investigation':'intelligence','medicine':'wisdom',\
            'nature':'intelligence','perception':'wisdom','performance':'charisma','persuasion':'charisma','religion':'intelligence',\
            'sleight-of-hand':'dexterity','stealth':'dexterity','survival':'wisdom'}
    
    skills_list = []

    for skill in skills:
        skills_list.append(skill)

    props = dispMultipleList('Select the skills you are proficient in:',skills_list)
    
    for key in skills:
        for entry in props:
            if key == entry:
                proficient_skills[key] = True
            else:
                proficient_skills[key] = False
    
    return proficient_skills

def initialiseVitality():

    vitality = {}
    vitality_list = ['hit-dice','temporary-health','max-health','current-health']
    
    for vital in vitality_list:
        choice = dispSingleEntry('What is your %s?: ' % (vital),'string')
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










    


