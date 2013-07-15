from GameEngine.api import synthesize, getSortedByAttr, getClassName

#------------------------------------------------------------
#------------------------------------------------------------
class Base(object):
    '''The base object almost everything should inherit from'''
    def __init__(self, world=None):
        synthesize(self, 'world', world)
        
    def init(self):
        pass
    
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def update(self, dt):
        pass

#------------------------------------------------------------
#------------------------------------------------------------
class BaseSystem(Base):
    '''The base class that handles processing objects during the update loop'''
    def __init__(self, priority=0, aysnc=False, *args):
        super(BaseSystem, self).__init__(*args)
        synthesize(self, 'priority', priority)
        synthesize(self, 'async', aysnc)


#------------------------------------------------------------
#------------------------------------------------------------
class BaseFactory(Base):
    '''The base class that handles generating objects from data'''
    def __init__(self, *args):
        super(BaseFactory, self).__init__(*args)


#------------------------------------------------------------
#------------------------------------------------------------
class BaseManager(Base):
    '''The base class that manages objects'''
    def __init__(self, priority=0, *args):
        super(BaseManager, self).__init__(*args)
        synthesize(self, 'priority', priority)
        synthesize(self, 'database', {})
    
    def __getattr__(self, name):
        try:
            return self.database[name]
        except:
            raise AttributeError
        
    def remove(self, key):
        self.database.pop(key)
        
    def exists(self, key):
        return key in self.database
    

