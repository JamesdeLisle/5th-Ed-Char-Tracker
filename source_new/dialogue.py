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

def dispAskForAllDict(dictionary,names,lists=[]):

    indentation = 3 
    stdscr = initialiseDisplay()
    curses.echo()
    y,x = curses.getsyx()

    for key,value in dictionary.iteritems():

        if names[key][1] == 'int': 
            
            dictionary[key] = dispInt(y,x,key,names,indentation,stdscr) 

        elif names[key][1] == 'str':
          
            dictionary[key] = dispStr(y,x,key,names,indentation,stdscr)
 
        elif names[key][1] == 'die':
            
            dictionary[key] = dispDie(y,x,key,indentation,stdscr)

        elif names[key][1] == 'lst':
            
            dictionary[key] = dispLst(y,x,key,indentation,stdscr,lists)
             
        elif names[key][1] == 'mlst':
            
            dictionary[key] = dispMLst(y,x,key,indentation,stdscr,lists) 

        elif names[key][1] == 'bool':

            dictionary[key] = dispBool(y,x,key,names,indentation,stdscr)

        stdscr.clear()

    stdscr.clear()
    killDisplay()

    return dictionary


def dispAskForAllDictBool(dictionary,names,lists=[]):

    indentation = 3 
    stdscr = initialiseDisplay()
    curses.echo()
    y,x = curses.getsyx()

    for key,value in names.iteritems():
        if dictionary[key]:
            if names[key][1] == 'int': 
                
                dictionary[key] = dispInt(y,x,key,names,indentation,stdscr) 

            elif names[key][1] == 'str':
              
                dictionary[key] = dispStr(y,x,key,names,indentation,stdscr)
     
            elif names[key][1] == 'die':
                
                dictionary[key] = dispDie(y,x,key,indentation,stdscr)

            elif names[key][1] == 'lst':
                
                dictionary[key] = dispLst(y,x,key,indentation,stdscr,lists)
                 
            elif names[key][1] == 'mlst':
                
                dictionary[key] = dispMLst(y,x,key,indentation,stdscr,lists)

            elif names[key][1] == 'bool':

                dictionary[key] = dispBool(y,x,key,names,indentation,stdscr)

            stdscr.clear()

    stdscr.clear()
    killDisplay()

    return dictionary

def dispInt(y,x,key,names,indentation,stdscr):

    go_flag = True 
    
    while go_flag:
        
        statement = '%s' % (names[key][0])
        stdscr.addstr(y+2,indentation,'%s:' % (statement))
        stdscr.refresh()
        choice = stdscr.getstr(y+2,indentation+len(statement)+1)
        
        try:   
            test = int(choice)
            
            if int(choice) > 20 or int(choice) < 1:
                stdscr.addstr(y+4,indentation,'That value is not within the allowed 1-20 range!')
            else:
                go_flag = False
        
        except ValueError:
            stdscr.addstr(y+4,indentation,'Thats not a integer!')
            stdscr.refresh()
        
        stdscr.clear()

    return int(choice)

def dispStr(y,x,key,names,indentation,stdscr):

    statement = '%s' % (names[key][0])
    stdscr.addstr(y+2,indentation,'%s:' % (statement))
    stdscr.refresh()
    choice = stdscr.getstr(y+2,indentation+len(statement)+1)
    
    return choice

