import pygame
import time

from src.config import MAIN_FONT_FILE, DEFAULT_ALERT_TIME, ALERT_FONT_COLOR, ALERT_FONT_SIZE


class Messaging:
    def __init__(self):
        self.font = pygame.font.Font(MAIN_FONT_FILE, ALERT_FONT_SIZE)
        self.show = False
        self.message = ""
        self.show_message_til_s = 0
        self.color = ALERT_FONT_COLOR

    def alert(self, message, duration_s:int = DEFAULT_ALERT_TIME):
        self.info(message, duration_s, "red")

    def info(self, message, duration_s: int = DEFAULT_ALERT_TIME, color: str = "white"):
        self.show = True
        self.message = message
        self.color = color
        self.show_message_til_s = time.time() + duration_s

    def update(self, dt):
        if self.show and time.time() >= self.show_message_til_s:
            self.show = False

    def clear(self):
        self.show = False

    def render(self, surface: pygame.Surface):
        if self.show:
            font_render = self.font.render(self.message, True, self.color)
            screen_center = surface.get_rect().center
            pos = (screen_center[0] - font_render.get_width() // 2,  screen_center[1] - font_render.get_height() // 2)
            surface.blit(font_render, pos)
