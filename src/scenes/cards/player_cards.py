import pygame

from src.scenes.cards.card import Card
import random
from src.scenes.cards.card_pile import CardPile
from src.scenes.cards.click_buffer import ClickBufferer
from src.scenes.cards.player_hand import PlayerHand


class PlayerCards(ClickBufferer):
    def __init__(self, stock_pile=[]):
        self.discard_pile = []
        self.stock_pile = []
        self.hand = PlayerHand([], self.discard_pile)
        self.sprites = pygame.sprite.Group()
        super().__init__()

        for c in stock_pile:
            self.add_to_stock_pile(c)

        self.stock_pile_sprite = CardPile(True)
        self.discard_pile_sprite = CardPile(False)
        self.sprites.add(self.stock_pile_sprite, self.discard_pile_sprite)

    def add_to_stock_pile(self, card: Card):
        self.stock_pile.append(card)
    
    def add_to_discard_pile(self, card: Card):
        self.discard_pile.append(card)

    def draw_cards(self, number_of_cards: int):
        total_to_draw = number_of_cards
        drawn = self._pop_count(self.stock_pile, total_to_draw)
        total_to_draw = total_to_draw - len(drawn)
        if total_to_draw > 0:
            self.shuffle_discard_pile_in()
            drawn_from_reshuffled = self._pop_count(self.stock_pile, total_to_draw)
            drawn.extend(drawn_from_reshuffled)
        self.hand.extend(drawn)

    def shuffle_discard_pile_in(self):
        self.stock_pile.extend(self.discard_pile)
        self.discard_pile.clear()
        random.shuffle(self.stock_pile)

    def discard(self):
        removed = self.hand.empty()
        self.discard_pile.extend(removed)

    def _pop_count(self, remove_list: list, count: int):
        remove_count = min(count, len(remove_list))
        removed = remove_list[0:remove_count]
        del remove_list[0:remove_count]
        return removed

    def update(self, dt):
        if len(self.stock_pile):
            self.stock_pile_sprite.show()
        else:
            self.stock_pile_sprite.hide()

        if len(self.discard_pile):
            self.discard_pile_sprite.show()
        else:
            self.discard_pile_sprite.hide()

        self.hand.update(dt)

        if pygame.mouse.get_pressed()[0]:
            cursor = pygame.mouse.get_pos()
            if self.stock_pile_sprite.rect.collidepoint(cursor[0], cursor[1]) and self.buffer_clicked():
                pass

    def render(self, surface):
        self.sprites.draw(surface)
        self.hand.render(surface)
