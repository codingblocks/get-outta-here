import json
import random

import pygame

from src.config import CARDS_JSON_PATH, ITEM_SPRITE_PATH, UI_ICON_WIDTH, UI_ICON_HEIGHT, UI_ICON_SCALE, \
    CANCEL_BUTTON_PATH, HAND_CARD_DISTANCE
from src.scenes import globals as g
from src.scenes.cards.card import Card
from src.scenes.cards.click_buffer import ClickBufferer

class PlayerCardChoice(ClickBufferer):
    def __init__(self, discard_pile):
        self.sprites = pygame.sprite.LayeredUpdates()
        self.cards = []
        self.hidden = True
        self.discard_pile = discard_pile
        self.cancel_button = self._create_skip_button()
        self.left_margin = 120
        self.button_pos = (self.left_margin + 40, 610)
        super().__init__()

    def _create_skip_button(self):
        cancel_image = pygame.image.load(CANCEL_BUTTON_PATH).convert_alpha()
        cancel_button = pygame.transform.scale(cancel_image, (int(UI_ICON_WIDTH * 2), int(UI_ICON_HEIGHT * 2)))
        return cancel_button

    def select_cards(self):
        self.hidden = False
        self.sprites.empty()
        self.cards.clear()

        with open(CARDS_JSON_PATH) as f:
            library = json.loads(f.read())

        library = [c for c in library if c.get("selectable", True)]
        random.shuffle(library)
        choices = library[0:g.resources.card_choices]


        i = 0
        for choice in choices:
            c = Card(choice)
            self.cards.append(c)
            self.sprites.add(c)
            c.update((self.left_margin + HAND_CARD_DISTANCE * i, self.left_margin))
            i += 1

    def update(self, dt):
        if self.hidden:
            return

        pos = pygame.mouse.get_pos()
        self._hover(pos)
        if self.buffer_clicked():
            self._card_click(pos)
            self._cancel_click(pos)

    def render(self, surface):
        if self.hidden:
            return
        self.sprites.draw(surface)

        surface.blit(self.cancel_button, self.button_pos)

    def _hover(self, pos):
        hovered = None
        for c in self.cards:
            if c.rect.collidepoint(pos[0], pos[1]):
                hovered = c
        if hovered:
            self.sprites.move_to_front(hovered)

    def _card_click(self, pos):
        clicked = None
        for c in self.cards:
            if c.rect.collidepoint(pos[0], pos[1]):
                clicked = c
        if clicked:
            self.discard_pile.append(clicked)
            self.hidden = True

    def _cancel_click(self, pos):
        rect = pygame.Rect(self.button_pos[0], self.button_pos[1], self.cancel_button.get_width(), self.cancel_button.get_height())
        if rect.collidepoint(pos[0], pos[1]):
            self.hidden = True
