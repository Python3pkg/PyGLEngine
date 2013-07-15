from GameEngine.api import synthesize, getClassName, BitTracker
from GameEngine.core import BaseManager

#------------------------------------------------------------
#------------------------------------------------------------
class EntityBitTracker(BitTracker):
    pass

#------------------------------------------------------------
#------------------------------------------------------------
class EntityManager(object):
    REMOVED_COMPONENT_EVENT = "RemovedComponent"
    REMOVED_ENTITY_EVENT    = "RemovedEntity"
    ADDED_COMPONENT_EVENT   = "AddedComponent"
    ADDED_ENTITY_EVENT      = "AddedEntity"

    def __init__(self, *args):
        super(EntityManager, self).__init__(*args)
        
        #List of the avaible entities, so we can reuse them
        synthesize(self, 'entityCache', list())
        #This is the nextId to append to the Entity class name if we need to create a new entity
        #Otherwise we just reuse them
        synthesize(self, 'nextId', 0)
        #This is the bit mask for all the active entities
        synthesize(self, 'entityMask', 0)
        #We don't deactive an entity untill the next update frame
        synthesize(self, 'deactivateQueue', set())

        
        #I'm not entirely sure why this stuff is here?
        #My guess is to eventually support event/signal based changed,
        #something that should be pushed into the base class and have some methods for setting it up, and kicking off events etc
        #or even a custom signal class
        self.events = { EntityManager.REMOVED_COMPONENT_EVENT : [],
                        EntityManager.REMOVED_ENTITY_EVENT : [],
                        EntityManager.ADDED_COMPONENT_EVENT : [],
                        EntityManager.ADDED_ENTITY_EVENT : [] }
        self.RemovedComponentEvent = self.events[EntityManager.REMOVED_COMPONENT_EVENT]
        self.RemovedEntityEvent = self.events[EntityManager.REMOVED_ENTITY_EVENT]
        self.AddedComponentEvent = self.events[EntityManager.ADDED_COMPONENT_EVENT]
        self.AddedEntityEvent = self.events[EntityManager.ADDED_ENTITY_EVENT]
        
    def scheduleDeactivate(self, ent_id):
        self.deactivateQueue.add(ent_id)
    
    def update(self, dt):
        for ent_id in self.deactivateQueue :
            self.deactivateEntity(ent_id)
        self.deactivateQueue = set()

    def addEvent(self, event, *data):
        event = self.events[event]
        event(*data)
            
    def getEntity(self, ent_id):
        return self.database[ent_id]

    def createEntity(self):
        try:
            ent = self.entityCache.pop()
        except IndexError:
            ent = Entity(world=self.world)
            ent_name = getClassName(Entity) + str(self.nextId)
            ent.id = EntityBitTracker.getBit(ent_name)
            self.nextId += 1
        
        self.entityMask += ent.id
        self.database[ent.id] = ent
        self.addEvent(EntityManager.ADDED_ENTITY_EVENT, ent)
        return ent
    
    def deactivateEntity(self, ent_id):
        try:
            ent = self.database.pop(ent_id)
        except KeyError:
            return
        
        self.entityMask -= ent.id
        ent.reset()
        self.entityCache.append(ent)
        self.addEvent(EntityManager.REMOVED_ENTITY_EVENT, ent_id)

    def removeEntity(self, ent_id):
        self.deactivateQueue.update(ent_id)
        
    def removeAllEntities(self):
        self.deactivateQueue.update(self.database.keys())
