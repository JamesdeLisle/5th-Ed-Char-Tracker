from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob

def setAttribute(self,name):
    
    if name in self.charState.attributes.returnListOfNames():
        self.charState.attributes.changeSingleAttribute(name)
    else:
        print("That isn't an attribute!")

    self.charState.skills.calculateSkills(self.charState.basic,self.charState.attributes)
    self.charState.combat.calculateCombat(self.charState.inventory,self.charState.basic,self.charState.attributes) 

def comp_setAttribute(self, text, line, begidx, endidx):
     
    completions = self.charState.attributes.returnListOfNames()
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]

def setSkillProficiencies(self,line):

    self.charState.skills.changeProficiencies()
    self.charState.skills.calculateSkills(self.charState.basic,self.charState.attributes)

def setBasic(self,name):
    
    if name in self.charState.basic.returnListOfNames():
        self.charState.basic.changeSingleBasic(name)
    else:
        print("That isn't an attribute!")

    self.charState.skills.calculateSkills(self.charState.basic,self.charState.attributes)
    self.charState.combat.calculateCombat(self.charState.inventory,self.charState.basic,self.charState.attributes) 

def comp_setBasic(self, text, line, begidx, endidx):
     
    completions = self.charState.basic.returnListOfNames()
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]
