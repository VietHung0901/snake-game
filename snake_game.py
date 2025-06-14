import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
display_width = 800
display_height = 600

# Set block size (snake segment size)
block_size = 20

# Set game speed
snake_speed = 15

# Initialize display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Initialize clock
clock = pygame.time.Clock()

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    """Display the current score on the screen"""
    value = score_font.render("Your Score: " + str(score), True, black)
    game_display.blit(value, [0, 0])

def our_snake(block_size, snake_list):
    """Draw the snake on the screen"""
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])

def message(msg, color):
    """Display a message on the screen"""
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

def game_loop():
    """Main game loop"""
    game_over = False
    game_close = False

    # Initial snake position
    x1 = display_width / 2
    y1 = display_height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # Initialize snake
    snake_list = []
    length_of_snake = 1

    # Generate first food position
    foodx = round(random.randrange(0, display_width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, display_height - block_size) / block_size) * block_size

    while not game_over:

        # Game over screen
        while game_close:
            game_display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = block_size
                    x1_change = 0

        # Check if snake hits the boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        
        # Draw background and food
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [foodx, foody, block_size, block_size])
        
        # Update snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        # Remove extra segments if snake hasn't eaten food
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw snake and score
        our_snake(block_size, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, display_height - block_size) / block_size) * block_size
            length_of_snake += 1

        # Control game speed
        clock.tick(snake_speed)

    # Quit pygame
    pygame.quit()
    quit()

# Start the game
game_loop()
