from pathlib import Path
from typing import Dict

from src.util.alias import DirName, FileName

_ASSETS_DIR = Path('assets')
_DATA_DIR = Path('data')
_MAPS_DIR = Path('maps')

CARDS_JSON_PATH = _DATA_DIR / 'cards.json'

"""
    Aggregation of all fonts packs with their paths, e. g.:
    
        assets/fonts/
        ├── Atlas
        │   └── mono.ttf
        └── Frank
            └── bold.ttf
    
        # => {'Atlas': {'mono': a/f/A/mono.ttf}
              'Frank': {'bold': a/f/F/bold.ttf}}
"""
FONT_PACKS: Dict[DirName, Dict[FileName, Path]] = \
    {path.name: {file.name.removesuffix('.ttf'): file
                 for file in path.iterdir()
                 if file.is_file() and file.name.endswith('.ttf')}
     for path in (_ASSETS_DIR / 'fonts').iterdir()
     if path.is_dir()}

"""
    Aggregation of all sprite packs with their paths, e. g.:

        assets/sprites/
        ├── retro
        │   └── pixel_dude.png
        └── modern
            └── cool_dude.png

        # => {'retro': {'pixel_dude': a/s/r/pixel_dude.png}
              'modern': {'cool_dude': a/s/m/cool_dude.png}}
"""
SPRITE_PACKS: Dict[DirName, Path] = \
    {path.name: path
     for path in (_ASSETS_DIR / 'sprites').iterdir()
     if path.is_dir()}

"""
    Aggregation of all maps with their paths, e. g.:

        maps/
        ├── menu_screen.tmx
        └── reds_home.tmx

        # => {'menu_screen': m/menu_screen.tmx}
              'reds_home': m/reds_home.tmx}}
              
    By convention, Game Scenes expect to find a map matching their name.
    Scenes that are just screens (like menus) expect to find a map suffixed with '_screen'. 
"""
MAPS: Dict[FileName, Path] =\
    {file.name.removesuffix('.tmx'): file
        for file in Path('maps').iterdir()
        if file.is_file() and file.name.endswith('.tmx')}

# currently the only font, used across the entire game
MAIN_FONT_FILE = FONT_PACKS['Press_Start_2P']['Regular']

# things/sprite assignments
CHARACTER_SPRITE_PATH = SPRITE_PACKS['Oryx-SciFi'] / 'oryx_16bit_scifi_creatures_trans.png'
ITEM_SPRITE_PATH = SPRITE_PACKS['Oryx-SciFi'] / 'oryx_16bit_scifi_items_trans.png'
CANCEL_BUTTON_PATH = SPRITE_PACKS['Oryx-SciFi'] / 'cancel_button.png'

# the game uses this image for the backs of all cards
CARD_BACK_IMAGE = SPRITE_PACKS['futuristic_cards-alpha'] / 'a_stan_back_no_shadow.png'

# different card types use specific sprite backs for their front
PERSONNEL_CARD_DIR = SPRITE_PACKS['futuristic_cards-delta']
EFFECT_CARD_DIR = SPRITE_PACKS['futuristic_cards-alpha']
SPECIAL_CARD_DIR = SPRITE_PACKS['futuristic_cards-epsilon']

# the card front components are always picked relative to the card type's sprite pack
CARD_FRONT_BACKGROUND_IMAGE = "stan_front_no_shadow.png"
CARD_TITLE_IMAGE = "stan_card_name.png"
CARD_TYPE_IMAGE = "stan_card_type.png"
CARD_TEXT_IMAGE = "stan_card_description.png"

MAP_TILE_SCALE = 2
CARD_IMAGE_SIZE = (300, 465)
HAND_CARD_SIZE = (CARD_IMAGE_SIZE[0], CARD_IMAGE_SIZE[1])
MAP_TILE_WIDTH = 24 * MAP_TILE_SCALE
MAP_TILE_HEIGHT = 24 * MAP_TILE_SCALE

UI_ENERGY_ICON_X = 40
UI_FUEL_ICON_X = 210
UI_PIRATE_ICON_X = 380
UI_ICON_TEXT_HEIGHT_BUFFER = 14

UI_ICON_SCALE = 1.75
UI_ICON_WIDTH = 16 * UI_ICON_SCALE
UI_ICON_HEIGHT = 16 * UI_ICON_SCALE
UI_ICON_TEXT_BUFFER = UI_ICON_WIDTH * 2
RESOLUTION = (MAP_TILE_WIDTH * 30, MAP_TILE_HEIGHT * 20)

STOCK_PILE_SIZE = (CARD_IMAGE_SIZE[0] // 4, CARD_IMAGE_SIZE[1] // 4)
STOCK_PILE_POSITION = (MAP_TILE_WIDTH // 2, RESOLUTION[1] - (MAP_TILE_HEIGHT // 2) - STOCK_PILE_SIZE[1])

HAND_Y_OFFSET = CARD_IMAGE_SIZE[1] / 2
HAND_CARD_POSITION = (200, RESOLUTION[1] - HAND_Y_OFFSET)
HAND_CARD_DISTANCE = 140

DISCARD_PILE_SIZE = STOCK_PILE_SIZE
DISCARD_PILE_POSITION = (RESOLUTION[0] - (MAP_TILE_WIDTH // 2) - DISCARD_PILE_SIZE[0],
                         RESOLUTION[1] - (MAP_TILE_HEIGHT // 2) - DISCARD_PILE_SIZE[1])

MOUSE_CLICK_BUFFER = 200

UI_ICON_FONT_SIZE = 24
DRAW_PILE_NUMBER_OFFSET = (-20, -35)

CARD_TEXT_SIZE = 14
CARD_TITLE_SIZE = 9
CARD_TYPE_SIZE = 7
CARD_TEXT_COLOR = "white"
CARD_TYPE_COLOR = "gray"

DEFAULT_ALERT_TIME = 1
ALERT_FONT_SIZE = 24
ALERT_FONT_COLOR = "red"
