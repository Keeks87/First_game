# importing the Pygame library

import pygame

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

background_color = (0, 0, 0)
screen.fill(background_color)

pygame.display.set_caption("My Game")

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # game logic goes here

    screen.fill(background_color)

    # draw game objects onto the screen here

    pygame.display.flip()

'''
You have successfully imported the Pygame library, initialized it, set up the game window with a specified
size, background color, and title, and updated the display.

You also included a while loop that continually checks for the quit event and updates the display. You can
add your game logic inside the loop and draw game objects onto the screen.

Make sure to import the necessary libraries and modules for your game logic, define your game objects and 
their properties, and include the necessary functions to control the game's behavior.
'''