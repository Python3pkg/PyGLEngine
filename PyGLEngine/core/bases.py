from PyGLEngine.api import synthesize, getSortedByAttr, getClassName

#------------------------------------------------------------
#------------------------------------------------------------
class Base(object):
    '''The base object almost everything should inherit from'''
    def __init__(self, priority=0, world=None):
        synthesize(self, 'world', world)
        synthesize(self, 'priority', priority)
        synthesize(self, 'database', {})
        
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
class BaseFactory(Base):
    '''The base class that handles generating objects from data'''
    def __init__(self, **kwds):
        super(BaseFactory, self).__init__(**kwds)


#------------------------------------------------------------
#------------------------------------------------------------
class BaseManager(Base):
    '''The base class that manages objects'''
    def __init__(self, **kwds):
        super(BaseManager, self).__init__(**kwds)
    
    def __getattr__(self, name):
        try:
            return self.database[name]
        except:
            raise AttributeError
        
    def remove(self, key):
        self.database.pop(key)
        
    def exists(self, key):
        return key in self.database
    

