from time import time, sleep
from pyglet import clock, app, window

from PyGLEngine.api import synthesize
from PyGLEngine.core import World       

class _GameClient(window.Window):
    
    def __init__(self):
        super(_GameClient, self).__init__(fullscreen=True)
        synthesize(self, 'gameFolder', None)
        synthesize(self, 'gameWorld', None)
        synthesize(self, 'showStats', False)
        synthesize(self, 'isAlive', True)
        
        synthesize(self, 'fps', clock.ClockDisplay(), True)
        
    def setGameWorld(self, value):
        self._gameWorld = value
        clock.schedule_interval(self._gameWorld.update, 0.1)

    def on_close(self):
        self.isAlive = 0
        self.dispatch_event('shutdown')
        self.dispatch_pending_events()
        super(_GameClient, self).on_close()
        
    def on_draw(self):
        self.clear()
        if self.showStats :
            self.fps.draw()
        
    def run(self):
        self.dispatch_event('init')
        self.dispatch_pending_events()
        self.gameWorld.init()
        app.run()
        

_GameClient.register_event_type('init')
_GameClient.register_event_type('shutdown')

GameClient = _GameClient()


