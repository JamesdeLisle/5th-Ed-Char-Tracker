from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob
import pickle

def addItem(self,name):
    
    if name in self.charState.inventory.returnListOfNames(): 
        self.charState.inventory.addItem(name)
    else:
        print('That is not an available type of item!')

def comp_addItem(self, text, line, begidx, endidx):
     
    completions = self.charState.inventory.returnListOfNames()
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]

def chuckItem(self,name):

    if name in self.charState.inventory.returnListOfNames(): 
        self.charState.inventory.chuckItem(name)
    else:
        print('That is not an available type of item!')

def comp_chuckItem(self, text, line, begidx, endidx):
     
    completions = self.charState.inventory.returnListOfNames()
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]


