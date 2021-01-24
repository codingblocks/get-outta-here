import pygame
from pygame.constants import QUIT

from src.config import MAP_TILE_WIDTH, MAP_TILE_HEIGHT

class Scene(object):

    def __init__(self, title: str = "Scene", state: dict = {}):
        self._init(title, state)

    def _init(self, title, state: dict):
        self.title = title
        self.state = state
        self.done = False
        self.quit = False
        self.clock = pygame.time.Clock()

    def update_state(self, state):
        self.state = state

    def get_event(self, event):
        if event.type == QUIT:
            self.quit = True

    def before_exit(self):
        pass

    def update(self, dt):
        pass

    def render_tmx(self, tiled_map, surface):
        for layer in tiled_map.layers:
            for x, y, image in layer.tiles():
                if image:
                    scaled_image = pygame.transform.scale(
                        image, (MAP_TILE_WIDTH, MAP_TILE_HEIGHT))
                    surface.blit(scaled_image, (MAP_TILE_WIDTH * x, MAP_TILE_HEIGHT * y))

    def render(self, surface):
        pass

    def change_scene(self, label, next_state: dict = {}):
        self.runner.change_scene(label, next_state)

    def register_runner(self, runner):
        self.runner = runner
