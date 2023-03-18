import pygame

class Target:
    startSize = 35
    
    size = startSize
    pos = None

    dead = False

    def __init__(self, pos: tuple) -> None:
        self.pos = pos

    def update(self) -> None:
        if not self.dead:
            self.size -= self.increment
            if self.size < 0:
                self.dead = True

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 0, 0), (self.pos[0], self.pos[1], self.size, self.size), 0) 