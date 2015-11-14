from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob
import pickle

def addSpell(self,name):

    if name in self.charState.spellbook.returnLevels():
        self.charState.spellbook.addSpell(name)
    else:
        print('That is not an option!')

def comp_addSpell(self, text, line, begidx, endidx):
     
    completions = self.charState.spellbook.returnLevels()
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]

def chuckSpell(self,name):

    if name in self.charState.spellbook.returnLevels():
        self.charState.spellbook.chuckSpell(name)
    else:
        print('That is not an option!')

def comp_chuckSpell(self, text, line, begidx, endidx):
     
    completions = self.charState.spellbook.returnLevels()
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]

