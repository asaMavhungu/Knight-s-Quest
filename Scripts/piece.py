import pygame

from pygame import Surface

class Piece():
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.image: Surface = pygame.image.load(self.path)
        self.pos: tuple = (0,0)
        self.rect = self.image.get_rect()
        

    def scale_by(self, factor: int) -> None:
        self.image = pygame.transform.scale_by(self.image, factor)
        self.rect.size = self.image.get_size()

    def move(self, x, y) -> None:
        self.pos = x, y


class Pawn(Piece):
    def __init__(self) -> None:
        super.__init__("../Assets/pawn.png")

