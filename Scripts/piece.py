import pygame

from pygame import Surface

class Piece():
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.image: Surface = pygame.image.load(self.path)
        self.pos: tuple = (0,0)
        self.rect = self.image.get_rect()
        

    def scale_by(self, factor: int) -> None:
        old_rect = self.rect.copy()
        self.image = pygame.transform.scale_by(self.image, factor)
        #self.rect.size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.topleft = old_rect.topleft
        print(self.rect.x)

    def move(self, x, y) -> None:
        self.pos = (x, y)
        self.rect.x, self.rect.y = x, y


class Pawn(Piece):
    def __init__(self, pos: tuple) -> None:
        super().__init__("./Assets/pawn.png")
        self.move(pos[0], pos[1])
        print(pos)


