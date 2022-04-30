from config import Config
from apple import Apple
import random

class Snake():
  RIGHT = 'right'
  LEFT = 'left'
  UP = 'up'
  DOWN = 'down'
  HEAD = 0

  def __init__(self):
    self.x = random.randint(5, Config.CELLWIDTH - 1)
    self.y = random.randint(5, Config.CELLHEIGHT - 1)
    self.direction = self.RIGHT
    self.snake_coordinates = [{'x': self.x, 'y': self.y}, {'x': self.x -1, 'y': self.y}, {'x': self.x -2, 'y': self.y}]
  def update(self, apple):
    #check if the snake have eaten an apple:
    if self.snake_coordinates[self.HEAD]['x'] == apple.x and self.snake_coordinates[self.HEAD]['y'] == apple.y:
        apple.set_new_location()
    else:
        del self.snake_coordinates[-1] #remove the tail
    #move the snake by adding a square in the beginning of the head in the direction it is moving
    if self.direction ==self.UP:
        new_head = {'x': self.snake_coordinates[self.HEAD]['x'], 'y':self.snake_coordinates[self.HEAD]['y']-1}
    elif self.direction == self.DOWN:
        new_head = {'x':self.snake_coordinates[self.HEAD]['x'], 'y':self.snake_coordinates[self.HEAD]['y']+1}
    elif self.direction == self.LEFT:
        new_head = {'x':self.snake_coordinates[self.HEAD]['x']-1, 'y':self.snake_coordinates[self.HEAD]['y']}
    elif self.direction == self.RIGHT:
        new_head ={'x':self.snake_coordinates[self.HEAD]['x']+1, 'y':self.snake_coordinates[self.HEAD]['y']}

    self.snake_coordinates.insert(0, new_head) #inserting the head



