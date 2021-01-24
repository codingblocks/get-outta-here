import pygame
import pytest
from src.scenes.cards.player_cards import PlayerCards
from src.scenes.cards.card import Card

pygame.init()
pygame.display.set_mode((800, 600))

@pytest.mark.parametrize("total", [0,10,1,5,2])
def test_add_to_stock_pile(total):
    p = PlayerCards()
    for _ in range(total):
        c = Card({})
        p.add_to_stock_pile(c)
    assert total == len(p.stock_pile)

@pytest.mark.parametrize("total", [0,10,1,5,2])
def test_add_to_discard_pile(total):
    p = PlayerCards()
    for _ in range(total):
        c = Card({})
        p.add_to_discard_pile(c)
    assert total == len(p.discard_pile)


@pytest.mark.parametrize("stock_size, discard_size, attempted_draw_size, size_drawn", [(10,0, 1,1),(2,0,3,2),(0,0,3,0),(1,2,3,3),(0,2,3,2)])
def test_draw_cards(stock_size:int, discard_size:int, attempted_draw_size:int, size_drawn:int):
    p = PlayerCards()
    for _ in range(stock_size):
        p.add_to_stock_pile(Card({}))
    for _ in range(discard_size):
        p.discard_pile.append(Card({}))
    p.draw_cards(attempted_draw_size)
    assert size_drawn == len(p.hand)

@pytest.mark.parametrize("stock_cards, discard_cards", [(0,0),(1,2),(2,1)])
def test_shuffle_discard_pile_in(stock_cards:int, discard_cards:int):
    p = PlayerCards()
    for _ in range(stock_cards):
        p.add_to_stock_pile(Card({}))
    for _ in range(discard_cards):
        p.add_to_discard_pile(Card({}))
    p.shuffle_discard_pile_in()
    assert (stock_cards + discard_cards) == len(p.stock_pile)

@pytest.mark.parametrize("hand_size", [0,10,1])
def test_discard(hand_size:int):
    p = PlayerCards()
    for _ in range(hand_size):
        p.hand.append(Card({}))
    p.discard()
    assert 0 == len(p.hand)