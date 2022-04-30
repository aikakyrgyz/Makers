from game import Game
import sys
"""
GameOver:
  - snake hits the wall
  - snake hits itself
Snake Movement:
  - the tail follows the head
Food:
  - its an apple, grows by one
Score:
  - determined by the amount of apples eaten
Menu Screen:
  - shows once in the beginning
  - dissappears on any key press
  - a new game any key press
  - arrow keys change direction
CONSTANTS:
  -color
  - window dimensions
  - size of cells
  - frame rate #-the number of pictures that the program draws per second, many monitors have a frame rate of 60 hertz, or 60 frames per second

  - cell width and height
"""


def main():
  game = Game()
  game.run()
  quit()

if __name__ == '__main__':
    main()

# pygame.init()

# DISPLAYSURF = pygame.display.set_mode((800, 600))
# BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
# CLOCK = pygame.time.Clock()
# pygame.display.set_caption('Змейка')

# while True:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       pygame.quit()
#       sys.exit()
#     elif event.type == pygame.KEYDOWN:
#       if event.key == pygame.K_ESCAPE:
#         pygame.quit()
#         sys.exit()
#   DISPLAYSURF.fill((255, 255, 255)) #white background
#   pygame.display.update()
#   CLOCK.tick(60) #make sure the game runs at the same speed no matter how fast of a computer it runs on


