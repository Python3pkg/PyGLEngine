from PyGLEngine.api import synthesize
from PyGLEngine.core import Base

class Entity(Base):
    def __init__(self, *args):
        super(Entity, self).__init__(*args)
        synthesize(self, 'id', 0)
        synthesize(self, 'componentMask', 0)
        synthesize(self, 'componentCache', {})
        
    def reset(self):
        self.componentMask = 0
        self.componentCache = {}
    
    def __str__(self):
        return "Entity({0})".format(self.id)
    
    def AddComponent(self, comp_inst):
        if not isinstance(component, Component): raise TypeError
        self.world.EntityManager.addComponent(self, component)
        
    def RemoveComponent(self, component):
        if not isinstance(component, Component): raise TypeError
        self.entityManager.RemoveComponent(self, component)

    def GetComponent(self, componentType):
        return self.entityManager.GetComponent(self, componentType)
    def GetComponents(self):
        self.entityManager.GetComponents(self)

    def SetGroup(self, group):
        self.world.GetGroupManager().Set(group, self)
    def SetTag(self, tag):
        self.world.GetTagManager().Register(tag, self)
    def GetTag(self):
        return self.world.GetTagManager().GetTagOfEntity(self)