import util
import engine
import ui
import validator
import characters


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
FOOD_ICON = 'A'
ENEMY_ICON_SPIDER = 'B' # spider
ENEMY_ICON_MUMMY = 'M' # mummy
ENEMY_ICON_ZOMBIE = 'Z' # zombie
BOSS_ICON = [['%', '%', '%', '%', '%'], ['%', '%', '%', '%', '%'], ['%', '%', '%', '%', '%'], ['%', '%', '%', '%', '%'], ['%', '%', '%', '%', '%']]

NUMBER_OF_ROOMS = 3
BOARD_WIDTH = 15
BOARD_HEIGHT = 10

DIRECTIONS_X = {'w': 0, 'd': 1, 's': 0, 'a': -1}
DIRECTIONS_Y = {'w': -1, 'd': 0, 's': 1, 'a': 0}


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    # player_name = input("Enter player's name: ")

    player = {
    "name": 'l',#player_name,
    "icon": PLAYER_ICON, 
    "position x": PLAYER_START_X,
    "position y": PLAYER_START_Y,
    "board": 0,
    "lives": 10,
    "armor": 0,
    "strength": 1,
    "inventory": []
    }

    return player


def main():
    player = create_player()
    
    board = engine.create_board(NUMBER_OF_ROOMS, BOARD_WIDTH, BOARD_HEIGHT)
    board[0], last_wall_choice, gate_x_0_1, gate_y_0_1 = engine.generate_random_gate(board[0], None)
    board[1], gate_x_1_0, gate_y_1_0 = engine.connect_gate(board[1], last_wall_choice, gate_x_0_1, gate_y_0_1)
    board[2], last_wall_choice, gate_x_2_1, gate_y_2_1 = engine.generate_random_gate(board[2], last_wall_choice)
    board[1], gate_x_1_2, gate_y_1_2 = engine.connect_gate(board[1], last_wall_choice, gate_x_2_1, gate_y_2_1)

    gates = [[gate_x_0_1, gate_y_0_1], [gate_x_1_0, gate_y_1_0], [gate_x_1_2,gate_y_1_2], [gate_x_2_1,gate_y_2_1]]
    monsters = characters.create_monsters(board)
    # ui.display_board(board)
    position = [2, 2]
    board[2] = engine.put_boss(BOSS_ICON, board[2], position)
    engine.put_monsters_on_board(board, monsters)

    board = game(board, player, gates)
    # ui.display_board(board)

    
def game(board, player, gates):
    is_running = True
    while is_running:
        #util.clear_screen()
        # print(player['board'])
        # print(board)
        engine.put_player_on_board(board[player['board']], player)
        
        ui.display_board(board)

        key = util.key_pressed()

        if key == 'q':
            is_running = False
        elif key in 'wasd':
            player_new_x = player['position x'] + DIRECTIONS_X[key]
            player_new_y = player['position y'] + DIRECTIONS_Y[key]
        
        engine.remove_player_from_board(board[player['board']], player)

        if validator.validate_turn(board[player['board']], (player_new_x, player_new_y)):
            player['position x'] = player_new_x
            player['position y'] = player_new_y
        

        if [player['position x'], player['position y']] == gates[0]:
            player['board'] = 1
            player['position x'], player['position y'] = gates[1]
        elif [player['position x'], player['position y']] == gates[1]:
            player['board'] = 0
            player['position x'], player['position y'] = gates[0]
        elif [player['position x'], player['position y']] == gates[2]:
            player['board'] = 2
            player['position x'], player['position y'] = gates[3]
        elif [player['position x'], player['position y']] == gates[3]:
            player['board'] = 1
            player['position x'], player['position y'] = gates[2]


if __name__ == '__main__':
    main()