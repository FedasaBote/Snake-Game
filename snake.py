import pygame
import random
import time
class Snake:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.x = 0
        self.y = 0
        self.width = 20
        self.height = 20
        self.speed = 20
        self.direction = 'right'
        self.score = 0
        self.body = []

    def draw(self):
        for index in range(len(self.body)):
            if(index%2==0):
                pygame.draw.rect(self.screen, self.settings.snake_color_even, pygame.Rect(self.body[index][0], self.body[index][1], self.width, self.height))
            else:
                pygame.draw.rect(self.screen, self.settings.snake_color_odd, pygame.Rect(self.body[index][0], self.body[index][1], self.width, self.height))


    # explain this part of the code
    # self.settings.snake_color
    # self.settings.snake_color
    # this code is used to access the settings class
    # the setting class is used to store all the settings of the game
    # it is used like this let's say you want to access the snake color
    # you can do it like this self.settings.snake_color
    # where does the setting class come from?
    # it is imported from the settings.py file
    # the settings.py file is used to store all the settings of the game
    # self.screen=screen
    # this code is used to access the screen
    # the screen is used to display the game
    # it is used like this let's say you want to access the screen
    # you can do it like this self.screen
    # where does the screen come from?
    # it is imported from the pygame module
    # the pygame module is used to display the game
    # how do i use the pygame to go from here
    

    def change_direction(self, direction):
        if direction == 'right' and self.direction != 'left':
            self.direction = 'right'
        if direction == 'left' and self.direction != 'right':
            self.direction = 'left'
        if direction == 'up' and self.direction != 'down':
            self.direction = 'up'
        if direction == 'down' and self.direction != 'up':
            self.direction = 'down'

    def move(self):

        for i in range(len(self.body)-1,-1,-1):

            if(i==0):
                
                if self.direction == 'right':
                    self.x += self.speed
                if self.direction == 'left':
                    self.x -= self.speed
                if self.direction == 'up':
                    self.y -= self.speed
                if self.direction == 'down':
                    self.y += self.speed

            else:
                prev_x,prev_y=self.body[i-1]
                print(prev_x,prev_y)
                self.body[i]=[prev_x,prev_y]

        if self.body:
            self.body.pop(0)
        self.body.insert(0, [self.x, self.y])
        time.sleep(0.2)

    def eat(self, food):
        if self.x == food.x and self.y == food.y:
            # if self.direction == 'right':
            #     self.x += self.speed
            # if self.direction == 'left':
            #     self.x -= self.speed
            # if self.direction == 'up':
            #     self.y -= self.speed
            # if self.direction == 'down':
            #     self.y += self.speed

            # print(self.body)
            # # Check if the snake's body is empty
            # if not self.body:
            #     self.body.append([self.x, self.y])
            # else:
            
            last_segment = self.body[-1]
            last_x, last_y = last_segment

            new_x = last_x
            new_y = last_y

        
            if self.direction == 'right':
                new_x -= self.speed
            elif self.direction == 'left':
                new_x += self.speed
            elif self.direction == 'up':
                new_y += self.speed
            elif self.direction == 'down':
                new_y -= self.speed

            # Add the new segment to the body
           
        
            self.body.append([new_x, new_y])
            self.score += 1
            # self.x,self.y=new_x,new_y
            food.x = None
            food.y = None
            return True
        return False
  
    def check_collision(self):
        if self.x > self.settings.screen_width - self.width or self.x < 0:
            return True
        if self.y > self.settings.screen_height - self.height or self.y < 0:
            return True
        for i in self.body[1:]:
            if self.x == i[0] and self.y == i[1]:
                return True
        return False

    def reset(self):
        self.x = 0
        self.y = 0
        self.direction = 'right'
        self.body = []
    
    def stop(self):
        self.speed = 0

    def get_body(self):
        return self.body

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.direction

def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))       


class Food:
    def __init__(self, screen, settings, snake):
        self.screen = screen
        self.settings = settings
        self.snake = snake

        self.x = None
        self.y = None
        self.width = 20
        self.height = 20

    def generate_position(self):
        board_width = self.settings.screen_width // self.settings.grid_size
        board_height = self.settings.screen_height // self.settings.grid_size

        valid_positions = []
        for row in range(board_height):
            for col in range(board_width):
                # position = (col * self.settings.grid_size, row * self.settings.grid_size)
                position = (col * self.settings.grid_size, row * self.settings.grid_size)
                
                if not self.check_collision_with_snake(position):
                    valid_positions.append(position)

        if valid_positions:
          
            self.x, self.y = random.choice(valid_positions)
          
            

    def check_collision_with_snake(self, position):
        snake_body = self.snake.get_body()
        for segment in snake_body:
            if segment[0] == position[0] and segment[1] == position[1]:
                return True
        return False

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.food_color, pygame.Rect(self.x, self.y, self.width, self.height))



