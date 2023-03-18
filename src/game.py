from target import *
import pygame
import random

class Game:
    is_running = True
    sens =  1000

    clock = None
    screen = None

    targets = []
    targetSpawnSpeed = 15
    targetSpawnSpeedCounter = 0

    cursorPos = None

    def __init__(self) -> None:
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Osu Hand Edition")


        #test targets
        self.targets.append(Target((100, 100)))

    def update(self, pos) -> None:
        if not pos:
            return
        
        self.cursorPos = (pos[0] * self.sens, pos[1] * self.sens)
        self.clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        self.screen.fill((0, 0, 0)) #draw background
        self.renderTargets()
        pygame.draw.circle(self.screen, (255, 0, 0), self.cursorPos , 5) #draw cursor

        #collision detection
        for i in self.targets:
            if self.collisionCheck(i, self.cursorPos):
                self.targets.remove(i)

        pygame.display.update()
        self.spawnTarget()

    def deinit(self) -> None:
        pygame.quit()

    #targets
    def spawnTarget(self) -> None:
        self.targetSpawnSpeedCounter += 1
        if self.targetSpawnSpeedCounter >= self.targetSpawnSpeed:
            self.targetSpawnSpeedCounter = 0
            self.targets.append(Target((random.randint(100, 700), random.randint(100, 500))))

    def renderTargets(self) -> None:
        for i in self.targets:
            if i.size > 0:
                i.size -= 0.3
                pygame.draw.circle(self.screen, (0, 0, 255), (i.pos[0] , i.pos[1]), i.size)
            else:
                self.targets.remove(i)

    def collisionCheck(self, target: Target, cursorPos: tuple) -> bool:
        grace = 10 #cause this game is too hard bruh

        #square collision for now cause im dumb and dont know math :)
        if cursorPos[0] > target.pos[0] and cursorPos[0] < target.pos[0] + target.size + grace:
            if cursorPos[1] > target.pos[1] and cursorPos[1] < target.pos[1] + target.size + grace:
                return True
        return False