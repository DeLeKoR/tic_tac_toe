from game_items import *
import sys

game = Game()

def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1]//FIELD_SIZE
                col = event.pos[0]//FIELD_SIZE
                if game.board.empty_sqr(row, col):
                    game.board.mark_sqr(row, col, game.player)
                    game.draw_fig(row, col)
                    game.queue()
                    print(game.board.squares)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    run()
