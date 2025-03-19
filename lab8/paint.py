import pygame

pygame.init()

# Screen size
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# colors
blue = (0, 0, 150)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue_color = (0, 0, 255)

# current color
current_color = white

clock = pygame.time.Clock()

# drawing options
DRAW_CIRCLE = "circle"
DRAW_RECT = "rectangle"
ERASE = "erase"

mode = DRAW_CIRCLE  # main screen

def main():
    running = True
    shapes = []
    x, y = 0, 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Changing the option
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    mode = DRAW_CIRCLE
                elif event.key == pygame.K_r:
                    mode = DRAW_RECT
                elif event.key == pygame.K_e:
                    mode = ERASE
                elif event.key == pygame.K_1:
                    current_color = red
                elif event.key == pygame.K_2:
                    current_color = green
                elif event.key == pygame.K_3:
                    current_color = blue_color
            
            # draw with mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if mode == DRAW_CIRCLE:
                    shapes.append(("circle", pos, current_color))
                elif mode == DRAW_RECT:
                    shapes.append(("rect", pos, current_color))
                elif mode == ERASE:
                    shapes.append(("erase", pos))

        screen.fill(blue)
        draw_shapes(shapes)
        pygame.display.update()
    
    pygame.quit()

def draw_shapes(shapes):
    for shape in shapes:
        if shape[0] == "circle":
            pygame.draw.circle(screen, shape[2], shape[1], 15)
        elif shape[0] == "rect":
            pygame.draw.rect(screen, shape[2], (*shape[1], 30, 30))
        elif shape[0] == "erase":
            pygame.draw.circle(screen, blue, shape[1], 20)  # clear

main()
