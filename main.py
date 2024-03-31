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

pawn = pygame.image.load("./Assets/pawn.png")
pawn = pygame.transform.scale_by(pawn, 3)

board_rect = board.get_rect()
pawn_rect = pawn.get_rect()

#ball = pygame.image.load("intro_ball.gif")
#ballrect = ball.get_rect()

dragging = False

while True:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and pawn_rect.collidepoint(event.pos):
                dragging = True
                offset_x = event.pos[0] - pawn_rect.x
                offset_y = event.pos[1] - pawn_rect.y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False

        if dragging:
            mouse_x , mouse_y = pygame.mouse.get_pos()
            pawn_rect.x = mouse_x - offset_x
            pawn_rect.y = mouse_y - offset_y

    clock.tick(FPS)

    screen.fill(black)
    screen.blit(board, board_rect)
    screen.blit(pawn, pawn_rect)
    pygame.display.flip()