from handcontroller import *
from game import *

if __name__ == "__main__":
    controller = handcontroller()
    game = Game()

    while game.is_running:
        pos = controller.update()
        game.update(pos)

    game.deinit()