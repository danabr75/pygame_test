from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d
)

import pygame
from lib.z_order import ZOrder
from models.spritesheet import Spritesheet
from models.sprite_strip_animator import SpriteStripAnimator

import pathlib



class Player(pygame.sprite.Sprite):
  SPEED  = 0.1
  HEIGHT = 90
  WIDTH  = 65
  IMAGE  = {
    'left': 1,
    'right': 2,
    'up': 3,
    'down': 4
  }

  FPS = 120
  FRAMES = FPS / 12


  def __init__(self, x, y):
    # super(Player, self).__init__()
    # pygame.sprite.Sprite.__init__(self)
    # self.image = pygame.Surface((50, 50))
    # self.image.fill((255, 125, 255))
    # self.rect = self.image.get_rect()
    sprite_sheet_file = str(pathlib.Path(__file__).parent.parent.absolute()) + '/assets/p1_walk.png'
    self.strips = [
        SpriteStripAnimator(sprite_sheet_file, (0,0,self.WIDTH,self.HEIGHT), 3, 1, True, self.FRAMES),
        SpriteStripAnimator(sprite_sheet_file, (0,0,self.WIDTH,self.HEIGHT), 3, 1, True, self.FRAMES),
        SpriteStripAnimator(sprite_sheet_file, (0,0,self.WIDTH,self.HEIGHT), 3, 1, True, self.FRAMES),
        SpriteStripAnimator(sprite_sheet_file, (0,0,self.WIDTH,self.HEIGHT), 3, 1, True, self.FRAMES),
        SpriteStripAnimator(sprite_sheet_file, (0,0,self.WIDTH,self.HEIGHT), 3, 1, True, self.FRAMES),
    ]

    self.current_sprite_n = 0
    self.strips[self.current_sprite_n].iter()
    self.image = self.strips[self.current_sprite_n].next()

    # self.ss = spritesheet.spriteshee('../assets/p1_walk.png')

    # self.image_direction = IMAGE['down']
    # self.image_scale = 0.8

    # self.surf = pygame.Surface((75, 25))
    # self.surf.fill((255, 125, 255))
    # self.rect = self.surf.get_rect()
    self.move_left = False
    self.move_right = False
    self.move_up = False
    self.move_down = False
    self.x = x
    self.y = y
    self.z = ZOrder.Player
    self.clock = pygame.time.Clock()

  def event_update(self, event):
    if event.type == KEYDOWN:
      if event.key == K_w:
        self.move_up = True
      if event.key == K_s:
        self.move_down = True
      if event.key == K_d:
        self.move_right = True
      if event.key == K_a:
        self.move_left = True
    elif event.type == KEYUP:
      if event.key == K_w:
        self.move_up = False
      if event.key == K_s:
        self.move_down = False
      if event.key == K_d:
        self.move_right = False
      if event.key == K_a:
        self.move_left = False


  def update(self):
    is_moving = self.move_left or self.move_right or self.move_up or self.move_down
    if self.move_left:
      self.x -= self.SPEED
    if self.move_right:
      self.x += self.SPEED
    if self.move_up:
      self.y -= self.SPEED
    if self.move_down:
      self.y += self.SPEED

    if is_moving:
      self.current_sprite_n += 1
      if self.current_sprite_n >= len(self.strips):
        self.current_sprite_n = 0
      self.strips[self.current_sprite_n].iter()
      self.image = self.strips[self.current_sprite_n].next()
      print('self.current_sprite_n')
      print(self.current_sprite_n)
      self.clock.tick(self.FPS)

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))
