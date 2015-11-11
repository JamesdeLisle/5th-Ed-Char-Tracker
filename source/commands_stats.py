from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob

def setAttribute(self,line):
    
    attribute_list = ['strength','dexterity','constitution','intelligence','wisdom','charisma'] 
    attribute = dispSingleList('Which attribute do you want to change?: ',attribute_list)
    value = dispSingleEntry('What is the new value?: ','integer')


    self.charState.attributes[attribute_list[int(attribute)-1]] = int(value)
    self.charState.updateSkills()
    self.charState.updateCombat()

def changeSkillProficiencies(self,line):
     
    self.charState.proficient_skills = dispMultipleListExisting('Select or deselect your skill proficiencies: ',self.charState.proficient_skills)
    self.charState.updateSkills()

def changeBasic(self,name):

    value = dispSingleEntry("Enter the new value for '%s':  " % (name),'string')
    self.charState.basic[name] = value
    self.charState.updateCombat()
    self.charState.updateSkills()

def comp_changeBasic(self, text, line, begidx, endidx):
     
    contents = self.charState.basic.iteritems()
    completions = [ key for key,value in contents ]
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]
