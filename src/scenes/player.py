import random

import pygame
from src.config import (MAIN_FONT_FILE,
                        UI_ICON_FONT_SIZE, DRAW_PILE_NUMBER_OFFSET, CARDS_JSON_PATH)
from src.scenes.cards.card import Card
from src.scenes.cards.click_buffer import ClickBufferer
from src.scenes.cards.player_cards import PlayerCards
import src.scenes.globals as g
import json


class Player(ClickBufferer):
    def __init__(self):
        self.cards = PlayerCards(self._create_initial_stock_pile())
        self.draw_cards_timer = g.resources.draw_timer

        self.font = pygame.font.Font(MAIN_FONT_FILE, UI_ICON_FONT_SIZE)
        super().__init__()

    def _create_initial_stock_pile(self):
        with open(CARDS_JSON_PATH) as f:
            library = json.loads(f.read())

        initial_cards = []
        for card_definition in library:
            if "starting_quantity" in card_definition:
                for i in range(card_definition["starting_quantity"]):
                    c = Card(card_definition)
                    initial_cards.append(c)

        random.shuffle(initial_cards)

        return initial_cards

    def draw_cards(self):
        if self.cards.hand.card_choice.hidden:
            if self.draw_cards_timer.can_run():
                self.cards.discard()
                self.draw_cards_timer.reset()
                self.cards.draw_cards(g.resources.draw_size)
            else:
                g.messaging.alert("You can't draw again yet", 1)
        else:
            g.messaging.alert("You must first choose a card", 1)

    def update(self, dt):
        if pygame.mouse.get_pressed()[0]:
            cursor = pygame.mouse.get_pos()
            ticks = pygame.time.get_ticks()
            if self.cards.stock_pile_sprite.rect.collidepoint(cursor[0], cursor[1]) and self.buffer_clicked():
                self.draw_cards()

        self.cards.update(dt)

    def render(self, surface):
        self.cards.render(surface)
        if self.draw_cards_timer.can_run():
            text = "Click to draw!"
        else:
            text = f"{self.draw_cards_timer.get_s_remaining()}s"

        font_img = self.font.render(text, True, 'white')
        position = self.cards.stock_pile_sprite.rect.bottomright
        position = (position[0] + DRAW_PILE_NUMBER_OFFSET[0], position[1] + DRAW_PILE_NUMBER_OFFSET[1])
        surface.blit(font_img, position)