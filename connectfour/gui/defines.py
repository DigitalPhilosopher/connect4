import connectfour.Field as fd

MARGIN = 15
RADIUS = 25

SCREEN_WIDTH = (2 * RADIUS + MARGIN) * fd.Field.FIELD_LENGTH + MARGIN
SCREEN_HEIGHT = (2 * RADIUS + MARGIN) * (fd.Field.FIELD_HEIGHT + 1) + MARGIN
PICK_ROW = (2 * RADIUS + MARGIN) * fd.Field.FIELD_HEIGHT + MARGIN + RADIUS

PLAYING = 0
GAME_OVER = 1
MENU = 2

RED_PLAYER_NAME = "RED"
YELLOW_PLAYER_NAME = "YELLOW"
DRAW_PLAYER_NAME = "-"
GAME_OVER_TEXT = "GAME OVER"
MENU_TEXT = "MENU"