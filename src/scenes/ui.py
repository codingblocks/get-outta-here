import pygame

from src.config import MAIN_FONT_FILE, UI_ICON_FONT_SIZE, UI_ICON_WIDTH, UI_ICON_HEIGHT, ITEM_SPRITE_PATH, \
    UI_ICON_SCALE, \
    UI_ENERGY_ICON_X, UI_FUEL_ICON_X, UI_PIRATE_ICON_X
from src.scenes.ui_element import UiElement
import src.scenes.globals as g

class Ui:

    def __init__(self):
        self.resources = g.resources
        self.font = pygame.font.Font(MAIN_FONT_FILE, UI_ICON_FONT_SIZE)
        self.sprites = pygame.sprite.Group()
        self.sheets = {}

        self.ui_elements = [
            UiElement(
                self._image_from_sheet(ITEM_SPRITE_PATH, (14, 4)),
                (UI_ENERGY_ICON_X, 20),
                lambda: str(self.resources.energy)
            ),
            UiElement(
                self._image_from_sheet(ITEM_SPRITE_PATH, (15, 7)),
                (UI_FUEL_ICON_X, 20),
                lambda: str(self.resources.fuel)
            ),
            UiElement(
                self._image_from_sheet(ITEM_SPRITE_PATH, (10, 2)),
                (UI_PIRATE_ICON_X, 20),
                lambda: str(self.resources.pirate_time_left)
            )
        ]

        self.sprites.add(self.ui_elements)

    def render(self, surface):
        self.sprites.draw(surface)
        for i in self.ui_elements:
            i.render_text(surface)

    def _image_from_sheet(self, sheet_path: str, pos: tuple) -> pygame.Surface:
        if sheet_path not in self.sheets:
            self.sheets[sheet_path] = pygame.image.load(sheet_path).convert_alpha()
        blank_image = pygame.Surface((UI_ICON_WIDTH // UI_ICON_SCALE, UI_ICON_HEIGHT // UI_ICON_SCALE), pygame.SRCALPHA)
        sprite_rect = pygame.Rect(pos[0] * UI_ICON_WIDTH // UI_ICON_SCALE, pos[1] * UI_ICON_WIDTH // UI_ICON_SCALE, UI_ICON_WIDTH, UI_ICON_HEIGHT)
        blank_image.blit(self.sheets[sheet_path], (0, 0), sprite_rect)
        scaled_image = pygame.transform.scale(blank_image, (int(UI_ICON_WIDTH * UI_ICON_SCALE), int(UI_ICON_WIDTH * UI_ICON_SCALE)))
        return scaled_image

