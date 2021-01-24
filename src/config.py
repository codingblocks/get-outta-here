from pathlib import Path

MAP_TILE_SCALE = 2
UI_ICON_SCALE = 1.75
SHIP_TMX_PATH = Path("maps\\ship2.tmx")
LOSE_SCREEN_TMX_PATH = Path("maps\\lose.tmx")
WIN_SCREEN_TMX_PATH = Path("maps\\win.tmx")
TITLE_SCREEN_TMX_PATH = Path("maps\\title.tmx")
CARDS_JSON_PATH = Path("data//cards.json")

UI_ENERGY_ICON_X = 40
UI_FUEL_ICON_X = 210
UI_PIRATE_ICON_X = 380
UI_ICON_TEXT_HEIGHT_BUFFER = 14

MAIN_FONT_FILE = Path("assets//fonts//Press_Start_2P//PressStart2P-Regular.ttf")
ITEM_SPRITE_PATH = Path('assets\\sprites\\Oryx-SciFi\\oryx_16bit_scifi_items_trans.png')
CANCEL_BUTTON_PATH = Path('assets\\sprites\\Oryx-SciFi\\cancel_button.png')

PERSONNEL_CARD_DIR = Path("assets\\sprites\\Futuristic Cards\\Futuristic Card Template - Delta\\Sliced\\Regular Size")
EFFECT_CARD_DIR = Path("assets\\sprites\\Futuristic Cards\\Futuristic Card Template - Alpha\\Sliced\\Regular Size")
SPECIAL_CARD_DIR = Path("assets\\sprites\\Futuristic Cards\\Futuristic Card Template - Epsilon\\Sliced\\Regular Size")

CARD_BACK_IMAGE = Path("assets\\sprites\\Futuristic Cards\\Futuristic Card Template - Alpha\\Sliced\\Regular Size\\a_stan_back_no_shadow.png")
CARD_FRONT_BACKGROUND_IMAGE = "stan_front_no_shadow.png"
CARD_TITLE_IMAGE = "stan_card_name.png"
CARD_TYPE_IMAGE = "stan_card_type.png"
CARD_TEXT_IMAGE = "stan_card_description.png"

CARD_IMAGE_SIZE = (300, 465)
HAND_CARD_SIZE = (CARD_IMAGE_SIZE[0], CARD_IMAGE_SIZE[1])
MAP_TILE_WIDTH = 24 * MAP_TILE_SCALE
MAP_TILE_HEIGHT = 24 * MAP_TILE_SCALE
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
DISCARD_PILE_POSITION = (RESOLUTION[0] - (MAP_TILE_WIDTH // 2) - DISCARD_PILE_SIZE[0], RESOLUTION[1] - (MAP_TILE_HEIGHT // 2) - DISCARD_PILE_SIZE[1])

MOUSE_CLICK_BUFFER = 200

UI_ICON_FONT_SIZE = 24
DRAW_PILE_NUMBER_OFFSET = (-20, -35)
CHARACTER_SPRITE_PATH = Path("assets\\sprites\\Oryx-SciFi\\oryx_16bit_scifi_creatures_trans.png")

CARD_TEXT_SIZE = 14
CARD_TITLE_SIZE = 9
CARD_TYPE_SIZE = 7
CARD_TEXT_COLOR = "white"
CARD_TYPE_COLOR = "gray"

DEFAULT_ALERT_TIME = 1
ALERT_FONT_SIZE = 24
ALERT_FONT_COLOR = "red"