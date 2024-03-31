import sys, pygame
from Scripts.board import Board

black = (0, 0, 0)

class Game:
    def __init__(self) -> None:
        pygame.init()

        size = width, height = 640, 480
        
        self.FPS = 60
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.board = Board("./Assets/board.png")
        self.board.scale_by(3)

        
    def run(self):
                

        #ball = pygame.image.load("intro_ball.gif")
        #ballrect = ball.get_rect()

        dragging = False

        while True:

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()


            self.clock.tick(self.FPS)

            self.screen.fill(black)

            self.screen.blit(self.board.image, (0, 0))  # Blit the board image onto the screen
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()