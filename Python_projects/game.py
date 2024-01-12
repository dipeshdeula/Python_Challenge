# import pygame

# screen_size=[600,900]
# pygame.display.set_mode(screen_size)
# background=pygame.image.load('home.png')

# screen_size.blit(background,(0,0))


import pygame

screen_size=[600,900]
pygame.display.set_mode(screen_size)

background=pygame.image.load('home.png')

# The game loop
running = True
while running:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False

    # Drawing the background image
    screen.blit(background, [0, 0])
    pygame.display.update()

    # Updating the display
    pygame.display.flip()

pygame.quit()