class Target:
    startSize = 15
    increment = 0.25
    
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