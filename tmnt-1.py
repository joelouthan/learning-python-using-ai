import pygame

# Initialize pygame
pygame.init()

# Set up the game window
screen_width = 1900
screen_height = 1024
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TMNT Game")

# Load images
background_image = pygame.image.load("background.gif")
turtle_image = pygame.image.load("turtle.png")
shredder_image = pygame.image.load("shredder.webp")
bebop_image = pygame.image.load("bebop.webp")
rocksteady_image = pygame.image.load("rocksteady.webp")

# Set initial positions
turtle_x = 100
turtle_y = 300
shredder_x = 600
shredder_y = 300
bebop_x = 400
bebop_y = 200
rocksteady_x = 400
rocksteady_y = 400

# Game loop
running = True
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Update game logic

  # Draw background
  screen.blit(background_image, (0, 0))

  # Draw characters
  screen.blit(turtle_image, (turtle_x, turtle_y))
  screen.blit(shredder_image, (shredder_x, shredder_y))
  screen.blit(bebop_image, (bebop_x, bebop_y))
  screen.blit(rocksteady_image, (rocksteady_x, rocksteady_y))

  # Update display
  pygame.display.flip()

# Quit the game
pygame.quit()