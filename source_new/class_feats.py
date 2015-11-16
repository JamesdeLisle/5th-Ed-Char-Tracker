from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob
import pickle
from textwrap import wrap
import copy

class feats:

    def __init__(self):

        self.feats = []

    def addFeat(self):

        self.feats.append(feat())

    def returnListOfNames(self):

        return [ [feat.returnName()] for feat in self.feats ]

    def checkIfExists(self):

        if len(self.feats) == 0: return False
        else: return True
    
    def returnTable(self):

        return tabulate(self.returnListOfNames())

    def returnFeat(self,name):

        for feat in self.feats:
            if feat.returnName() == name:
                return copy.deepcopy(feat)
                break
    
    def returnFeatIndex(self,feat_name):

        index = 0
        for idx,feat in enumerate(self.feats):
            if feat.returnName() == feat_name:
                index = idx
                break 
            
        return index

    def returnFeatFromList(self):
    
        names = []
        for feat in self.feats:
            names.append(feat.returnName())
        
        types = { 'choice':['Please select the feat you wish to examine','lst']}
        lists = {'choice':names}
        out = {'choice':''}
        
        choice = dispAskForAllDict(out,types,lists)
        
        return copy.deepcopy(self.returnFeat(choice['choice']))
   
class feat:

    def __init__(self):

        self.types = OrderedDict([('name',['What is the name of the feat','str']),\
                ('description',['Please write a description of the feat','str'])])

        self.properties = OrderedDict((key,0) for key in self.types)
        self.properties = dispAskForAllDict(self.properties,self.types)

    def returnName(self):
        
        return self.properties['name']

    def returnDescription(self):

        return [[entry] for entry in wrap(self.properties['description'])]
