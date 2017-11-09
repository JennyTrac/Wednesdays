# Stub created by: Mr. Coxall
# Modified by: Jenny Trac
# Created on: Oct 4 2017
# Created for: ICS3U
# This scene shows the game scene

from scene import *
import ui
from numpy import random
from copy import deepcopy

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        # pass
        
        self.SIZE_OF_SCREEN = deepcopy(self.size)
        self.CENTRE_OF_SCREEN = self.size / 2
        self.left_button_down = False
        self.right_button_down = False
        self.ship_move_speed = 20.0
        self.missiles = []
        self.aliens = []
        self.alien_attack_rate = 1
        self.alien_attack_speed = 20.0
        self.scale_size = 0.75
        
        # background colour
        self.background = SpriteNode('./assets/sprites/star_background.PNG',
                                     position = self.CENTRE_OF_SCREEN,
                                     parent = self,
                                     size = self.size)
        
        # show spaceship
        spaceship_position = self.CENTRE_OF_SCREEN
        spaceship_position.y = 100
        self.spaceship = SpriteNode('./assets/sprites/spaceship.PNG',
                                    parent = self,
                                    position = spaceship_position,
                                    scale = self.scale_size)
        
        # show left button
        left_button_position = self.CENTRE_OF_SCREEN
        left_button_position.x = 100
        left_button_position.y = 100
        self.left_button = SpriteNode('./assets/sprites/left_button.PNG',
                                      parent = self,
                                      position = left_button_position,
                                      alpha = 0.5)
        
        # show right button
        right_button_position = self.CENTRE_OF_SCREEN
        right_button_position.x = 300
        right_button_position.y = 100
        self.right_button = SpriteNode('./assets/sprites/right_button.PNG',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.5)
        
        # show red firing button
        fire_button_position = self.size
        fire_button_position.x = fire_button_position.x - 100
        fire_button_position.y = 100
        self.fire_button = SpriteNode('./assets/sprites/red_button.PNG',
                                      parent = self,
                                      position = fire_button_position,
                                      alpha = 0.5)
        
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        # pass
        
        # will move spaceship if button is being held down
        if self.left_button_down == True:
            self.spaceship.run_action(Action.move_by(-1 * self.ship_move_speed, 0.0, 0.1))
        
        if self.right_button_down == True:
            self.spaceship.run_action(Action.move_by(1 * self.ship_move_speed, 0.0, 0.1))
        
        # check if any missile is off the screen
        for missile in self.missiles:
            if missile.position.y > self.SIZE_OF_SCREEN.y - 50:
                missile.remove_from_parent()
                self.missiles.remove(missile)
        
        # check if any alien is off the screen
        for alien in self.aliens:
            if alien.position.y < 150:
                alien.remove_from_parent()
                self.aliens.remove(alien)
        
        # check if any missile is touching any alien
        if len(self.aliens) > 0 and len(self.missiles) > 0:
            for alien in self.aliens:
                for missile in self.missiles:
                    if alien.frame.contains_rect(missile.frame):
                        missile.remove_from_parent()
                        self.missiles.remove(missile)
                        alien.remove_from_parent()
                        self.aliens.remove(alien)
        
        # check if a new alien should be created every update
        alien_create_chance = random.randint(1, 60)
        if alien_create_chance <= self.alien_attack_rate:
            self.add_alien()
        
        # check if alien touches spaceship
        if len(self.aliens) > 0:
            for alien_hit in self.aliens:
                if alien_hit.frame.intersects(self.spaceship.frame):
                    self.spaceship.remove_from_parent()
                    alien_hit.remove_from_parent()
                    self.aliens.remove(alien_hit)
        else:
            pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        # pass
        
        # check if buttons are being held down
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
        
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        # pass
        
        # will stop spaceship from moving if finger is lifted from anywhere on the screen
        self.left_button_down = False
        self.right_button_down = False
        
        # will create new missile when red button is pressed by calling the function
        if self.fire_button.frame.contains_point(touch.location):
            self.create_new_missile()
    
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
    
    def create_new_missile(self):
        # creates new missile every time red button is pressed
        
        missile_start_position = Vector2()
        missile_start_position = self.spaceship.position
        missile_start_position.y = 100
        
        missile_end_position = self.size
        missile_end_position.x = missile_start_position.x
        
        self.missiles.append(SpriteNode('./assets/sprites/missile.PNG',
                             position = missile_start_position,
                             parent = self))
                             
        # make missile go to end of the screen
        missileMoveAction = Action.move_to(missile_end_position.x, 
                                           missile_end_position.y + 0, 
                                           5.0)
        self.missiles[len(self.missiles) - 1].run_action(missileMoveAction)
        
    def add_alien(self):
        # adds new alien to come down
        
        alien_start_position = Vector2()
        alien_start_position = deepcopy(self.SIZE_OF_SCREEN)
        alien_start_position.x = random.randint(100, self.SIZE_OF_SCREEN.x - 100)
        alien_start_position.y = alien_start_position.y + 200
        
        alien_end_position = deepcopy(self.SIZE_OF_SCREEN)
        alien_end_position.x = random.randint(100, self.SIZE_OF_SCREEN.x - 100)
        alien_end_position.y = 100
        
        self.aliens.append(SpriteNode('./assets/sprites/alien.PNG',
                                      position = alien_start_position,
                                      parent = self))
                                      
        # make alien move downward
        alienMoveAction = Action.move_to(alien_end_position.x,
                                         alien_end_position.y,
                                         self.alien_attack_speed,
                                         TIMING_SINODIAL)
        self.aliens[len(self.aliens)-1].run_action(alienMoveAction)
