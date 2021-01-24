import pygame
from src.config import (CARD_FRONT_BACKGROUND_IMAGE, CHARACTER_SPRITE_PATH, MAP_TILE_HEIGHT,
                        MAP_TILE_WIDTH, MAIN_FONT_FILE, MAP_TILE_SCALE, CARD_TEXT_SIZE, CARD_TEXT_COLOR,
                        CARD_IMAGE_SIZE, CARD_TITLE_SIZE, CARD_TITLE_IMAGE, CARD_TEXT_IMAGE, CARD_TYPE_IMAGE,
                        CARD_TYPE_SIZE, CARD_TYPE_COLOR, PERSONNEL_CARD_DIR, EFFECT_CARD_DIR, SPECIAL_CARD_DIR)
from src.scenes.text_writer import draw_text
import src.scenes.globals as g

class Card(pygame.sprite.Sprite):
    character_sheet = None

    def __init__(self, config: dict):
        if self.character_sheet is None:
            self.character_sheet = pygame.image.load(CHARACTER_SPRITE_PATH).convert_alpha()

        pygame.sprite.Sprite.__init__(self)
        self.config = config
        if self.config['type'].lower() == "special":
            self.card_dir = f"{SPECIAL_CARD_DIR}"
        elif self.config['type'].lower() == "effect":
            self.card_dir = f"{EFFECT_CARD_DIR}"
        else:
            self.card_dir = f"{PERSONNEL_CARD_DIR}"

        card_background_path = f"{self.card_dir}\\{CARD_FRONT_BACKGROUND_IMAGE}"
        print(card_background_path)
        card_background = pygame.image.load(card_background_path).convert_alpha()

        self._draw_portrait(card_background)
        self._draw_title(card_background)
        self._draw_text(card_background)
        self._draw_type(card_background)
        self.image = card_background

        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = -1000

    def update(self, position: tuple):
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def can_be_played(self):
        can_be_played = True
        modifiers = self.config.get("modifiers", {})
        if modifiers.get("energy", 0) and modifiers["energy"] + g.resources.energy <= 0:
            can_be_played = False
        if modifiers.get("fuel", 0) and modifiers["fuel"] + g.resources.fuel <= 0:
            can_be_played = False
        if modifiers.get("shields", 0) and modifiers["shields"] + g.resources.shields <= 0:
            can_be_played = False
        return can_be_played

    def play(self):
        modifiers = self.config.get("modifiers", {})
        for k,v in modifiers.items():
            g.resources.modify(k, v)

    def is_single_use(self):
        return self.config['type'].lower() == "personnel"

    def _draw_portrait(self, card_background):
        if "sheet" in self.config['sprite']:
            self._draw_item_portrait(card_background)
        else:
            self._draw_character_portrait(card_background)

    def _draw_item_portrait(self, card_background):
        config = self.config
        sheet = pygame.image.load(config['sprite']['sheet']).convert_alpha()
        tile_size = self.config['sprite']['sheet_tile_size']
        sprite_position_on_sheet = (config['sprite']['x'], config['sprite']['y'])
        sprite_rect = pygame.Rect(sprite_position_on_sheet[0] * tile_size, sprite_position_on_sheet[1] * tile_size,  tile_size,  tile_size)

        portrait_image = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
        portrait_image.blit(sheet, (0, 0), sprite_rect)
        scaled_portrait = pygame.transform.scale(portrait_image, (MAP_TILE_WIDTH * 3, MAP_TILE_HEIGHT * 3))
        card_center = card_background.get_rect().center
        card_center = (card_center[0] - scaled_portrait.get_rect().w // 2, card_center[1] - 190)

        card_background.blit(scaled_portrait, card_center)


        pass

    def _draw_character_portrait(self, card_background):
        config = self.config
        portrait_position = (config['sprite']['x'], config['sprite']['y'])

        blank_image = pygame.Surface((MAP_TILE_WIDTH // MAP_TILE_SCALE, MAP_TILE_HEIGHT // MAP_TILE_SCALE), pygame.SRCALPHA)
        sprite_rect = pygame.Rect(portrait_position[0] * MAP_TILE_WIDTH // MAP_TILE_SCALE, portrait_position[1] * MAP_TILE_HEIGHT // MAP_TILE_SCALE, MAP_TILE_WIDTH // MAP_TILE_SCALE, MAP_TILE_HEIGHT // MAP_TILE_SCALE)
        blank_image.blit(self.character_sheet, (0, 0), sprite_rect)

        scaled_portrait = pygame.transform.scale(blank_image, (MAP_TILE_WIDTH * 3, MAP_TILE_HEIGHT * 3))
        portrait_rect = scaled_portrait.get_rect()
        card_center = card_background.get_rect().center
        card_center = (card_center[0] - scaled_portrait.get_rect().w // 2, card_center[1] - 190)

        card_background.blit(scaled_portrait, card_center, portrait_rect)

    def _draw_title(self, card_background):
        plate_image = pygame.image.load(f"{self.card_dir}\\{CARD_TITLE_IMAGE}").convert_alpha()

        font = pygame.font.Font(MAIN_FONT_FILE, CARD_TITLE_SIZE)
        font_render = font.render(self.config['title'], True, CARD_TEXT_COLOR)
        font_render.get_rect().center = card_background.get_rect().center
        font_left = plate_image.get_rect().center[0] - font_render.get_rect().w // 2
        font_top = plate_image.get_rect().center[1] - font_render.get_rect().h // 2
        font_pos = (font_left, font_top - 8)

        plate_image.blit(font_render, font_pos)
        card_background.blit(plate_image, (31, 214))

    def _draw_type(self, card_background):
        plate_image = pygame.image.load(f"{self.card_dir}\\{CARD_TYPE_IMAGE}").convert_alpha()

        font = pygame.font.Font(MAIN_FONT_FILE, CARD_TYPE_SIZE)
        font_render = font.render(self.config['type'], True, CARD_TYPE_COLOR)
        font_render.get_rect().center = card_background.get_rect().center
        font_left = plate_image.get_rect().center[0] - font_render.get_rect().w // 2
        font_top = plate_image.get_rect().center[1] - font_render.get_rect().h // 2
        font_pos = (font_left, font_top)

        plate_image.blit(font_render, font_pos)
        card_background.blit(plate_image, (73, 259))

    def _draw_text(self, card_background):
        plate_image = pygame.image.load(f"{self.card_dir}\\{CARD_TEXT_IMAGE}").convert_alpha()
        font = pygame.font.Font(MAIN_FONT_FILE, CARD_TEXT_SIZE)
        card_center = card_background.get_rect().center

        cr = card_background.get_rect()
        left_buffer = 70
        text_area = pygame.Rect(cr.x + left_buffer, card_center[1] + 80, CARD_IMAGE_SIZE[0] - left_buffer * 2, 200)

        card_background.blit(plate_image, (25, 276))
        draw_text(card_background, self.config['text'], CARD_TEXT_COLOR, text_area, font)



# Card title, cost