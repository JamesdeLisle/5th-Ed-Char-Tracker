from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob
import pickle


def prompt(self,line):
    
    self.prompt = line + ': '

def save(self,line):

    with open('saves/%s.pkl'%(self.charState.basic.getValue('name')),'wb') as output:
        pickle.dump(self.charState,output,pickle.HIGHEST_PROTOCOL)

def load(self,name):
    
    dirs = glob.glob('saves/*.pkl')
    exist_flag = False

    for exist in dirs:
        if 'saves/%s.pkl'%(name) == exist:
            exist_flag = True
    if exist_flag:
        with open('saves/%s.pkl'%(name),'rb') as input:
            self.charState = pickle.load(input)

        self.prompt = '%s > ' % (self.charState.basic.getValue('name'))
    else:
        print('There is no character by that name!')

def comp_load(self, text, line, begidx, endidx):

    dirs = glob.glob('saves/*.pkl')
    completions = [ dir_name[6:len(dir_name)-4] for dir_name in dirs ]
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [name[offs:] for name in completions if name.startswith(mline)]

def createCharacter(self,line):

    self.charState = charstate()

