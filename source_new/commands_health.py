from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob
import pickle

def addTemporaryHealth(self,line):

    self.charState.health.addTemporaryHealth()

def clearTemporaryHealth(self,line): 

    self.charState.health.clearTemporaryHealth()

def takeDamage(self,line):

    self.charState.health.takeDamage()

def setHealth(self,name):

    if name in self.charState.health.returnListOfNames():
        self.charState.health.setHealth(name)
    else:
        print("That isn't something you can change!")

def comp_setHealth(self, text, line, begidx, endidx):
     
    completions = self.charState.health.returnListOfNames()
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]

def heal(self,line):

    self.charState.health.heal()

def shortRest(self,line):

    self.charState.health.shortRest(self.charState.attributes)

def addHitDice(self,line):

    self.charState.health.addHitDice(self.charState.basic)
