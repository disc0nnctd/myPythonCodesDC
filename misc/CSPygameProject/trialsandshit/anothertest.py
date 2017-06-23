import pygame, sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen_r = screen.get_rect()
clock = pygame.time.Clock()
rect = pygame.rect.Rect(0, 0, 50, 50)

# let's start at the center of the screen
rect.center = screen_r.center

# a dict to map keys to a direction
movement = {pygame.K_UP:    ( 0, -1),
            pygame.K_DOWN:  ( 0,  1),
            pygame.K_LEFT:  (-1,  0), 
            pygame.K_RIGHT: ( 1,  0)}

move = (0, 0)

# a simple helper function to apply some "speed" to your movement
def mul10(x):
    return x * 2

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # try getting a direction from our dict
        # if the key is not found, we don't change 'move'
        if e.type == pygame.KEYDOWN:
            move = movement.get(e.key, move)

    # move the rect by using the 'move_ip' function
    # but first, we multiply each value in 'move' with 10
    rect.move_ip(map(mul10, move))

    # ensure that 'rect' is always inside the screen
    rect.clamp_ip(screen_r)
    screen.fill(pygame.color.Color('Black'))
    pygame.draw.rect(screen, pygame.color.Color('White'), rect)
    pygame.display.update()
    clock.tick(60)
