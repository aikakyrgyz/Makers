from config import Config
from apple import Apple
from snake import Snake
import pygame
import sys

class Game():
  def __init__(self): #constructor
    pygame.init() #starts the game
    self.screen = pygame.display.set_mode((Config.WINDOW_WIDTH,Config.WINDOW_HEIGHT)) #задаем surface(поверхность поверх которой будет все рисоваться и устанавливаем загаловок окна
    self.clock = pygame.time.Clock()
    self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Змейка')
    self.apple = Apple()
    self.snake = Snake()


  def drawGrid(self):
    for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
      pygame.draw.line(self.screen, Config.WHITE, (x, 0), (x, Config.WINDOW_HEIGHT)) #draw vertical lines -> left to right
    for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
      pygame.draw.line(self.screen,Config.WHITE, (0, y), (Config.WINDOW_WIDTH, y)) #draw horizontal lines, top to bottom

  def drawSnake(self):
    for coord in self.snake.snake_coordinates:
          x = coord['x'] * Config.CELLSIZE
          y = coord['y'] * Config.CELLSIZE
          # if x == self.snake.snake_coordinates[self.HEAD]['x'] and y == self.snake.snake_coordinates[self.HEAD]['y']:
          #   snake_coord_fill = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
          #   pygame.draw.rect(self.screen, Config.GREEN, snake_coord_fill)
          #   snake_inner_coord_fill = pygame.Rect(x+2, y+2, Config.CELLSIZE-6, Config.CELLSIZE-6)
          #   pygame.draw.rect(self.screen, Config.GREEN, snake_inner_coord_fill)
          # else:
          snake_coord_fill = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
          pygame.draw.rect(self.screen, Config.PURPLE, snake_coord_fill)
          snake_inner_coord_fill = pygame.Rect(x+2, y+2, Config.CELLSIZE-6, Config.CELLSIZE-6)
          pygame.draw.rect(self.screen, Config.PURPLE, snake_inner_coord_fill)
 
  def drawApple(self):
      x = self.apple.x * Config.CELLSIZE
      y = self.apple.y * Config.CELLSIZE
      appleRect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
      pygame.draw.rect(self.screen, Config.RED, appleRect)
      

  def drawScore(self, score):
      scoreSurf = self.BASICFONT.render(f'Score: {score}', True, Config.WHITE)
      scoreRect = scoreSurf.get_rect()
      scoreRect.topleft = (Config.WINDOW_WIDTH - 120, 10)
      self.screen.blit(scoreSurf, scoreRect)

  def draw(self):
      self.screen.fill(Config.BG_COLOR)
      self.drawGrid()
      self.drawSnake()
      self.drawApple()
      self.drawScore(len(self.snake.snake_coordinates)-3)
      pygame.display.update()
      self.clock.tick(Config.FPS)

  def checkForKeyPress(self):
    if len(pygame.event.get(pygame.QUIT))>0:
        pygame.quit()

    keyUpEvents = pygame.event.get(pygame.KEYUP)

    if len(keyUpEvents) == 0:
        return None

    if keyUpEvents[0].key == pygame.K_ESCAPE:
        pygame.quit()
        quit()

    return keyUpEvents[0].key

  def handleKeyEvents(self, event):
    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.direction!=self.snake.RIGHT:
        self.snake.direction = self.snake.LEFT
    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.direction!=self.snake.LEFT:
        self.snake.direction = self.snake.RIGHT
    elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.direction!=self.snake.DOWN:
        self.snake.direction = self.snake.UP
    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.direction!=self.snake.UP:
        self.snake.direction = self.snake.DOWN
    elif event.key == pygame.K_ESCAPE:
        pygame.quit()

  def resetGame(self):
      del self.snake
      del self.apple
      self.snake = Snake()
      self.apple = Apple()
      return True
 
  def displayGameOver(self):
      gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
      gameSurf = gameOverFont.render('Game', True, Config.WHITE)
      overSurf = gameOverFont.render('Over', True, Config.WHITE)
      gameRect = gameSurf.get_rect()
      overRect = overSurf.get_rect()
      gameRect.midtop = (Config.WINDOW_WIDTH/2, 10)
      overRect.midtop = (Config.WINDOW_WIDTH/2, gameRect.height + 10 + 25)
      self.screen.blit(gameSurf, gameRect)
      self.screen.blit(overSurf, overRect)

      #self.drawPressKeyMsg()
      pygame.display.update()
      pygame.time.wait(500)

      self.checkForKeyPress() #clear out any key presses in the event queue
      while True:
          if self.checkForKeyPress():
              pygame.event.get() #clear event queue
              return

  def isGameOver(self):
    if(self.snake.snake_coordinates[self.snake.HEAD]['x']==-1 or self.snake.snake_coordinates[self.snake.HEAD]['x'] == Config.CELLWIDTH or self.snake.snake_coordinates[self.snake.HEAD]['y'] == -1 or self.snake.snake_coordinates[self.snake.HEAD]['y'] == Config.CELLHEIGHT):
        return self.resetGame()
    for snake_segment in self.snake.snake_coordinates[1:]:
        if snake_segment['x'] == self.snake.snake_coordinates[self.snake.HEAD]['x'] and snake_segment['y'] == self.snake.snake_coordinates[self.snake.HEAD]['y']:
            return self.resetGame()




  def run(self):
      #self.showStartScreen
      while True:
          self.gameLoop()
          self.displayGameOver()

  def gameLoop(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        elif event.type == pygame.KEYDOWN:
          self.handleKeyEvents(event) #if any other key is pressed
      self.snake.update(self.apple)
      self.draw()
      if self.isGameOver():
        break
        


      #self.screen.fill((255, 255, 255)) #white background
      #pygame.display.update()
      #self.clock.tick(60) #make sure the game runs at the same speed no matter how fast of a computer it runs on

