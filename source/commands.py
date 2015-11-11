from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob


def prompt(self,line):
    
    self.prompt = line + ': '

def attributes(self,line):

    table = []
    
    for key, value in self.charState.attributes.iteritems():
        table.append([key,value,getModifier(int(value))])
    
    out = tabulate(table,headers=['Attribute','Base','Modifier'],tablefmt='grid')
    outputToDash(0,0,out)

def skills(self,line):

    table = []
    
    for key, value in self.charState.skills.iteritems():
        table.append([key,value])
    
    out = tabulate(table,headers=['Skill','Value'],tablefmt='grid')
    outputToDash(0,0,out)


def vitality(self,line):
    
    table = []
    
    for key,    value in self.charState.vitality.iteritems():
        table.append([key,value])
        
    out = tabulate(table,tablefmt='grid')
    outputToDash(0,0,out)

def comabat(self,line):
    
    table = []
    
    for key, value in self.charState.combat.iteritems():
        table.append([key,value])
        
    out = tabulate(table,tablefmt='grid')
    outputToDash(0,0,out)

def sheet(self,line):
    
    if self.charState == []:
        print("You haven't loaded any character yet! Use the 'load' command.")
    else:
        stdscr = initialiseDisplay() 
        
        windows = []
        tables = []
        dicts = []
        dims = []

        dicts.append(self.charState.attributes)
        dicts.append(self.charState.vitality)
        dicts.append(self.charState.combat)
        dicts.append(self.charState.skills)
        
        headers = [['Attribute','Base','Modifier'],['Health',''],['Combat',''],['Skill','Value','Prof']]
        layout = ['start','row','row','col']
        
        head_count = 0
        counter = 0
        skill_flag = False

        for d in dicts: 
            table = []
            width = 0
            height = 0
            
            for key,value in d.iteritems():
                if counter == 0:
                    table.append([key,value,getModifier(int(value))])
                    if len(key) + len(str(value)) + len(str(getModifier(int(value)))) > width:
                        width = len(key) + len(str(value)) 
                elif counter == 3:
                    if self.charState.proficient_skills[key]:
                        star = '(*)'
                    else:
                        star = ' '
                    table.append([key,value,star])
                    if len(key) + len(str(value)) + len(str(star)) > width:
                        width = len(key) + len(str(value))  
                else:
                    if key == 'hit-dice':
                        table.append([key,value[2]])
                        if len(key) + len(str(value)) > width:
                            width = len(key) + len(str(value))
                    else:
                        table.append([key,value])
                        if len(key) + len(str(value)) > width:
                            width = len(key) + len(str(value))

                height += 1
            counter += 1

            att_flag = False
            dims.append([width+15,3*height-1])
            tables.append(tabulate(table,headers=headers[head_count],tablefmt='grid'))   
            head_count += 1 

        windows.append(curses.newwin(dims[0][1],dims[0][0]+20,0,0))
        windows.append(curses.newwin(dims[1][1],dims[1][0]+20,dims[0][1],0))
        windows.append(curses.newwin(dims[2][1]+10,dims[2][0]+20,dims[0][1]+dims[1][1]+2,0))
        windows.append(curses.newwin(dims[3][1],dims[3][0]+30,0,dims[0][0]+25))
        
        for table,window in zip(tables,windows):
            window.addstr(0,0,table)
        
        stdscr.refresh()
        for window in windows:
            window.refresh()
        
        waitToKill(stdscr)

def save(self,line):

    with open('saves/%s.pkl'%(self.charState.basic['name']),'wb') as output:
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

        self.prompt = '%s > ' % (self.charState.basic['name'])
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

def updateCombat(self,line):

    self.charState.updateCombat()

def updateSkills(self,line):

    self.charState.updateSkills()




    
    
