import pygame
from src.config import (DISCARD_PILE_POSITION, DISCARD_PILE_SIZE, STOCK_PILE_POSITION, STOCK_PILE_SIZE, CARD_BACK_IMAGE)


class CardPile(pygame.sprite.Sprite):
    def __init__(self, stock: bool):
        if stock:
            size = STOCK_PILE_SIZE
            position = STOCK_PILE_POSITION
        else:
            size = DISCARD_PILE_SIZE
            position = DISCARD_PILE_POSITION
        self.stock = stock
        pygame.sprite.Sprite.__init__(self)
        image_path = CARD_BACK_IMAGE
        self.card_image = pygame.image.load(image_path).convert_alpha()

        self.empty_image = pygame.transform.scale(self.card_image, size)
        self.empty_image.fill((255, 255, 255, 80), None, pygame.BLEND_RGBA_MULT)

        self.full_image = pygame.transform.scale(self.card_image, size)
        self.image = self.full_image

        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def hide(self):
        self.image = self.empty_image

    def show(self):
        self.image = self.full_image
