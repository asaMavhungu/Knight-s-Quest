import sys, pygame
from Scripts.board import Board
from Scripts.piece import Piece, Pawn

black = (0, 0, 0)

class Game:
    def __init__(self) -> None:
        pygame.init()

        size = width, height = 640, 480
        
        self.FPS = 60
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.board : Board = Board("./Assets/board.png")
        self.board.scale_by(3)

        self.pieces : list[Piece] = []

        for i in range(8):
            for j in range(8):
                piece_symbol = self.board.chessboard[i, j]
                if piece_symbol != '_':
                    x, y = (j+1)*48, (i+1)*48
                    piece = Pawn((x,y))
                    piece.scale_by(3)
                    piece.last_valid_pos = (x, y)
                    self.pieces.append(piece)

        
    def run(self):
                

        dragging : bool = False

        current_piece : Piece | None = None

        while True:

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()



                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for piece in self.pieces:
                        if event.button == 1 and piece.rect.collidepoint(event.pos):
                            dragging = True
                            current_piece = piece
                            offset_x = event.pos[0] - piece.rect.x
                            offset_y = event.pos[1] - piece.rect.y

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and dragging:
                        dragging = False
                        x, y = ((current_piece.rect.x+offset_x)//48)*48, ((current_piece.rect.y+offset_y)//48)*48
                        if current_piece.is_valid_move(x, y, 48):
                            print("valid")
                            current_piece.move(x, y)
                            current_piece.last_valid_pos = x, y
                        else:
                            print("invalid")
                            prev_x, prev_y = current_piece.last_valid_pos
                            current_piece.move(prev_x, prev_y)
                        #print(current_piece.is_valid_move(x, y, 48))
                        current_piece = None
                            


                if dragging:
                    mouse_x , mouse_y = pygame.mouse.get_pos()
                    x = mouse_x - offset_x
                    y = mouse_y - offset_y
                    current_piece.move(x , y)


            self.clock.tick(self.FPS)

            self.screen.fill(black)

            self.screen.blit(self.board.image, (0, 0))  # Blit the board image onto the screen

            for piece in self.pieces:
                self.screen.blit(piece.image, piece.pos)
                
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()