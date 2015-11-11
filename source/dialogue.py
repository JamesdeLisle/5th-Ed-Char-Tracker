from display import *

def dispSingleList(statement,options):
    
    indentation = 3 
    
    stdscr = initialiseDisplay()
    stdscr.addstr(1,indentation,statement)
    stdscr.refresh()
    
    for tik in range(len(options)):
        stdscr.addstr(3+tik,indentation,'%d) %s' % (tik+1,options[tik]))
        stdscr.refresh()
   
    y,x = curses.getsyx()
    curses.echo()
    choice_flag = True
    
    while choice_flag:
        stdscr.addstr(y+4,indentation,'Pick a number:               ')
        stdscr.refresh()
        choice = stdscr.getstr(y+4,indentation+16)
        try:
            test = int(choice)
            
            if 0 < test < len(options)+1:
                choice_flag = False
            else:
                stdscr.addstr(y+2,indentation,'Thats not an option!                ')
                stdscr.refresh()
        except ValueError:
            stdscr.addstr(y+2,indentation,'Thats not a number!                     ')
            stdscr.refresh()

    stdscr.clear()
    killDisplay()
    
    return choice

def dispSingleEntry(statement,input_type):
    indentation = 3 
    stdscr = initialiseDisplay()
    curses.echo()
    choice_flag = True
    y,x = curses.getsyx()
    
    while choice_flag:
        stdscr.addstr(y+2,indentation,'%s                                             ' % (statement))
        stdscr.refresh()
        choice = stdscr.getstr(y+2,indentation+len(statement)+1)
        if input_type == 'integer':
            try:
                test = int(choice)
                choice_flag = False
            except ValueError:
                stdscr.addstr(y+2,indentation,'Thats not a number!                     ')
                stdscr.refresh()
        elif input_type == 'string':
            choice_flag = False

    stdscr.clear()
    killDisplay()

    return choice

def dispMultipleList(statement,options):
    
    indentation = 3 
    stdscr = initialiseDisplay()

    curses.echo()
    
    stdscr.addstr(1,indentation,statement)
    stdscr.refresh()

    input_flag = True
    props = []

    while input_flag:
        
        count = 1
        for values in options:
            choose_flag = False
            for chosen in props: 
                if chosen == values:
                    choose_flag = True
            if choose_flag:
                stdscr.addstr(3+count,indentation,'%d) %s (*)' % (count,values))
                stdscr.refresh()
            else:
                stdscr.addstr(3+count,indentation,'%d) %s    ' % (count,values)) 
                stdscr.refresh()
            count = count + 1 
        
        stdscr.addstr(5 + count,indentation,"If you want to undo your last choice press 'u'")
        stdscr.addstr(6 + count,indentation,"If you have finished choosing press 'q'")
        
        stdscr.addstr(9 + count,indentation,'Pick a number:               ')
        stdscr.refresh()
        choice = stdscr.getstr(9 + count,indentation+15)
       
        try:
            test = int(choice)
            if 0 < test < len(options)+1:
                redundant_flag = True
                if len(props) > 0:
                    for chosen in props:
                        if chosen == options[int(choice)-1]:
                            redundant_flag = False
                    if redundant_flag:
                        props.append(options[int(choice)-1])
                else:
                    props.append(options[int(choice)-1])
            else:
                stdscr.addstr(8 + count,indentation,'Thats not an option!                ')
                stdscr.refresh()
        except ValueError:
            if choice == 'u':
                if len(props) > 0:
                    props.pop(len(props)-1)
            elif choice == 'q':
                input_flag = False
            else:
                stdscr.addstr(8 + count,indentation,'Thats not a number!                     ')
                stdscr.refresh() 
    
    stdscr.clear()
    killDisplay()

    return props

def dispMultipleListExisting(statement,options):

    indentation = 3 
    stdscr = initialiseDisplay()

    curses.echo()
    
    stdscr.addstr(1,indentation,statement)
    stdscr.refresh()

    input_flag = True

    while input_flag:

        count = 1
        
        for key,value in sorted(options.iteritems()):
            if value:
                stdscr.addstr(3+count,indentation,'%d) %s (*)' % (count,key))
                stdscr.refresh()
            else:
                stdscr.addstr(3+count,indentation,'%d) %s    ' % (count,key)) 
                stdscr.refresh()
            
            count += 1

        
        stdscr.addstr(5 + count,indentation,"If you have finished choosing press 'q'")
        
        stdscr.addstr(6 + count,indentation,'Pick a number (picking an already selected number will deselect it):               ')
        stdscr.refresh()
        choice = stdscr.getstr(9 + count,indentation+15)

        try:
            test = int(choice)
            if 0 < test < len(options)+1:
                options[sorted(options.iteritems())[test-1][0]] = not options[sorted(options.iteritems())[test-1][0]]
            else:
                stdscr.addstr(8 + count,indentation,'Thats not an option!                ')
                stdscr.refresh()
        except ValueError:
            if choice == 'q':
                input_flag = False
            else:
                stdscr.addstr(8 + count,indentation,'Thats not a number!                     ')
                stdscr.refresh() 

    stdscr.clear()
    killDisplay()

    return options
