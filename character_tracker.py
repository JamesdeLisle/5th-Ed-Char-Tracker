import cmd
from character import *
from commands import *

class CharacterTracker(cmd.Cmd):
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.charState = []
        self.prompt = 'CHARTRACKER> '
        self.intro = "\n=============================\n5th Edition Character Tracker\n=============================\n"     
        self.doc_header = 'doc_header'
        self.misc_header = 'misc_header'
        self.undoc_header = 'undoc_header'
        self.ruler = '-' 

    def do_prompt(self, line):
        prompt(self,line) 

    def do_attributes(self,line):
        attributes(self,line)
    
    def do_skills(self,line):
        skills(self,line) 

    def do_vitality(self,line):
        vitality(self,line)

    def do_combat(self,line):
        combat(self,line)
        
    def do_setAttribute(self,line):
        setAttribute(self,line)
        
    def do_sheet(self,line):
        sheet(self,line)

    def do_addItem(self,line):
        addItem(self,line)
    
    def do_inventoryShort(self,line):
        inventoryShort(self,line)
   
    def do_chuckItem(self, item):
        chuckItem(self,item)
        
    def complete_chuckItem(self,text,line,begidx,endidx):
        return comp_chuckItem(self,text,line,begidx,endidx)

    def do_save(self,line):
        save(self,line)
    
    def do_load(self,name):
        load(self,name)

    def complete_load(self,text,line,begidx,endidx):
        return comp_load(self,text,line,begidx,endidx)

    def do_quit(self, line):
        return True

if __name__ == '__main__':        
     
    CharacterTracker().cmdloop() 
