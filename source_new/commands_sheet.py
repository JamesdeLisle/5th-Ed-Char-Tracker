from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob

#def createNewWindow(height,width,start_y,start_x)

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
        tables = []
        tables.append(self.charState.basic.returnTable())
        tables.append(self.charState.attributes.returnTable())
        tables.append(self.charState.health.returnTable())
        tables.append(self.charState.combat.returnTable())
        tables.append(self.charState.skills.returnTable())
        dimensions = []
        
        for table in tables:
            dimensions.append(returnHeightWidth(table))

        windows = []
        
        windows.append(curses.newwin(dimensions[0][0],dimensions[0][1],0,0))
        windows.append(curses.newwin(dimensions[1][0],dimensions[1][1],dimensions[0][0],0))
        windows.append(curses.newwin(dimensions[2][0],dimensions[2][1],dimensions[4][0],max(dimensions[:][1])+3))
        windows.append(curses.newwin(dimensions[3][0],dimensions[3][1],dimensions[0][0]+dimensions[1][0],0))
        windows.append(curses.newwin(dimensions[4][0],dimensions[4][1],0,max(dimensions[:][1])+3))
        
        for window, table in zip(windows,tables):
            window.addstr(0,0,table)

        stdscr.refresh()
        
        for window in windows:
            window.refresh()
        
        waitToKill(stdscr) 
        
        
    
    
