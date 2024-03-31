import pygame
from pygame import Surface

import numpy as np

class Board:
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.image: Surface = pygame.image.load(self.path)
        self.rect = self.image.get_rect()

        # Define the initial state of the chessboard
        initial_board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]

        # Convert it to a NumPy array
        self.chessboard = np.array(initial_board)

    def scale_by(self, factor: int) -> None:
        self.image = pygame.transform.scale_by(self.image, factor)
        self.rect.size = self.image.get_size()