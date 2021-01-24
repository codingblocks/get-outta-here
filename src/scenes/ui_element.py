from typing import Callable

import pygame
from pygame.sprite import Sprite

from src.config import MAIN_FONT_FILE, UI_ICON_FONT_SIZE, UI_ICON_TEXT_BUFFER, UI_ICON_TEXT_HEIGHT_BUFFER


class UiElement(Sprite):
    def __init__(self, image:pygame.Surface, pos: tuple, get_text: Callable[[], str]):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(MAIN_FONT_FILE, UI_ICON_FONT_SIZE)
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.get_text = get_text

    def render_text(self, surface):
        img = self.font.render(self.get_text(), True, 'white')
        surface.blit(img, (self.rect[0] + UI_ICON_TEXT_BUFFER, self.rect[1] + UI_ICON_TEXT_HEIGHT_BUFFER))