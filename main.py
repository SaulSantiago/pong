import pygame

class Board():
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((0,0), pygame.fullscreen)
        self.clock = pygame.time.Clock()
    def run(self):
        done = False
        player_1 = Paddle()
        player_2 = Paddle()
        player_1_score = 0
        player_2_score = 0
        max_score = 3
        game_history = []
        while not done:
            pass
class Paddle():
    pass
class Ball():
    pass
class ScoreBoard():
    pass
if __name__ =='__main__':
    pass