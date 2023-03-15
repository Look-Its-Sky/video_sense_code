from target import *
import pygame
import random

class Game:
    is_running = True
    sens =  1000

    clock = None
    screen = None

    targetArr = []
    targetSpawnSpeed = 15
    targetSpawnSpeedCounter = 0

    def __init__(self) -> None:
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Osu Hand Edition")

    def update(self, pos) -> None:
        self.clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        self.screen.fill((0, 0, 0)) #draw background
        pygame.draw.circle(self.screen, (255, 0, 0), (pos[0] * self.sens, pos[1] * self.sens), 5)#draw cursor
        
        pygame.display.update()

    def deinit(self) -> None:
        pygame.quit()

    def targetUpdate(self) -> None:
        if self.targetSpawnSpeedCounter > self.targetSpawnSpeed:
            self.targetSpawnSpeedCounter = 0
            self.targetArr.append(Target((random.randint(0, 800), random.randint(0, 600))))

        for i in range(len(self.targetArr)):
            if i.dead:
                self.targetArr.pop(i)