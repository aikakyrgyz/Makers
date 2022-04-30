import random # for the Apple
from config import Config

class Apple():
  def __init__(self):
    self.set_new_location()
  def set_new_location(self):
    self.x = random.randint(0, Config.CELLWIDTH - 1) #x coordinate #32-1
    self.y = random.randint(0, Config.CELLHEIGHT - 1)
    #y coordinate



