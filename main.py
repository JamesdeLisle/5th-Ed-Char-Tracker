import cmd
import readline
from character import *
from tabulate import tabulate
import curses
import curses.textpad

def initialiseDisplay():

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1) 
    return stdscr

def killDisplay():

    curses.nocbreak()
    curses.echo()
    curses.endwin()

def outputToDash(ypos,xpos,output):

    stdscr = initialiseDisplay()
    stdscr.addstr(ypos,xpos,output) 
    stdscr.refresh()
    y,x = curses.getsyx()
    stdscr.addstr(y+2,0,"Press 'q' to return to the console")
    stdscr.refresh()
    key = ''
    while key != ord('q'):
        key = stdscr.getch()
    stdscr.clear()
    killDisplay()

class CharacterTracker(cmd.Cmd):
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.charState = readSaveData()
        self.prompt = '%s > ' % (self.charState.basic['name'])
        self.intro = "\n=============================\n5th Edition Character Tracker\n=============================\n"     
        self.doc_header = 'doc_header'
        self.misc_header = 'misc_header'
        self.undoc_header = 'undoc_header'
        self.ruler = '-' 

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_attributes(self,line):
        table = []
        for key, value in self.charState.attributes.iteritems():
            table.append([key,value,getModifier(value)])
        out = tabulate(table,headers=['Attribute','Base','Modifier'],tablefmt='grid')
        outputToDash(0,0,out) 
    
    def do_skills(self,line):
        table = []
        for key, value in self.charState.skills.iteritems():
            table.append([key,value])
        
        out = tabulate(table,headers=['Skill','Value'],tablefmt='grid')
        outputToDash(0,0,out)

    def do_vitality(self,line):
        table = []
        for key,    value in self.charState.vitality.iteritems():
            table.append([key,value])
            
        out = tabulate(table,tablefmt='grid')
        outputToDash(0,0,out)

    def do_combat(self,line):
        table = []
        for key, value in self.charState.combat.iteritems():
            table.append([key,value])
            
        out = tabulate(table,tablefmt='grid')
        outputToDash(0,0,out)
        
    def do_setAttribute(self,line):
        
        attribute_list = ['strength','dexterity','constitution','intelligence','wisdom','charisma']
        print('\nWhich attribute do you want to change?\n\n1) Strength\n2) Dexterity\n3) Constitution\n4) Intelligence\n5) Wisdom\n6) Charisma\n')
        attribute = raw_input('Enter a number: ')
        print('\nWhat is the new value?\n')
        value = raw_input('Enter a number: ')
        
        self.charState.attributes[attribute_list[int(attribute)-1]] = int(value)
        self.charState.skills = calculateSkills(self.charState.attributes,self.charState.proficient_skills)
        self.charState.combat = calculateCombat(self.charState.attributes,self.charState.basic)

    def do_sheet(self,line):
        stdscr = initialiseDisplay()
        at_win = curses.newwin(40,40,0,0)
        vi_win = curses.newwin(40,40,0,41)
        co_win = curses.newwin(40,30,0,64)
        sk_win = curses.newwin(40,80,0,87)
        table = []
        for key, value in self.charState.attributes.iteritems():
            table.append([key,value,getModifier(value)])
        out = tabulate(table,headers=['Attribute','Base','Modifier'],tablefmt='grid')
        at_win.addstr(0,0,out) 
        table = []
        for key,    value in self.charState.vitality.iteritems():
            table.append([key,value])    
        out = tabulate(table,tablefmt='grid')
        vi_win.addstr(0,0,out)
        table = []
        for key, value in self.charState.combat.iteritems():
            table.append([key,value])    
        out = tabulate(table,tablefmt='grid')
        co_win.addstr(0,0,out)
        table = []
        for key, value in self.charState.skills.iteritems():
            table.append([key,value]) 
        out = tabulate(table,headers=['Skill','Value'],tablefmt='grid')
        sk_win.addstr(0,0,out)
        stdscr.refresh()
        at_win.refresh()
        vi_win.refresh()
        co_win.refresh()
        sk_win.refresh()
        key = ''
        while key != ord('q'):
            key = stdscr.getch()
        stdscr.clear()
        killDisplay()

    def do_quit(self, line):
        return True
    
    def write(self,text) :
        screen.clear()
        textwin.clear()
        screen.addstr(3,0,text)
        screen.refresh()
 

if __name__ == '__main__':        
     
    CharacterTracker().cmdloop() 
