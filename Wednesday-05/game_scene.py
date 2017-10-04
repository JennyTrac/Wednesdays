# Stub created by: Mr. Coxall
# Modified by: Jenny Trac
# Created on: Oct 4 2017
# Created for: ICS3U
# This scene shows the game scene

from scene import *
import ui

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        # pass
        
        CENTRE_OF_SCREEN = self.size / 2
        
        # background colour
        self.background = SpriteNode(position = CENTRE_OF_SCREEN,
                                     color = 'black',
                                     parent = self,
                                     size = self.size)
        
        # show spaceship
        spaceship_position = CENTRE_OF_SCREEN
        spaceship_position.y = 100
        self.spaceship = SpriteNode('./assets/sprites/spaceship.PNG',
                                    parent = self,
                                    position = spaceship_position)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
