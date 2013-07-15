from GameEngine.api import getSortedByAttr, BitTracker
from GameEngine.core import BaseManager

#------------------------------------------------------------
#------------------------------------------------------------
class SystemBitTracker(BitTracker):
    pass


#------------------------------------------------------------
#------------------------------------------------------------
class SystemManager(BaseManager):
    def __init__(self, *args):
        super(SystemManager, self).__init__(*args)
        
    def addSystem(self, system):
        sys_id = SystemBitTracker.getBit(system)
        self.database[sys_id] = system
        
    def customize(self, system):
        pass 
    
    def update(self, dt):
        #@TODO: There should be parrallization if possible
        for system in getSortedByAttr(self.database.viewvalues(), 'priority') :
            system.process()
