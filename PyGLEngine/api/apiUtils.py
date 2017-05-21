import types
import copy
from operator import attrgetter, itemgetter

#------------------------------------------------------------
def getClassName(x):
    if not isinstance(x, str):
        if type(x) in [types.FunctionType, type, types.ModuleType] :
            return x.__name__
        else:
            return x.__class__.__name__
    else:
        return x
    
#------------------------------------------------------------
def getSortedByAttr(obj_list, key_name):
    return sorted(obj_list, key=attrgetter(key_name))

#------------------------------------------------------------
def getSortedByItem(obj_list, item_index):
    return sorted(obj_list, key=itemgetter(item_index))

#------------------------------------------------------------
def synthesize(inst, name, value, readonly=False):
    """
    Convenience method to create getters, setters and a property for the instance.
    Should the instance already have the getters or setters defined this won't add them
    and the property will reference the already defined getters and setters
    Should be called from within __init__. Creates [name], get[Name], set[Name], 
    _[name] on inst.

    :param inst: An instance of the class to add the methods to.
    :param name: The base name to build the function names, and storage variable.
    :param value: The initial state of the created variable.

    """
    cls = type(inst)
    storageName = '_{0}'.format(name)
    getterName = 'get{0}{1}'.format(name[0].capitalize(), name[1:])
    setterName = 'set{0}{1}'.format(name[0].capitalize(), name[1:])
    deleterName = 'del{0}{1}'.format(name[0].capitalize(), name[1:])

    setattr(inst, storageName, value)
    
    #We always define the getter
    def customGetter(self):
        return getattr(self, storageName)

    #Add the Getter
    if not hasattr(inst, getterName):
        setattr(cls, getterName, customGetter)
    
    #Handle Read Only
    if readonly :
        if not hasattr(inst, name):
            setattr(cls, name, property(fget=getattr(cls, getterName, None) or customGetter, fdel=getattr(cls, getterName, None)))
    else:
        #We only define the setter if we arn't read only
        def customSetter(self, state):
            setattr(self, storageName, state)        
        if not hasattr(inst, setterName):
            setattr(cls, setterName, customSetter)
        member = None
        if hasattr(cls, name):
            #we need to try to update the property fget, fset, fdel incase the class has defined its own custom functions
            member = getattr(cls, name)
            if not isinstance(member, property):
                raise ValueError('Member "{0}" for class "{1}" exists and is not a property.'.format(name, cls.__name__))
        #Reguardless if the class has the property or not we still try to set it wit
        setattr(cls, name, property(fget=getattr(member, 'fget', None) or getattr(cls, getterName, None) or customGetter,
                                    fset=getattr(member, 'fset', None) or getattr(cls, setterName, None) or customSetter,
                                    fdel=getattr(member, 'fdel', None) or getattr(cls, getterName, None)))

#------------------------------------------------------------
def Enum(*enumerated):
    enums = dict(list(zip(enumerated, list(range(len(enumerated))))))
    enums["names"] = enumerated
    return type('Enum', (), enums)


#------------------------------------------------------------        
#------------------------------------------------------------
class BitTracker(object):
    '''A Management class that keeps a map of strings to bit values and bit indexes
    The BitTracker keeps a cache that maps a string(key) to a BitMask(value)
    The BitTracker has convience functions for getBit and getId and handles all the internal machinery
    '''
    bitMask = 1 #Bit Cache
    bitCacheMap = {}
    _hasInit = False
    
    @classmethod
    def increment(cls):
        cls.bitMask <<= 1
        
    @classmethod
    def reset(cls):
        cls.bitMask = BitMask()
        cls.bitCacheMap = {}
    
    @classmethod
    def getBit(cls, name):
        name = getClassName(name)
        try:
            bit = cls.bitCacheMap[name]
        except KeyError :
            bit = cls.bitMask
            cls.bitCacheMap[name] = bit
            cls.increment()
        
        return bit
