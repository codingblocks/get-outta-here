import pygame

from src.config import HAND_CARD_POSITION, HAND_CARD_DISTANCE, HAND_Y_OFFSET
from src.scenes.cards.player_card_choice import PlayerCardChoice
from src.scenes.cards.click_buffer import ClickBufferer
import src.scenes.globals as g


class PlayerHand(ClickBufferer):
    def __init__(self, cards=[], discard_pile=[]):
        self.cards = cards
        self.sprites = pygame.sprite.LayeredUpdates()
        self.discard_pile = discard_pile
        self.card_choice = PlayerCardChoice(self.discard_pile)
        super().__init__()

    def extend(self, cards: list):
        self.cards.extend(cards)
        self.sprites.add(cards)

    def empty(self):
        removed = self.cards
        self.cards = []
        self.sprites.empty()
        return removed

    def update(self, dt):
        self.card_choice.update(dt)

        hand_position = HAND_CARD_POSITION
        for c in self.cards:
            c.update(hand_position)
            hand_position = (hand_position[0] + HAND_CARD_DISTANCE, hand_position[1])

        pos = pygame.mouse.get_pos()
        if self.buffer_clicked():
            if self.card_choice.hidden:
                self._card_click(pos)
            else:
                g.messaging.alert("You must first choose a card", 1)

        self._card_hover(pos)

    def render(self, surface):
        self.card_choice.render(surface)
        self.sprites.draw(surface)

    def _card_click(self, pos):

        clicked = None
        clicked_index = None
        for i, c in enumerate(self.cards):
            if c.rect.collidepoint(pos[0], pos[1]):
                clicked = c
                clicked_index = i
        if clicked:
            if clicked.can_be_played():
                clicked.play()
                self._handle_special_actions(clicked)
                if clicked.is_single_use():
                    del self.cards[clicked_index]
                    clicked.kill()
                else:
                    self.cards.remove(clicked)
                    self.sprites.remove(clicked)
                    self.discard_pile.append(clicked)
            else:
                g.messaging.alert("You don't have enough resources to play this card!")


    def _handle_special_actions(self, card):
        special_action = card.config.get("special_action", "")
        if special_action == "buy":
            self.card_choice.select_cards()
        if special_action == "win":
            g.resources.got_outta_here = True

    def _card_hover(self, pos):
        hovered = None
        for c in self.cards:
            if c.rect.collidepoint(pos[0], pos[1]):
                hovered = c

        if hovered:
            hovered.rect.y -= (hovered.rect[3] - HAND_Y_OFFSET)
            self.sprites.move_to_front(hovered)

