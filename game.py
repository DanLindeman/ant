import pygame
from ant import Ant
from environment import Environment
import time
from random import randint


class Game(object):

    def __init__(self):
        pygame.display.set_caption('Ants')
        width, height = (600, 600)
        self.screen = pygame.display.set_mode((width, height))
        self.env = Environment(width, height)

    def add_ants(self, number_of_ants):
        for x in range(number_of_ants):
            self.env.add_ant(x=50, y=50, speed=3, angle=randint(0, 360), awareness_radius=300)

    def handle_event(self, event):
        running = True
        if event.type == pygame.QUIT:
            running = False
        elif (event.type == pygame.MOUSEBUTTONDOWN) or (event.type == pygame.KEYDOWN):
            if (event.type == pygame.MOUSEBUTTONDOWN):
                print("MOUSE")
                print event
        return running

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                running = self.handle_event(event)
            self.env.update()
            self.screen.fill(self.env.color)

            for p in self.env.ants:
                pygame.draw.circle(self.screen, p.color, (int(p.x), int(p.y)), p.size, p.thickness)
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.add_ants(10)
    game.run_game()