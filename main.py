import pygame as pg
import random as rand
from settings import *
from sprites import *

class Game:

  def __init__(self):
    pg.init()
    pg.mixer.init() # Initializes mixer for sound
    self.screen = pg.display.set_mode((WIDTH,HEIGHT))
    pg.display.set_caption("Game Title")
    self.clock = pg.time.Clock()
    self.running = True


  def run(self):
    # Game loop
    self.playing = True
    while self.playing:
      self.clock.tick(FPS)
      self.events()
      self.update()
      self.draw()

  def new(self):
    self.all_sprites = pg.sprite.Group()
    self.platforms = pg.sprite.Group()
    self.player = Player(self)
    self.all_sprites.add(self.player)
    platform1 = Platform(0, HEIGHT-40, WIDTH, 40)
    self.all_sprites.add(platform1)
    self.platforms.add(platform1)
    platform2 = Platform(WIDTH/2 - 50, HEIGHT * 3/4, 100, 20)
    self.all_sprites.add(platform2)
    self.platforms.add(platform2)
    self.run()

  def events(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        self.playing = False
        self.running = False
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE:
          self.player.jump()

  def update(self):
    self.all_sprites.update()
    hits = pg.sprite.spritecollide(self.player,self.platforms, False)
    if hits:
      self.player.pos.y = hits[0].rect.top + 1 #+1 added to keep from bouncing incessantly
      self.player.vel.y = 0


  def draw(self):
    self.screen.fill(BLACK)
    self.all_sprites.draw(self.screen)

    pg.display.flip()

  def show_start_screen(self):
    pass

  def show_go_screen(self):
    pass

g = Game()
g.show_start_screen()

while g.running:
  g.new()
  g.show_go_screen()

pg.quit()