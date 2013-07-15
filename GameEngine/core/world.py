from operator import attrgetter

from GameEngine.api import synthesize, getClassName, getSortedByAttr
from GameEngine.core import SystemManager, EntityManager, TagManager, GroupManager

#------------------------------------------------------------
#------------------------------------------------------------
class World(object):
    '''The main class the represents the game world simulation'''
    #------------------------------------------------------------
    def __init__(self):
        synthesize(self, 'managersMap', {})
        synthesize(self, 'Delta', 0)
        
        #This should get moved a configuration somehow
        self.addManager(TagManager)
        self.addManager(GroupManager)
        self.addManager(SystemManager)
        self.addManager(EntityManager)
        
    def addManager(self, manager, priority=0):
        manager_name = getClassName(manager)
        if manager_name not in self.managersMap.keys():
            manager_cls = manager(priority=priority, world=self)
            self.managersMap[manager_name] = manager_cls
        
    def getManager(self, manager_name):
        return self.managersMap.get(manager_name)
    
    def init(self):
        for manager in getSortedByAttr(self.managerMap.values(), 'priorty'):
            manager.init()
        self.start()
    
    def start(self):
        for manager in getSortedByAttr(self.managerMap.values(), 'priorty'):
            manager.start()
    
    def stop(self):
        for manager in getSortedByAttr(self.managerMap.values(), 'priorty'):
            manager.stop()
    
    def update(self, dt):
        self.setDelta(dt)
        for manager in getSortedByAttr(self.managerMap.values(), 'priorty'):
            manager.update(dt)
        