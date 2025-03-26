import pygame

pygame.init()

# Screen size
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
blue = (0, 0, 150)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue_color = (0, 0, 255)

# Current color for drawing
current_color = white

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Drawing options
DRAW_CIRCLE = "circle"
DRAW_RECT = "rectangle"
DRAW_SQUARE = "square"
DRAW_RIGHT_TRIANGLE = "right_triangle"
DRAW_EQUILATERAL_TRIANGLE = "equilateral_triangle"
DRAW_RHOMBUS = "rhombus"
ERASE = "erase"

mode = DRAW_CIRCLE  # Initial mode

def main():
    global current_color  # Declare current_color as a global variable
    running = True
    shapes = []  # List to store shapes
    x, y = 0, 0  # Starting position

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Changing the drawing mode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    mode = DRAW_CIRCLE
                elif event.key == pygame.K_r:
                    mode = DRAW_RECT
                elif event.key == pygame.K_s:
                    mode = DRAW_SQUARE
                elif event.key == pygame.K_q:
                    mode = DRAW_RHOMBUS
                elif event.key == pygame.K_w:
                    mode = DRAW_EQUILATERAL_TRIANGLE
                elif event.key == pygame.K_t:
                    mode = DRAW_RIGHT_TRIANGLE
                elif event.key == pygame.K_e:
                    mode = ERASE
                elif event.key == pygame.K_1:
                    current_color = red
                elif event.key == pygame.K_2:
                    current_color = green
                elif event.key == pygame.K_3:
                    current_color = blue_color

            # Draw shapes when mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mode == DRAW_CIRCLE:
                    shapes.append(("circle", pos, current_color))
                elif mode == DRAW_RECT:
                    shapes.append(("rect", pos, current_color))
                elif mode == DRAW_SQUARE:
                    shapes.append(("square", pos, current_color))
                elif mode == DRAW_RIGHT_TRIANGLE:
                    shapes.append(("right_triangle", pos, current_color))
                elif mode == DRAW_EQUILATERAL_TRIANGLE:
                    shapes.append(("equilateral_triangle", pos, current_color))
                elif mode == DRAW_RHOMBUS:
                    shapes.append(("rhombus", pos, current_color))
                elif mode == ERASE:
                    shapes.append(("erase", pos))

        screen.fill(blue)  # Fill the screen with the background color
        draw_shapes(shapes)  # Draw all the shapes on the screen
        pygame.display.update()  # Update the screen to show changes
    
    pygame.quit()  # Quit pygame

def draw_shapes(shapes):
    for shape in shapes:
        if shape[0] == "circle":
            pygame.draw.circle(screen, shape[2], shape[1], 15)  # Draw circle
        elif shape[0] == "rect":
            pygame.draw.rect(screen, shape[2], (*shape[1], 30, 30))  # Draw rectangle
        elif shape[0] == "square":
            pygame.draw.rect(screen, shape[2], (*shape[1], 30, 30))  # Draw square (same as rectangle, but labeled differently)
        elif shape[0] == "right_triangle":
            # Draw right triangle using pygame.draw.polygon
            points = [(shape[1][0], shape[1][1]), 
                      (shape[1][0] + 40, shape[1][1]), 
                      (shape[1][0], shape[1][1] + 40)]
            pygame.draw.polygon(screen, shape[2], points)
        elif shape[0] == "equilateral_triangle":
            # Draw equilateral triangle
            points = [(shape[1][0], shape[1][1] - 30), 
                      (shape[1][0] - 26, shape[1][1] + 15), 
                      (shape[1][0] + 26, shape[1][1] + 15)]
            pygame.draw.polygon(screen, shape[2], points)
        elif shape[0] == "rhombus":
            # Draw rhombus using pygame.draw.polygon
            points = [(shape[1][0], shape[1][1] - 20), 
                      (shape[1][0] + 20, shape[1][1]), 
                      (shape[1][0], shape[1][1] + 20), 
                      (shape[1][0] - 20, shape[1][1])]
            pygame.draw.polygon(screen, shape[2], points)
        elif shape[0] == "erase":
            pygame.draw.circle(screen, blue, shape[1], 20)  # Clear area by drawing a blue circle (background color)

# Run the main function to start the game
main()
