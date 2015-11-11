from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob

def spellBook(self,line):

    spell_lists = []
     
    for key,item in sorted(self.charState.spells.iteritems()):
        spell_lists.append(item)
    
    windows = []
    tables = []
    start_y = 0
    start_x = 0
    max_length = 0
    
    num = 1
    stdscr = initialiseDisplay() 

    for level in spell_lists:
        table = [ [ spell['name'] ] for spell in level ]
        tables.append(tabulate(table,headers=['level-%d'%(num)],tablefmt='orgtbl'))
        widths = [ len(item[0]) for item in table ]
        num += 1
        if widths != []:
            max_width = max(widths) + 10
        else:
            max_width = len('level-%d'%(num)) + 10

        windows.append(curses.newwin(len(table)+3,max_width,start_y,start_x))
        start_x += max_width
        if len(table) > max_length:
            max_length = len(table)

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

def addSpell(self,line):
    
    levels = ['level-1','level-2','level-3','level-4','level-5','level-6','level-7','level-8','level-9']
    level = dispSingleList('What level is the spell?', levels)
    name = dispSingleEntry('What is the name of the spell?: ','string')
    description = dispSingleEntry('If you want to, write a description of the spells effects: ','string')
    self.charState.spells['level-%s' % (level)].append({ 'name' : name, 'description' : description })
    


