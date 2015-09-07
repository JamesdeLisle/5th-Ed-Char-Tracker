import readline
import code


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
    basic = {}
    attributes = {}
    proficient_skills = []
    vitality = {}

    lines = save_file.readlines()

    basic_limits = [idx for idx , data in enumerate(lines) if '%--basic--%' in data ]
    basic_lines = lines[basic_limits[0]+1:basic_limits[1]]
    attribute_limits = [idx for idx , data in enumerate(lines) if '%--attributes--%' in data ]
    attribute_lines = lines[attribute_limits[0]+1:attribute_limits[1]]
    proficientskills_limits = [idx for idx , data in enumerate(lines) if '%--proficientskills--%' in data ]
    proficientskills_lines = lines[proficientskills_limits[0]+1:proficientskills_limits[1]]
    vitality_limits = [idx for idx , data in enumerate(lines) if '%--vitality--%' in data ]
    vitality_lines = lines[vitality_limits[0]+1:vitality_limits[1]]

    for line in basic_lines:
        fields = line.strip().split()
        basic[fields[0]] = fields[1]

    for line in attribute_lines:
        fields = line.strip().split()
        attributes[fields[0]] = int(fields[1])
    
    for line in proficientskills_lines:
        fields = line.strip().split()
        proficient_skills.append(fields[0]) 

    for line in vitality_lines:
        fields = line.strip().split()
        vitality[fields[0]] = int(fields[1])

    return  charstate(basic,attributes,proficient_skills,vitality)

def calculateSkills(attributes,proficient_skills):
    
    skills = {}
    
    skill_types = {'acrobatics':'dexterity','animal handling':'wisdom','arcana':'intelligence','athletics':'strength','deception':'charisma',\
            'history':'intelligence','insight':'wisdom','intimidation':'charisma','investigation':'intelligence','medicine':'wisdom',\
            'nature':'intelligence','perception':'wisdom','performance':'charisma','persuasion':'charisma','religion':'intelligence',\
            'sleight of hand':'dexterity','stealth':'dexterity','survival':'wisdom'}

    for key in skill_types:
        for tik in range(len(proficient_skills)):
            if key == proficient_skills[tik]:
                skills[key] = 2 + getModifier(attributes[skill_types[key]])
                break
            skills[key] = getModifier(attributes[skill_types[key]])


    return skills

def calculateCombat(attributes, basic):

    combat = {}

    combat['ac'] = 10 + getModifier(attributes['dexterity'])
    combat['proficiency'] = getProficiency(int(basic['level']))
    combat['initiative'] = getModifier(attributes['dexterity'])

    return combat



class charstate:

    def __init__(self,basic,attributes,proficient_skills,vitality):
        
        self.basic = basic
        self.attributes = attributes
        self.skills = calculateSkills(self.attributes,proficient_skills)
        self.vitality = vitality
        self.combat = calculateCombat(self.attributes,self.basic)
        self.proficient_skills = proficient_skills

