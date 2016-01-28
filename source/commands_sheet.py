from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob


def returnHeightWidth(table):

    width = 0
    for line in table.split('\n'):
        if width < len(line): width = len(line)
    
    height = len(table.split('\n')) + 1


    return height+1,width+1

def sheet(self,line):
    
    if self.charState == []:
        print("You haven't loaded any character yet! Use the 'load' command.")
    else:
        stdscr = initialiseDisplay()
        tabs = []
        tabs.append(self.charState.basic.table)

        tables = []
        
        for tab in tabs:
            tables.append(tab.returnTable())

        #tables.append(self.charState.basic.table.returnTable())
        #tables.append(self.charState.attributes.returnTable())
        #tables.append(self.charState.health.returnTable())
        #tables.append(self.charState.combat.returnTable())
        #tables.append(self.charState.skills.returnTable())
        
        dimensions = []
        
        for tab in tabs:
            dimensions.append(tab.returnHeightWidth())

        windows = []
        
        windows.append(curses.newwin(dimensions[0][0],dimensions[0][1],0,0))
        #windows.append(curses.newwin(dimensions[1][0],dimensions[1][1],dimensions[0][0],0))
        #windows.append(curses.newwin(dimensions[2][0],dimensions[2][1],dimensions[4][0],max(dimensions[:][1])+3))
        #windows.append(curses.newwin(dimensions[3][0],dimensions[3][1],dimensions[0][0]+dimensions[1][0],0))
        #windows.append(curses.newwin(dimensions[4][0],dimensions[4][1],0,max(dimensions[:][1])+3))
        
        for window, table in zip(windows,tables):
            window.addstr(0,0,table)

        stdscr.refresh()
        
        for window in windows:
            window.refresh()
        
        waitToKill(stdscr) 

def showInventory(self,line):

    if self.charState.inventory.checkIfExists():
        stdscr = initialiseDisplay()
        tables = self.charState.inventory.returnTable()
        
        dimensions = []
        
        for table in tables:
            dimensions.append(returnHeightWidth(table))
        
        windows = []    
        windows.append(curses.newwin(dimensions[0][0],dimensions[0][1],0,0))
        windows.append(curses.newwin(dimensions[1][0],dimensions[1][1],0,dimensions[0][1]))
        windows.append(curses.newwin(dimensions[2][0],dimensions[2][1],0,dimensions[0][1]+dimensions[1][1]))
        windows.append(curses.newwin(dimensions[3][0],dimensions[3][1],0,dimensions[0][1]+dimensions[1][1]+dimensions[2][1]))
        windows.append(curses.newwin(dimensions[4][0],dimensions[4][1],0,dimensions[0][1]+dimensions[1][1]+dimensions[2][1]+dimensions[3][1]))
        windows.append(curses.newwin(dimensions[5][0],dimensions[5][1],0,dimensions[0][1]+dimensions[1][1]+dimensions[2][1]+dimensions[3][1]+dimensions[4][1]))
        
        for window, table in zip(windows,tables):
            window.addstr(0,0,table)

        stdscr.refresh()
        
        for window in windows:
            window.refresh()
        
        waitToKill(stdscr) 
    else:
        print("You have nothing in your inventory!")

def showFeats(self,line):

    if self.charState.feats.checkIfExists():

        stdscr = initialiseDisplay()
        table = self.charState.feats.returnTable()
        dimension = returnHeightWidth(table)
        window = curses.newwin(dimension[0],dimension[1],0,0)
        window.addstr(0,0,table)
        stdscr.refresh()
        window.refresh()
        waitToKill(stdscr)
    else:
        print("You have no feats!")

def examineFeat(self,line):

    if self.charState.feats.checkIfExists():
        
        choice = self.charState.feats.returnFeatFromList()
        stdscr = initialiseDisplay()

        tables = []

        tables.append(tabulate([[choice.returnName()]]))
        tables.append(tabulate(choice.returnDescription()))

        dimensions = []

        for table in tables:
            dimensions.append(returnHeightWidth(table))

        windows = []

        windows.append(curses.newwin(dimensions[0][0],dimensions[0][1],0,0))
        windows.append(curses.newwin(dimensions[1][0],dimensions[1][1],dimensions[0][0],0))

        for window, table in zip(windows,tables):
            window.addstr(0,0,table)

        stdscr.refresh()

        for window in windows:
            window.refresh()

        waitToKill(stdscr)

    else:
        print("You have no feats!")

def examineItem(self,name):

    if self.charState.inventory.checkIfExists():
        
        choice = self.charState.inventory.returnItemFromList(name)
        stdscr = initialiseDisplay()
         
        table = choice.returnTable()
        dimension = returnHeightWidth(table)
       
        window = curses.newwin(dimension[0],dimension[1],0,0)
        window.addstr(0,0,table)

        stdscr.refresh()
        window.refresh()
        
        waitToKill(stdscr)

    else:
        print("You have no items!")

def comp_examineItem(self, text, line, begidx, endidx):
     
    completions = self.charState.inventory.returnListOfNames()
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]

def showSpellBook(self,line):

    if self.charState.spellbook.checkIfExists():
        
        stdscr = initialiseDisplay()
        tables = self.charState.spellbook.returnTable()
        
        dimensions = []
        
        for table in tables:
            dimensions.append(returnHeightWidth(table))
        
        windows = []   
        spacing = 0
        for rect in dimensions:
            windows.append(curses.newwin(rect[0],rect[1],0,spacing))
            spacing += rect[1]
       
        for window, table in zip(windows,tables):
            window.addstr(0,0,table)

        stdscr.refresh()
        
        for window in windows:
            window.refresh()
        
        waitToKill(stdscr) 
    else:
        print('You have nothing in your spellbook!')

def examineSpell(self,name):

    if self.charState.spellbook.checkIfExists():
        if name in self.charState.spellbook.returnLevels(): 
            
            choice = self.charState.spellbook.returnSpellFromList(name)
            stdscr = initialiseDisplay()

            tables = []

            tables.append(tabulate([[choice.returnName()]]))
            tables.append(tabulate(choice.returnDescription()))

            dimensions = []

            for table in tables:
                dimensions.append(returnHeightWidth(table))

            windows = []

            windows.append(curses.newwin(dimensions[0][0],dimensions[0][1],0,0))
            windows.append(curses.newwin(dimensions[1][0],dimensions[1][1],dimensions[0][0],0))

            for window, table in zip(windows,tables):
                window.addstr(0,0,table)

            stdscr.refresh()

            for window in windows:
                window.refresh()

            waitToKill(stdscr)
        else:
            print('That is not an option!')
    else:
        print("You have no spells!")

def comp_examineSpell(self, text, line, begidx, endidx):
     
    completions = self.charState.spellbook.returnLevels()
    mline = line.partition(' ')[2]
    offs = len(mline) - len(text)

    return [item[offs:] for item in completions if item.startswith(mline)]
