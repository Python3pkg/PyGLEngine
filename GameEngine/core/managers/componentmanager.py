from GameEngine.core import Base, BaseManager
from GameEngine.api import synthesize, BitTracker

#------------------------------------------------------------
#------------------------------------------------------------
class Component(Base):
    pass


#------------------------------------------------------------
#------------------------------------------------------------
class ComponentBitTracker(BitTracker):
    pass


#------------------------------------------------------------
#------------------------------------------------------------
class ComponentManager(BaseManager):
    '''This class manages all the components registered'''
    def __init__(self, *args):
        super(ComponentManager, self).__init__(*args)
        synthesize(self, 'deactivateQueue', set())
        
    def scheduleDeactivate(self, ent_id):
        self.deactivateQueue.add(ent_id)
    
    def update(self, dt):
        for id_tuple in self.deactivateQueue :
            self.deactivateComponent(id_tuple)
        self.deactivateQueue = set()
        
    def addComponent(self, ent_id, comp_inst):
        comp_id = ComponentBitTracker.getBit(comp_inst)
        self.database[ent_id][comp_id] = comp_inst
        return comp_id
    
    def deactivateComponet(self, id_tuple):
        try:
            ent = self.database[id_tuple[0]].pop(id_tuple[1])]
        except KeyError:
            return
    
    def removeComponent(self, ent_id, comp_id):
        self.deactivateQueue.add((ent_id, comp_id))
        
    def removeAllcomponents(self, ent_id):
        components = self.database[ent_id]
        allComponents = zip(self.database.pop(ent_id), components)
        self.deactivateQueue.add(allComponents)
        

