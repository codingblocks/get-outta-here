import pygame

from src.config import MOUSE_CLICK_BUFFER


class ClickBufferer:
    def __init__(self):
        self.last_click = pygame.time.get_ticks() - MOUSE_CLICK_BUFFER

    def buffer_clicked(self):
        if pygame.mouse.get_pressed()[0]:
            ticks = pygame.time.get_ticks()
            able_to_click = self.last_click + MOUSE_CLICK_BUFFER < ticks
            if able_to_click:
                self.last_click = ticks
                return True
            else:
                return False
