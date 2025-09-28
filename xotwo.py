import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Roboto", 50) 
running = True

square_size = 190

squares=[
    {'start_pos':(0, 0), 'end_pos':(190, 190), 'x_checked':False, 'o_checked': False},
    {'start_pos':(200, 0), 'end_pos':(390, 190), 'x_checked':False, 'o_checked': False},
    {'start_pos':(400, 0), 'end_pos':(600, 190), 'x_checked':False, 'o_checked': False},
    {'start_pos':(0, 200), 'end_pos':(190, 390), 'x_checked':False, 'o_checked': False},
    {'start_pos':(200, 200), 'end_pos':(390, 390), 'x_checked':False, 'o_checked': False},
    {'start_pos':(400, 200), 'end_pos':(600, 390), 'x_checked':False, 'o_checked': False},
    {'start_pos':(0, 400), 'end_pos':(190, 600), 'x_checked':False, 'o_checked': False},
    {'start_pos':(200, 400), 'end_pos':(390, 600), 'x_checked':False, 'o_checked': False},
    {'start_pos':(400, 400), 'end_pos':(600, 600), 'x_checked':False, 'o_checked': False},
]
player="x_checked"
wins= [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
is_paused=False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for square in squares:
                if (not is_paused) and square['start_pos'][0]<pygame.mouse.get_pos()[0]<square['end_pos'][0] and square['start_pos'][1]<pygame.mouse.get_pos()[1]<square['end_pos'][1]:
                    square[player]=True
                    print(square)
                    if player=='x_checked':
                        player='o_checked'
                    else:
                        player='x_checked'
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for square in squares:
        pygame.draw.rect(screen, "white", 
                         (square['start_pos'][0], 
                          square['start_pos'][1], 
                          square_size, square_size))
        if square['x_checked']:
            pygame.draw.line(screen, 'red', 
                             square['start_pos'], 
                             square['end_pos'], 10)
            pygame.draw.line(screen, 'red', 
                             (square['end_pos'][0], 
                              square['start_pos'][1]), 
                              (square['start_pos'][0], 
                               square['end_pos'][1]), 10)
        
        if square['o_checked']:
            pygame.draw.circle(screen, 'blue', 
                               (square['start_pos'][0]+square_size/2, 
                                square['start_pos'][1]+square_size/2), 90)
            pygame.draw.circle(screen, 'white', (square['start_pos'][0]+square_size/2, square['start_pos'][1]+square_size/2), 80)
    
    for win in wins:
        if (squares[win[0]]['x_checked'] and squares[win[1]]['x_checked'] and squares[win[2]]['x_checked']) or (squares[win[0]]['o_checked'] and squares[win[1]]['o_checked'] and squares[win[2]]['o_checked']):
            is_paused=True
            text_surface = font.render("X Has Won" if player=='o_checked' else "O Has Won", True, 'red') 
            screen.blit(text_surface, (200, 250))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    

pygame.quit()