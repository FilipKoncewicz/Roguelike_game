import util
import engine
import ui
import validator


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
PLAYER_NAME = "Mordulec"

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

DIRECTIONS_X = {'w': 0, 'd': 1, 's': 0, 'a': -1}
DIRECTIONS_Y = {'w': -1, 'd': 0, 's': 1, 'a': 0}


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
    "name": PLAYER_NAME,
    "icon": PLAYER_ICON, 
    "position x": PLAYER_START_X,
    "position y": PLAYER_START_Y
    }
    return player


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    

    # util.clear_screen()

    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        print(key)

        if key == 'q':
            is_running = False
        elif key in 'wasd':
            player_new_x = player['position x'] + DIRECTIONS_X[key]
            player_new_y = player['position y'] + DIRECTIONS_Y[key]
        
        engine.remove_player_from_board(board, player)

        if validator.validate_turn(board, (player_new_x, player_new_y)):
            
            player['position x'] = player_new_x
            player['position y'] = player_new_y


if __name__ == '__main__':
    main()