import pygame
import random

# Define colors
blue = (50, 153, 213)
black = (0, 0, 0)
red = (213, 50, 80)
white = (255, 255, 255)

dis_width = 600
dis_height = 400
snake_block = 10

# Initialize pygame
pygame.init()

display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game with Levels")
clock = pygame.time.Clock()

# Function to generate random food position
def generate_food(snake_list):
    while True:
        food_x = random.randint(0, (dis_width // snake_block) - 1) * snake_block
        food_y = random.randint(0, (dis_height // snake_block) - 1) * snake_block
        if [food_x, food_y] not in snake_list:  # Ensure food does not overlap with the snake
            return food_x, food_y

# Main game function
def main():
    game_over = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    
    snake_list = []
    snake_length = 1  # Start with one block
    food_x, food_y = generate_food(snake_list)
    
    score = 0
    level = 1
    speed = 10  # Initial speed
    
    while not game_over:
        display.fill(blue)
        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0
        
        # Update snake position
        x1 += x1_change
        y1 += y1_change
        
        # Check wall collision
        if x1 < 0 or x1 >= dis_width or y1 < 0 or y1 >= dis_height:
            game_over = True
        
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        # Check self-collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True
        
        # Check if food is eaten
        if x1 == food_x and y1 == food_y:
            food_x, food_y = generate_food(snake_list)
            snake_length += 1
            score += 1
            
            # Level up every 3 points
            if score % 3 == 0:
                level += 1
                speed += 2  # Increase speed
        
        print_snake(snake_block, snake_list)
        show_score(score, level)
        pygame.display.update()
        clock.tick(speed)  # Adjust speed dynamically
    
    pygame.quit()

# Function to draw the snake
def print_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

# Function to display score and level
def show_score(score, level):
    font = pygame.font.SysFont("bahnschrift", 20)
    score_text = font.render(f"Score: {score}  Level: {level}", True, white)
    display.blit(score_text, [10, 10])

main()
