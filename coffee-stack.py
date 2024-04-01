import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Coffee Stack")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the coffee stack
stack_width = 100
stack_height = 20
stack_x = window_width // 2 - stack_width // 2
stack_y = window_height - stack_height
stack_speed = 5

# Set up the coffee cup
cup_width = 50
cup_height = 80
cup_x = stack_x + stack_width // 2 - cup_width // 2
cup_y = stack_y - cup_height
cup_speed = 5

# Set up the coffee beans
bean_width = 20
bean_height = 20
bean_x = random.randint(0, window_width - bean_width)
bean_y = 0
bean_speed = 3

# Game loop
running = True
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Move the coffee stack
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and stack_x > 0:
    stack_x -= stack_speed
  if keys[pygame.K_RIGHT] and stack_x < window_width - stack_width:
    stack_x += stack_speed

  # Move the coffee cup with the stack
  cup_x = stack_x + stack_width // 2 - cup_width // 2

  # Move the coffee beans
  bean_y += bean_speed

  # Check for collision between the cup and the beans
  if cup_x < bean_x + bean_width and cup_x + cup_width > bean_x and cup_y < bean_y + bean_height and cup_y + cup_height > bean_y:
    # Collision occurred, increase score or perform other actions

  # Update the display
    window.fill(BLACK)
  pygame.draw.rect(window, WHITE, (stack_x, stack_y, stack_width, stack_height))
  pygame.draw.rect(window, WHITE, (cup_x, cup_y, cup_width, cup_height))
  pygame.draw.rect(window, WHITE, (bean_x, bean_y, bean_width, bean_height))
  pygame.display.update()

# Quit the game
pygame.quit()