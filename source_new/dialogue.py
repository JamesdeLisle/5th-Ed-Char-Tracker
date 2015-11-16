from display import *

def initDisp():

    indentation = 3 
    stdscr = initialiseDisplay()
    curses.echo()

    return indentation,stdscr

def dialogue(stat):
    
    indentation,stdscr = initDisp()
             
    if stat.returnType() == 'int': 
        
        stat = dispInt(stat,indentation,stdscr) 
    
    elif stat.returnType()  == 'intr':

        stat = dispIntRange(stat,indentation,stdscr)

    elif stat.returnType() == 'intv':

        stat = dispIntValues(stat,indentation,stdscr)

    elif stat.returnType()== 'str':
      
        stat = dispStr(stat,indentation,stdscr)

    elif stat.returnType() == 'die':
        
        stat = dispDie(key,indentation,stdscr)

    elif stat.returnType() == 'lst':
        
        stat = dispLst(stat,indentation,stdscr)
         
    elif stat.returnType() == 'mlst':
        
        stat = dispMLst(stat,indentation,stdscr)

    elif stat.returnType() == 'bool':

        stat = dispBool(stat,indentation,stdscr)

    elif stat.returnType() == 'lstc':

        stat = dispListCont(stat,indentation,stdscr)

    return stat

def dispListCont(stat,indentation,stdscr):

    go_flag = True
    question_ypos = 2
    list_ypos = 4
    error_ypos = 4
    error_statement = '' 
    statement = '%s' % (stat.returnStatement())
    
    while go_flag:
        
        stdscr.addstr(error_ypos,indentation,error_statement)
        stdscr.refresh()
        stdscr.addstr(question_ypos,indentation,'%s' % (statement))
        stdscr.refresh()

        for idx,destat in enumerate(stat.returnList()):
            stdscr.addstr(list_ypos+idx,indentation,'%d) %s' % (idx+1,destat.returnLabel()))
            stdscr.refresh()

        y_end,x_end = curses.getsyx()    
        error_ypos = y_end + 6
        stdscr.addstr(y_end+4,indentation,'Pick a number: ')
        stdscr.refresh()
        choice = stdscr.getstr(y_end+4,indentation+16)
        
        try:
            test = int(choice)
            if 0 < test < len(stat.returnList())+1:
                go_flag = False 
            else:
                error_statement = 'Thats not an option!'
                stdscr.refresh()
        except ValueError:
            error_statement = 'Thats not a number!'
            
        stdscr.clear()
    
    
    stdscr.clear() 
    killDisplay()
    
    indentation,stdscr = initDisp()

    stat.list[int(choice)-1] = dialogue(stat.list[int(choice)-1])
    stat.setValue(stat.returnList())    

    return stat


def dispInt(stat,indentation,stdscr):

    go_flag = True
    question_ypos = 2
    error_ypos = 4
    error_statement = '' 
    statement = '%s' % (stat.returnStatement())

    while go_flag:
        
        stdscr.addstr(error_ypos,indentation,error_statement)
        stdscr.refresh() 
        stdscr.addstr(question_ypos,indentation,'%s: ' % (statement))
        stdscr.refresh()
        selection = stdscr.getstr(question_ypos,indentation+len(statement)+2) 
        
        try:    
            test = int(selection)        
            go_flag = False  
        except ValueError: 
            error_statement = 'Thats not a integer!'
        
        stdscr.clear()
    
    stat.setValue(int(selection))

    
    stdscr.clear() 
    killDisplay()

    return stat

def dispIntRange(key,names,indentation,stdscr,lists):

    go_flag = True
    question_ypos = 2
    error_ypos = 4
    error_statement = '' 
    statement = '%s' % (names[key][0])
    
    while go_flag:
        
        stdscr.addstr(error_ypos,indentation,error_statement)
        stdscr.refresh()    
        stdscr.addstr(question_ypos,indentation,'%s: ' % (statement))
        stdscr.refresh()
        selection = stdscr.getstr(question_ypos,indentation+len(statement)+2)
        
        try:   
            
            test = int(selection)
            if lists[key][0] <= test <= lists[key][1]:
                go_flag = False 
            else:
                error_statement = 'That is not in the allowed range (%d to %d)' % (lists[key][0],lists[key][1])
        
        except ValueError:
        
            error_statement = 'Thats not a integer!'
        
        stdscr.clear()

    return int(selection)

def dispIntValues(key,names,indentation,stdscr,lists):

    go_flag = True
    question_ypos = 2
    error_ypos = 4
    error_statement = '' 
    statement = '%s' % (names[key][0])
    
    while go_flag:
        
        stdscr.addstr(error_ypos,indentation,error_statement)
        stdscr.refresh()    
        stdscr.addstr(question_ypos,indentation,'%s: ' % (statement))
        stdscr.refresh()
        selection = stdscr.getstr(question_ypos,indentation+len(statement)+2)
        
        try:   
            
            test = int(selection)
            if test in lists[key]:
                go_flag = False 
            else:
                error_statement = 'That is not in the allowed range %s' % (str(lists[key]))
        
        except ValueError:
        
            error_statement = 'Thats not a integer!'
        
        stdscr.clear()

    return int(selection)

def dispStr(stat,indentation,stdscr):
    
    question_ypos = 2
    statement = '%s' % (stat.returnStatement())
    stdscr.addstr(question_ypos,indentation,'%s: ' % (statement))
    stdscr.refresh()
    selection = stdscr.getstr(question_ypos,indentation+len(statement)+2)
    stat.setValue(selection)
 
    stdscr.clear() 
    killDisplay()

    return stat

