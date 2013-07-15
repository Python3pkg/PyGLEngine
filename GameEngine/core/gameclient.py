from pyglet import clock, app, window

from GameEngine.api import synthesize
from GameEngine.core import World

class GameClient(window.Window):
    
    def __init__(self):
        super(GameClient, self).__init__(fullscreen=True)
        synthesize(self, 'gameFolder', None)
        synthesize(self, 'gameWorld', None)
        synthesize(self, 'showStats', False)
        
        synthesize(self, 'fps', clock.ClockDisplay())
        
    def setGameWorld(self, value):
        self._gameWorld = value
        clock.schedule(self._gameWorld.update)

    def on_close(self):
        self.dispatch_event('shutdown')
        self.dispatch_pending_events()
        super(GameClient, self).on_close()
        
    def on_draw(self):
        self.clear()
        if self.showStats :
            self.fps.draw()
        
    def run(self):
        self.dispatch_event('init')
        self._gameWorld.init()
        app.run()

GameClient.register_event_type('init')
GameClient.register_event_type('shutdown')