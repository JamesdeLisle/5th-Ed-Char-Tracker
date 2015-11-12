import cmd
import sys
sys.path.insert(1,'source_new/')
from character import *
from commands import *
from commands_sheet import *
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

    def do_createCharacter(self,line):
        createCharacter(self,line)

    def do_save(self,line):
        save(self,line)
    
    def do_load(self,name):
        load(self,name)

    def complete_load(self,text,line,begidx,endidx):
        return comp_load(self,text,line,begidx,endidx)

    def do_sheet(self,line):
        sheet(self,line)

    def do_quit(self, line):
        return True

if __name__ == '__main__':        
     
    CharacterTracker().cmdloop() 
