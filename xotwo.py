import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

square_size = 190

squares=[
    {'start_pos':(0, 0), 'end_position':(190, 190)},
    {'start_pos':(200, 0), 'end_position':(390, 190)},
    {'start_pos':(400, 0), 'end_position':(600, 190)},
    {'start_pos':(0, 200), 'end_position':(190, 390)},
    {'start_pos':(200, 200), 'end_position':(390, 390)},
    {'start_pos':(400, 200), 'end_position':(600, 390)},
    {'start_pos':(0, 400), 'end_position':(190, 600)},
    {'start_pos':(200, 400), 'end_position':(390, 600)},
    {'start_pos':(400, 400), 'end_position':(600, 600)},
]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for square in squares:
        pygame.draw.rect(screen, "white", 
                         (square['start_pos'][0], 
                          square['start_pos'][1], 
                          square_size, square_size))
    # pygame.draw.line(screen, 'red', (200, 200), (400, 200))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()