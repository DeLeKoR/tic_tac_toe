import pygame
import numpy
from constans import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("TIC TAC TOE")
        screen = pygame.display.set_mode((SIZE, SIZE))
        screen.fill(BG_COLOR)
        self.__screen = screen
        self.board = Board()
        self.player = 1

        self.draw_lines()

    def draw_lines(self):
        for i in range(1, BORD_SIZE):
            # вертикальные линии
            pygame.draw.line(self.__screen, LINE_COLOR, (FIELD_SIZE * i, 0), (FIELD_SIZE * i, SIZE), LINE_WIDTH)
            # горизонтальные линии
            pygame.draw.line(self.__screen, LINE_COLOR, (0, FIELD_SIZE * i), (SIZE, FIELD_SIZE * i), LINE_WIDTH)

    def queue(self):
        self.player = 2 if self.player == 1 else 1

    def draw_fig(self, row, col):
        if self.player == 1:
            # крестик
            start_desc = (col * FIELD_SIZE + OFFSET, row * FIELD_SIZE + OFFSET)
            end_desc = (col * FIELD_SIZE + FIELD_SIZE - OFFSET, row * FIELD_SIZE + FIELD_SIZE - OFFSET)
            pygame.draw.line(self.__screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            start_asc = (col * FIELD_SIZE + OFFSET, row * FIELD_SIZE + FIELD_SIZE - OFFSET)
            end_asc = (col * FIELD_SIZE + FIELD_SIZE - OFFSET, row * FIELD_SIZE + OFFSET)
            pygame.draw.line(self.__screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2:
            # нолик
            center = (col * FIELD_SIZE + FIELD_SIZE // 2, row * FIELD_SIZE + FIELD_SIZE // 2)
            pygame.draw.circle(self.__screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

class Board:
    def __init__(self):
        self.squares = numpy.zeros((BORD_SIZE, BORD_SIZE))
        print(self.squares)

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0
