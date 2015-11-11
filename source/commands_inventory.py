from display import *
from character import *
from tabulate import tabulate
from os import listdir
import glob

def inventoryShort(self,line):
    
    item_lists = []
    item_lists.append(self.charState.inventory.allStuff['weapon'])
    item_lists.append(self.charState.inventory.allStuff['armor'])
    item_lists.append(self.charState.inventory.allStuff['magical'])
    item_lists.append(self.charState.inventory.allStuff['adventure-gear'])
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

def showEquipped(self,line):

    equipped_lists = []
     
    equipped_lists.append(self.charState.equipped.weapon)
    equipped_lists.append(self.charState.equipped.armor)
    equipped_lists.append(self.charState.equipped.magical)

    windows = []
    tables = []
    start_y = 0
    start_x = 0
    max_length = 0
    
    num = 0
    stdscr = initialiseDisplay() 
    
    kinds = ['weapons','armor','magical']
    for items in equipped_lists:
        table = [ [ item.sub_kind ] for item in items  ]
        tables.append(tabulate(table,headers=[kinds[num]],tablefmt='orgtbl'))
        widths = [ len(entry[0]) for entry in table ]
        
        if widths != []:
            if max(widths) > len(kinds[num]):
                max_width = max(widths) + 10
            else:
                max_width = len(kinds[num]) + 10
        else:
            max_width = len(kinds[num]) + 10

        windows.append(curses.newwin(len(table)+3,max_width,start_y,start_x))
        start_x += max_width
        
        if len(table) > max_length:
            max_length = len(table)
        
        num += 1
        
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




