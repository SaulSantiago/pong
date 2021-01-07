import pygame

class Pong:
    HEIGHT: int = 800
    WIDTH: int = 1600

    def __init__(self):
        pygame.init() #start the pygame instance
        #setup the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    print('Game Ending')
                    return


if __name__ == '__main__':
    pong = Pong()
    pong.game_loop()
