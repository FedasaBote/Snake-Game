# let's set settings for snake class here and import this file in snake file


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.background_color = (0, 0, 0)  # Black

        # Snake settings
        self.snake_color_odd = (0, 255, 255)  # Green
        self.snake_color_even=(0,255,0)
        self.snake_speed = 1

        # Food settings
        self.food_color = (0, 255, 25)  # Red
        # self.food_size=20

        # Other settings
        self.grid_size = 20

