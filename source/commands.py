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

def setAttribute(self,line):
    
    attribute_list = ['strength','dexterity','constitution','intelligence','wisdom','charisma']
    print('\nWhich attribute do you want to change?\n\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\n6) Charisma\n')
    attribute = raw_input('Enter a number: ')
    print('\nWhat is the new value?\n')
    value = raw_input('Enter a number: ')
    
    self.charState.attributes[attribute_list[int(attribute)-1]] = int(value)
    self.charState.skills = calculateSkills(self.charState.attributes,self.charState.proficient_skills)
    self.charState.combat = calculateCombat(self.charState.attributes,self.charState.basic)

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
        headers = [['Attribute','Base','Modifier'],['Health',''],['Combat',''],['Skill','Value']]
        layout = ['start','row','row','col']
        head_count = 0
        att_flag = True
        for d in dicts: 
            table = []
            width = 0
            height = 0
            for key,value in d.iteritems():
                if att_flag:
                    table.append([key,value,getModifier(int(value))])
                    if len(key) + len(str(value)) + len(str(getModifier(int(value)))) > width:
                        width = len(key) + len(str(value)) 
                else:
                    table.append([key,value])
                    if len(key) + len(str(value)) > width:
                        width = len(key) + len(str(value)) 
                height += 1
            
            att_flag = False
            dims.append([width+15,3*height-1])
            tables.append(tabulate(table,headers=headers[head_count],tablefmt='grid'))   
            head_count += 1 

        windows.append(curses.newwin(dims[0][1],dims[0][0]+10,0,0))
        windows.append(curses.newwin(dims[1][1],dims[1][0],dims[0][1],0))
        windows.append(curses.newwin(dims[2][1]+10,dims[2][0]+10,dims[0][1]+dims[1][1]+2,0))
        windows.append(curses.newwin(dims[3][1],dims[3][0],0,dims[0][0]+20))
        
        for table,window in zip(tables,windows):
            window.addstr(0,0,table)
        
        stdscr.refresh()
        for window in windows:
            window.refresh()
        
        waitToKill(stdscr)

def inventoryShort(self,line):
    
    item_lists = []
    item_lists.append(self.charState.inventory.allStuff['weapon'])
    item_lists.append(self.charState.inventory.allStuff['armor'])
    item_lists.append(self.charState.inventory.allStuff['magical'])
    item_lists.append(self.charState.inventory.allStuff['adventure'])
    item_lists.append(self.charState.inventory.allStuff['tool'])
    item_lists.append(self.charState.inventory.allStuff['food'])
    item_lists.append(self.charState.inventory.allStuff['misc'])
    
    lengths = []
    for element in item_lists:
        lengths.append(len(element))

    if any(length != 0 for length in lengths):
        stdscr = initialiseDisplay() 
        windows = []
        
        tables = []
        start_y = 0
        start_x = 0
        max_length = 0

        for tik in range(len(lengths)): 
            width = 0
            table = []
            types = {}
            if lengths[tik] != 0:
                count = 0
                for item in item_lists[tik]:
                    if item.sub_kind in types:
                        types[item.sub_kind] = types[item.sub_kind] + 1
                    else:
                        types[item.sub_kind] = 1 
                    if len(item.sub_kind) > width:
                        width = len(item.sub_kind)
                    if len(item.kind) > width:
                        width = len(item.kind)
                
                table = [ [entry[0],types[entry[0]]] for entry in sorted(types.items()) ]
                tables.append(tabulate(table,headers=[item_lists[tik][0].kind,'#'],tablefmt='orgtbl'))

                if len(types) > max_length:
                    max_length = len(types)
                
                size_y = len(types) + 3
                size_x = width + 15
                
                windows.append(curses.newwin(size_y,size_x,start_y,start_x))
                
                start_y = start_y
                start_x = start_x + width + 15
        
        stdscr.addstr(max_length + 3, 3, "Press 'q' to return to the console.")

        for table,window in zip(tables,windows):
            window.addstr(0,0,table)
         
        stdscr.refresh()
        for window in windows:
            window.refresh()
        
        stdscr.addstr(max_length + 3, 3, "Press 'q' to return to the console.")

        key = ''
        while key != ord('q'):
            key = stdscr.getch()
        stdscr.clear()
        killDisplay()
    else:
        print('There is nothing in your inventory')

def chuckItem(self,item):
    
    contents = self.charState.inventory.getDictOfNames()
    
    go_flag = False
    for key in contents:
        if key == item:
            go_flag = True
            break

    number = 0
    
    if go_flag:
        if contents[item] > 1:
            within_range = True
            string = 'You have %d of this item. How many do you want to chuck: ' % (contents[item])
            while within_range:
                number = dispSingleEntry(string,'integer')
                if 0 < int(number) <= contents[item]:
                    within_range = False
                elif int(number) < 1:
                    string = "You can't throw away nothing! You have %d of this item. How many do you want to chuck: " % (contents[item])
                else:
                    string = "You don't have that many of that item! You have %d of this item. How many do you want to chuck: " % (contents[item])
            
            for tik in range(int(number)):
                self.charState.inventory.removeItem(item) 
        else:
            self.charState.inventory.removeItem(item)

    else:
        print("You dont have an item by that name!")
 
    self.charState.updateEquipped()

def comp_chuckItem(self, text, line, begidx, endidx):
     
    contents = self.charState.inventory.getDictOfNames()
    completions = [ item[0] for item in sorted(contents.items()) ]
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]

def save(self,line):

    with open('saves/%s.pkl'%(self.charState.basic['name']),'wb') as output:
        pickle.dump(self.charState,output,pickle.HIGHEST_PROTOCOL)

def load(self,name):
    
    with open('saves/%s.pkl'%(name),'rb') as input:
        self.charState = pickle.load(input)

    self.prompt = '%s > ' % (self.charState.basic['name'])

def comp_load(self, text, line, begidx, endidx):

    dirs = glob.glob('saves/*.pkl')
    completions = [ dir_name[6:len(dir_name)-4] for dir_name in dirs ]
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [name[offs:] for name in completions if name.startswith(mline)]


