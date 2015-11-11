import cmd
import sys
sys.path.insert(1,'source/')
from character import *
from commands import *
from commands_vitality import *
from commands_stats import *
from commands_inventory import *
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

    def do_addFeat(self,line):
        addFeat(self,line)

    def do_createCharacter(self,line):
        createCharacter(self,line)

    def do_spellBook(self,line):
        spellBook(self,line)

    def do_addSpell(self,line):
        addSpell(self,line)

    def do_showEquipped(self,line):
        showEquipped(self,line)

    def do_updateCombat(self,line):
        updateCombat(self,line)

    def do_updateSkills(self,line):
        updateSkills(self,line)
    
    def do_changeSkillProficiencies(self,line):
        changeSkillProficiencies(self,line)
    
    def do_changeBasic(self,name):
        changeBasic(self,name)

    def complete_changeBasic(self, text, line, begidx, endidx):
        return comp_changeBasic(self, text, line, begidx, endidx)

    def do_takeDamage(self,damage):
        takeDamage(self,damage)

    def do_addTemporaryHealth(self,points):
        addTemporaryHealth(self,points)

    def do_clearTemporaryHealth(self,points):
        clearTemporaryHealth(self,points)
    
    def do_heal(self,points):
        heal(self,points)
    
    def do_setMaxHitPoints(self,points):
        setMaxHitPoints(self,points)
    
    def do_restShort(self,number):
        restShort(self,number)

    def do_addHitDice(self,number):
        addHitDice(self,number)

    def do_restExtended(self,line):
        restExtended(self)

    def do_quit(self, line):
        return True

if __name__ == '__main__':        
     
    CharacterTracker().cmdloop() 
