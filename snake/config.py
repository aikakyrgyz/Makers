import pygame
class Config():
  FPS = 15#9
  #MENU_FPS = 60 #basic FPS
  WINDOW_WIDTH = 640
  WINDOW_HEIGHT = 480
  CELLSIZE = 20 #the cell is a square
  assert WINDOW_WIDTH % CELLSIZE ==0, 'Window width must be a multiple of the cell size'
  assert WINDOW_HEIGHT %CELLSIZE ==0, 'Window height must be a multiple of the cell size'
  CELLWIDTH = int(WINDOW_WIDTH/CELLSIZE)
  CELLHEIGHT = int(WINDOW_HEIGHT/CELLSIZE)

  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLUE = (0, 255, 255)
  PURPLE = (204, 153, 255)
  LIGHT_BLUE = (153, 204, 255)
  DARK_PURPLE = (153, 51, 255)
  BG_COLOR = BLACK
  