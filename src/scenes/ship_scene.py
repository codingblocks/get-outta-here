import pygame

from src.scenes.player import Player
from src.scenes.scene import Scene
from pytmx import load_pygame
from pygame import Surface
from src.config import (MAPS, MAP_TILE_WIDTH, MAP_TILE_HEIGHT)
import typing
from src.scenes.ui import Ui
import src.scenes.globals as g


class ShipScene(Scene):
    def __init__(self, title: str = "Scene", state: dict = typing.Dict):
        self.resources = g.resources
        self.ui = Ui()
        self.tmx_data = load_pygame(MAPS['ship'])
        super().__init__(title, state)

        self.player = Player()

    def update_state(self, state):
        super().update_state(state)
        g.messaging.clear()
        self.resources.reset()

    def update(self, dt):
        g.resources.update(dt)
        g.messaging.update(dt)
        self.player.update(dt)

        game_over = False
        if g.resources.got_outta_here:
            self._win_game()
        if g.resources.energy < 0:
            self._lose_game("energy")
            game_over = True
        if g.resources.fuel < 0:
            self._lose_game("fuel")
            game_over = True
        if g.resources.pirate_time_left < 0:
            self._lose_game("time")

        if game_over:
            self.done = True

    def render(self, surface: Surface):
        self.render_tmx(self.tmx_data, surface)
        self.ui.render(surface)
        self.player.render(surface)
        g.messaging.render(surface)

    def render_tmx(self, tiled_map, surface):
        g.resources.pirate_time_left
        thresholds = {
            'Pirate 1': 220,
            'Pirate 2': 180,
            'Pirate 3': 130,
            'Pirate 4': 90,
            'Pirate 5': 15,
            'Pirate 6': 2,
        }

        for layer in tiled_map.layers:
            draw_layer = True
            if layer.name in thresholds and g.resources.pirate_time_left > thresholds[layer.name]:
                draw_layer = False
            if draw_layer:
                for x, y, image in layer.tiles():
                    if image:
                        scaled_image = pygame.transform.scale(
                            image, (MAP_TILE_WIDTH, MAP_TILE_HEIGHT))
                        surface.blit(scaled_image, (MAP_TILE_WIDTH * x, MAP_TILE_HEIGHT * y))

    def _lose_game(self, reason: str):
        self.change_scene("lose", {"reason": reason})

    def _win_game(self):
        self.change_scene("win")
