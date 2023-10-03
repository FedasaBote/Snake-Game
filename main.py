# Import necessary modules
import pygame
from settings import Settings
from snake import Snake
from snake import Food 
from snake import draw_score

# Initialize Pygame
pygame.init()

# Create a game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Create an instance of the Settings class
settings = Settings()



# Create an instance of the Snake class
snake = Snake(screen, settings)
# create the instance of the food class
food=Food(screen,settings,snake)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('up')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('down')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('left')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('right')


    # Render graphics
    
  
    # print(food.x,food.y)
    # Update game state
    if not snake.check_collision():
        snake.move()
        snake.eat(food)
        if(not food.x or not food.y):
            food.generate_position()
       
        
    else:
        snake.stop()
        
        # food.reset()
    
    screen.fill(settings.background_color)
    food.draw()
    snake.draw()
    draw_score(screen, snake.score)
    pygame.display.flip()
    # print(snake.body)
    # snake.body.pop()
# Quit the game
# pygame.quit()