def dispDie(key,indentation,stdscr):

    go_flag = True 
    error_statement = ''
    question_ypos = 2
    error_ypos = 4
    dice = [4,6,8,10,12,20]
    statement = 'Please enter the %s. What kind of dice is it [d4,d6,d8,d10,d12,d20] (only type the number, e.g. 6): ' % (key.upper())

    while go_flag:
        stdscr.addstr(error_ypos,indentation,error_statement)
        stdscr.refresh()
        stdscr.addstr(question_ypos,indentation,'%s' % (statement))
        stdscr.refresh()
        dice_type = stdscr.getstr(question_ypos,indentation+len(statement)+2)
        try:
            test = int(dice_type)
            if test in dice:
                go_flag = False 
            else:
                error_statement = 'That is not a valid dice type!'
        except ValueError:
            error_statement = 'Thats not a integer!'
            

        stdscr.clear()

    go_flag = True 
    error_statement = ''
    question_ypos = 2
    error_ypos = 4
    dice = [4,6,8,10,12,20]
    statement = 'How many dice: '

    while go_flag:
        
        stdscr.addstr(error_ypos,indentation,error_statement)
        stdscr.refresh()
        stdscr.addstr(question_ypos,indentation,'%s' % (statement))
        stdscr.refresh()
        dice_type = stdscr.getstr(question_ypos,indentation+len(statement)+2)
        
        try:   
            test = int(dice_num)  
            go_flag = False 
        except ValueError: 
            error_statement = 'Thats not a integer!' 
        stdscr.clear()

    return [int(dice_num),int(dice_type),'%sd%s' % (dice_num,dice_type)]

def dispLst(key,indentation,stdscr,lists):

    go_flag = True
    question_ypos = 2
    list_ypos = 4
    error_ypos = 4
    error_statement = '' 
    statement = '%s' % (names[key][0])
    

    while go_flag:
        
        stdscr.addstr(error_ypos,indentation,error_statement)
        stdscr.refresh()
        stdscr.addstr(error_ypos,indentation,'%s' % (statement))
        stdscr.refresh()

        for idx,value in enumerate(lists[key]):
            stdscr.addstr(3+idx,indentation,'%d) %s' % (idx+1,value))
            stdscr.refresh()

        y_end,x_end = curses.getsyx()    
        error_ypos = y_end + 6
        stdscr.addstr(y_end+4,indentation,'Pick a number: ')
        stdscr.refresh()
        choice = stdscr.getstr(y_end+4,indentation+16)
        
        try:
            test = int(choice)
            
            if 0 < test < len(lists[key])+1:
                choice_flag = False    
            else:
                error_statement = 'Thats not an option!'
                stdscr.refresh()
        except ValueError:
            error_statement = 'Thats not a number!'
            
        stdscr.clear()

    return lists[key][int(choice)-1]

def dispMLst(key,indentation,stdscr,lists):

    go_flag = True
    options = { key : False for key in lists[key] }
    error_statement = '' 

    while go_flag:

        count = 1
        
        for key1,value in sorted(options.iteritems()):
            if value:
                stdscr.addstr(3+count,indentation,'%d) %s (*)' % (count,key1))
                stdscr.refresh()
            else:
                stdscr.addstr(3+count,indentation,'%d) %s    ' % (count,key1)) 
                stdscr.refresh()
            
            count += 1
        
        quit_ypos = count + 9
        statement_ypos = count + 5
        error_ypos = count + 7
        stdscr.addstr(quit_ypos,indentation,"If you have finished choosing press 'q'")
        statement = 'Pick a number (picking an already selected number will deselect it): ' 
        stdscr.addstr(statement_ypos,indentation,statement)
        stdscr.refresh()
        choice = stdscr.getstr(6 + count,indentation+len(statement))
        stdscr.addstr(error_ypos,indentation,error_statement)

        try:
            test = int(choice)
            if 0 < test < len(options)+1:
                options[sorted(options.iteritems())[test-1][0]] = not options[sorted(options.iteritems())[test-1][0]]
            else:
                error_statement = 'Thats not an option!'
        except ValueError:
            if choice == 'q':
                go_flag = False
            else:
                error_statement = 'Thats not a number!' 
        stdscr.clear()

    return options

def dispBool(key,names,indentation,stdscr):

    go_flag = True
    question_ypos = 2
    list_ypos = 4
    error_ypos = 4
    error_statement = '' 
    statement = '%s' % (names[key][0]) 
    lists = ['yes','no']

    while go_flag:
        
        stdscr.addstr(question_ypos,indentation,statement)
        stdscr.refresh()
        count = 1     
        for idx,value in enumerate(lists):
            stdscr.addstr(question_ypos+3+idx,indentation,'%d) %s' % (idx+1,value))
            stdscr.refresh()
            count += 1

        stdscr.addstr(question_ypos+5+count,indentation,error_statement)
        stdscr.refresh()
        stdscr.addstr(question_ypos+3+count,indentation,'Pick a number: ')
        stdscr.refresh()
        choice = stdscr.getstr(question_ypos+3+count,indentation+len(statement))
        try:
            test = int(choice)
            if 0 < test < len(lists)+1:
                go_flag = False
            else:
                error_statement = 'Thats not an option!'
        except ValueError:
            error_statement = 'Thats not a number!'
        
        stdscr.clear()

    if int(choice) == 1: return True
    else: return False
