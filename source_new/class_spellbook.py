from collections import OrderedDict
from dialogue import *
from tabulate import tabulate
import copy
from textwrap import wrap

class spellbook:

    def __init__(self,basic):
        
        self.names = ['cantrips','level-1','level-2','level-3','level-4','level-5','level-6','level-7','level-8','level-9']
        self.spellbook = OrderedDict((key,[]) for key in self.names)
        self.spellslots = spellslots()

    def addSpell(self,level):
        
        self.spellbook[level].append(spell())

    def returnLevels(self):

        return self.names
    
    def checkIfExists(self):

        flag = False

        for key,value in self.spellbook.iteritems():
            if len(value) != 0: flag = True

        return flag
    
    def returnTable(self):

        tables = []
        for key1,item_list in self.spellbook.iteritems():
            names = []
            for item in item_list:
                names.append([item.returnName()])
            tables.append(tabulate(names,headers=[key1],tablefmt='grid'))
        
        return tables

    def returnSpellIndex(self,spell_level,spell_name):

        index = 0
        for idx,spell in enumerate(self.spellbook[spell_level]):
            if spell.returnName() == spell_name:
                index = idx
                break 
            
        return index
        
    def returnSpellFromList(self,spell_level):
        
        names = []
        for spell in self.spellbook[spell_level]:
            names.append(spell.returnName())
        
        types = { 'choice':['Please select the spell you wish to examine','lst']}
        lists = {'choice':names}
        out = {'choice':''}

        choice = dispAskForAllDict(out,types,lists)
        
        index = self.returnSpellIndex(spell_level,choice['choice'])
        
        return copy.deepcopy(self.spellbook[spell_level][index])
        
    
    def chuckSpell(self,spell_level):

        names = []
        for spell in self.spellbook[spell_level]:
            names.append(spell.returnName())
        
        types = { 'choice':['Please select the spell you wish to throw away','lst']}
        lists = {'choice':names}
        out = {'choice':''}

        choice = dispAskForAllDict(out,types,lists)
        
        index = self.returnSpellIndex(spell_level,choice['choice'])
        self.spellbook[spell_level].pop(index)

class spellslots:

    def __init__(self,basic):

        self.slots = OrderedDict(('level-%d' % (tik+1),0) for tik in range(0,9))
        self.slots = self.setSlots()


    def setSlots(self):


        

        

class spell:

    def __init__(self):

        self.types = OrderedDict([('name',['What is the name of the spell','str']),\
                ('description',['Write a description of the spells effects','str'])])

        self.properties = OrderedDict((key,'') for key,value in self.types.iteritems())
        self.properties = dispAskForAllDict(self.properties,self.types)

    def returnName(self):

        return self.properties['name']

    def returnDescription(self):

        return [[entry] for entry in wrap(self.properties['description'])]
    
