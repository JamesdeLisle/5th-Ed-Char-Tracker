import cmd
import sys
sys.path.insert(1,'source/')
from character import *
from commands import *
from commands_sheet import *
from commands_stats import *
from commands_health import *
from commands_inventory import *
from commands_feats import *
from commands_spellbook import *

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
        
    def do_s(self,line):
        sheet(self,line)

    def do_setAttribute(self,name):
        setAttribute(self,name)
    
    def complete_setAttribute(self, text, line, begidx, endidx):
        return comp_setAttribute(self, text, line, begidx, endidx)

    def do_setSkillProficiencies(self,line):
        setSkillProficiencies(self,line)

    def do_setBasic(self,name):
        setBasic(self,name)

    def complete_setBasic(self, text, line, begidx, endidx):
        return comp_setBasic(self, text, line, begidx, endidx)
    
    def do_addTemporaryHealth(self,line):
        addTemporaryHealth(self,line)

    def do_clearTemporaryHealth(self,line):
        clearTemporaryHealth(self,line)

    def do_takeDamage(self,line):
        takeDamage(self,line)

    def do_setHealth(self,name):
        setHealth(self,name)

    def complete_setHealth(self, text, line, begidx, endidx):
        return comp_setHealth(self, text, line, begidx, endidx)

    def do_heal(self,line):
        heal(self,line)

    def do_shortRest(self,line):
        shortRest(self,line)

    def do_addHitDice(self,line):
        addHitDice(self,line)
    
    def do_showInventory(self,line):
        showInventory(self,line)

    def do_i(self,line):
        showInventory(self,line)

    def do_addItem(self,name):
        addItem(self,name)

    def complete_addItem(self, text, line, begidx, endidx):
        return comp_addItem(self, text, line, begidx, endidx)

    def do_chuckItem(self,name):
        chuckItem(self,name)

    def complete_chuckItem(self, text, line, begidx, endidx):
        return comp_chuckItem(self, text, line, begidx, endidx)
    
    def do_addFeat(self,line):
        addFeat(self,line)

    def do_showFeats(self,line):
        showFeats(self,line)

    def do_examineFeat(self,line):
        examineFeat(self,line)
    
    def do_ef(self,line):
        examineFeat(self,line)

    def do_examineItem(self,name):
        examineItem(self,name)
    
    def complete_examineItem(self, text, line, begidx, endidx):
        return comp_examineItem(self, text, line, begidx, endidx)

    def do_ei(self,line):
        examineItem(self,line)

    def complete_ei(self,
        text, line, begidx, endidx):
        return comp_examineItem(self, text, line, begidx, endidx)

    def do_addSpell(self,name):
        addSpell(self,name)

    def complete_addSpell(self, text, line, begidx, endidx):
        return comp_addSpell(self, text, line, begidx, endidx)

    def do_showSpellBook(self,line):
        showSpellBook(self,line)

    def do_w(self,line):
        showSpellBook(self,line)

    def do_examineSpell(self,name):
        examineSpell(self,name)

    def complete_examineSpell(self, text, line, begidx, endidx):
        return comp_examineSpell(self, text, line, begidx, endidx)

    def do_chuckSpell(self,name):
        chuckSpell(self,name)

    def complete_chuckSpell(self, text, line, begidx, endidx):
        return comp_chuckSpell(self, text, line, begidx, endidx)

    def do_quit(self, line):
        return True

if __name__ == '__main__':        
     
    CharacterTracker().cmdloop() 