def dispDie(y,x,key,indentation,stdscr):

    go_flag = True 
    
    while go_flag:
        statement = 'Please enter the %s. What kind of dice is it (4,6,8,10,12,20): ' % (key.upper())
        stdscr.addstr(y+2,indentation,'%s' % (statement))
        stdscr.refresh()
        dice_type = stdscr.getstr(y+2,indentation+len(statement)+1)
        try:
            test = int(dice_type)
            if int(dice_type) == 4 or int(dice_type) == 6 or int(dice_type) == 8 or int(dice_type) == 10 or int(dice_type) == 12 or int(dice_type) == 20:
                go_flag = False 
            else:
                stdscr.addstr(y+4,indentation,'That is not a valid dice type!')
        except ValueError:
            stdscr.addstr(y+4,indentation,'Thats not a integer!')
            stdscr.refresh()

        stdscr.clear()

    
    go_flag = True 
    
    while go_flag:
        
        statement = 'How many dice %s: ' % (key.upper())
        stdscr.addstr(y+2,indentation,'%s' % (statement))
        stdscr.refresh()
        dice_num = stdscr.getstr(y+2,indentation+len(statement)+1)
         
        try:   
            test = int(dice_num)  
            go_flag = False 
        except ValueError:
            stdscr.addstr(y+4,indentation,'Thats not a integer!')
            stdscr.refresh()
        
        stdscr.clear()


    return [int(dice_num),int(dice_type),'%sd%s' % (dice_num,dice_type)]

def dispLst(y,x,key,indentation,stdscr,lists):

    y,x = curses.getsyx()
    curses.echo()
    choice_flag = True
    
    while choice_flag:
       
        for idx,value in enumerate(lists[key]):
            stdscr.addstr(3+idx,indentation,'%d) %s' % (idx+1,value))
            stdscr.refresh()
        
        stdscr.addstr(y+4,indentation,'Pick a number:')
        stdscr.refresh()
        choice = stdscr.getstr(y+4,indentation+16)
        try:
            test = int(choice)
            
            if 0 < test < len(lists[key])+1:
                choice_flag = False    
            else:
                stdscr.addstr(y+2,indentation,'Thats not an option!')
                stdscr.refresh()
        except ValueError:
            stdscr.addstr(y+2,indentation,'Thats not a number!')
            stdscr.refresh()
        stdscr.clear()

    return lists[key][int(choice)-1]

def dispMLst(y,x,key,indentation,stdscr,lists):

    input_flag = True
    options = { key : False for key in lists[key] }

    while input_flag:

        count = 1
        
        for key1,value in sorted(options.iteritems()):
            if value:
                stdscr.addstr(3+count,indentation,'%d) %s (*)' % (count,key1))
                stdscr.refresh()
            else:
                stdscr.addstr(3+count,indentation,'%d) %s    ' % (count,key1)) 
                stdscr.refresh()
            
            count += 1

        stdscr.addstr(5 + count,indentation,"If you have finished choosing press 'q'")
        
        stdscr.addstr(6 + count,indentation,'Pick a number (picking an already selected number will deselect it):')
        stdscr.refresh()
        choice = stdscr.getstr(9 + count,indentation+15)
        
        try:
            test = int(choice)
            if 0 < test < len(options)+1:
                options[sorted(options.iteritems())[test-1][0]] = not options[sorted(options.iteritems())[test-1][0]]
            else:
                stdscr.addstr(8 + count,indentation,'Thats not an option!')
                stdscr.refresh()
        except ValueError:
            if choice == 'q':
                input_flag = False
            else:
                stdscr.addstr(8 + count,indentation,'Thats not a number!')
                stdscr.refresh() 
        stdscr.clear()

    return options

def dispBool(y,x,key,names,indentation,stdscr):

    y,x = curses.getsyx()
    curses.echo()
    choice_flag = True
    
    lists = ['yes','no']

    while choice_flag:
        
        statement = '%s: ' % (names[key][0])
        stdscr.addstr(y+1,indentation,'%s' % (statement))
        stdscr.refresh()
        for idx,value in enumerate(lists):
            stdscr.addstr(y+3+idx,indentation,'%d) %s' % (idx+1,value))
            stdscr.refresh()
        
        stdscr.addstr(y+7,indentation,'Pick a number:')
        stdscr.refresh()
        choice = stdscr.getstr(y+7,indentation+16)
        try:
            test = int(choice)
            if 0 < test < len(lists)+1:
                choice_flag = False
            else:
                stdscr.addstr(y+9,indentation,'Thats not an option!')
                stdscr.refresh()
        except ValueError:
            stdscr.addstr(y+9,indentation,'Thats not a number!')
            stdscr.refresh()
        stdscr.clear()

    if int(choice) == 1: return True
    else: return False
