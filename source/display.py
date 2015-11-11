import curses
import curses.textpad
import readline

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

def waitToKill(stdscr):

    key = ''
    
    y,x = curses.getsyx()
    stdscr.addstr(y+10,0,"Press 'q' to return to the console")
    stdscr.refresh()

    while key != ord('q'):
        key = stdscr.getch()
    
    stdscr.clear()
    killDisplay()


def outputToDash(ypos,xpos,output):

    stdscr = initialiseDisplay()
    stdscr.addstr(ypos,xpos,output) 
    stdscr.refresh()
    
    y,x = curses.getsyx()
    stdscr.addstr(y+10,0,"Press 'q' to return to the console")
    stdscr.refresh()
    
    key = ''

    while key != ord('q'):
        key = stdscr.getch()
    
    stdscr.clear()
    killDisplay()


