from PyGLEngine.core import BaseManager

#------------------------------------------------------------
#------------------------------------------------------------
class TagManager(BaseManager):
    def __init__(self, *args):
        super(TagManager, self).__init__(*args)

    def addTag(self, tag, value):
        self.database[tag] = value
    
    def getValueByTag(self, tag):
        return self.database.get(tag)
    
    def getTagsByValue(self, value):
        try:
            return [k for k, v in self.database.items() if v == value]
        except :
            return ''
