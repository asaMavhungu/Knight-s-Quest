import pygame

from pygame import Surface

class Piece():
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.image: Surface = pygame.image.load(self.path)
        self.pos: tuple = (0,0)
        self.rect = self.image.get_rect()
        self.last_valid_pos: tuple = (0,0)

        

    def scale_by(self, factor: int) -> None:
        old_rect = self.rect.copy()
        self.image = pygame.transform.scale_by(self.image, factor)
        #self.rect.size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.topleft = old_rect.topleft
        #print(self.rect.x)

    def move(self, x, y) -> None:
        self.pos = (x, y)
        self.rect.x, self.rect.y = x, y

    def is_valid_move(self, new_x: int, new_y: int, factor: int) -> bool:
        return False


class Pawn(Piece):
    def __init__(self, pos: tuple) -> None:
        super().__init__("./Assets/pawn.png")
        self.move(pos[0], pos[1])
        #print(pos)

    def is_valid_move(self, new_x: int, new_y: int, factor: int) -> bool:
        old_x, old_y = self.last_valid_pos
        if abs(new_y - old_y)//factor == 1 and old_x - new_x == 0:
            return True
        return False


