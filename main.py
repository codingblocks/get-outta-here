import pygame
from src import config
from src.scene_runner import SceneRunner
from src.scenes.lose_scene import LoseScene
from src.scenes.ship_scene import ShipScene
from src.scenes.title_scene import TitleScene
from src.scenes.win_scene import WinScene

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(config.RESOLUTION)

    scenes = {
        "title": TitleScene("title", {}),
        "ship": ShipScene("ship", {}),
        "lose": LoseScene("lose", {}),
        "win": WinScene("title", {}),
    }

    game = SceneRunner(screen, scenes, "title")
    game.run()
