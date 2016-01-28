from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob

def changebasic(self,line):

    self.charState.basic.changeBasic()

def changeattribute(self,line):
    
    self.charState.attributes.changeAttribute()

def changeName(self,line):

    self.charState.basic.changeName()
