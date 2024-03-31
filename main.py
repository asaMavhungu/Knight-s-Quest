import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0
FPS = 60

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

board = pygame.image.load("./Assets/board.png")
board = pygame.transform.scale_by(board, 3)

board_rect = board.get_rect()

#ball = pygame.image.load("intro_ball.gif")
#ballrect = ball.get_rect()

while True:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    clock.tick(FPS)

    screen.fill(black)
    screen.blit(board, board_rect)
    pygame.display.flip()