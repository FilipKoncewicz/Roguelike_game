import util
import engine_board
import engine_fight
import engine_moving
import engine_setting
import ui
import validator
import characters


NUMBER_OF_ROOMS = 3
BOARD_WIDTH = 15
BOARD_HEIGHT = 10
DIRECTIONS_X = {'w': 0, 'd': 1, 's': 0, 'a': -1}
DIRECTIONS_Y = {'w': -1, 'd': 0, 's': 1, 'a': 0}

def get_key(is_running, key, player, boss_turn_counter):
    if key == 'q':
        is_running = False
    elif key in 'wasd':
        player_new_x = player['position x'] + DIRECTIONS_X[key]
        player_new_y = player['position y'] + DIRECTIONS_Y[key]
        boss_turn_counter += 1
    
    return is_running, player_new_x, player_new_y, boss_turn_counter


def initiate_game():
    util.clear_screen
    player = characters.create_player()
    board = engine_board.create_board(NUMBER_OF_ROOMS, BOARD_WIDTH, BOARD_HEIGHT)
    gates = engine_board.get_gates(board)
    monsters = characters.create_monsters(board)
    boss = characters.create_boss(board)
    engine_setting.put_monsters_on_board(board, monsters)
    engine_setting.put_boss_on_board(board, boss)
    free_spaces = engine_board.check_free_space(board)
    items = characters.create_items(board, free_spaces)
    engine_setting.put_invetory_on_board(board, items)
    game(board, player, gates, monsters, boss, items)

    
def game(board, player, gates, monsters, boss, items):
    boss_turn_counter = 0
    is_running = True

    while player["lives"] > 0 and is_running:
        util.clear_screen()

        engine_setting.put_player_on_board(board[player['board']], player)
        engine_setting.put_monsters_on_board(board, monsters)
        engine_setting.put_invetory_on_board(board, items)
        engine_setting.put_boss_on_board(board, boss)

        ui.display_board(board[player['board']])
        ui.display_hud(player, boss)

        key = util.key_pressed()
        is_running, player_new_x, player_new_y, boss_turn_counter = get_key(is_running, key, player, boss_turn_counter)
        
        engine_fight.fight_boss(boss, player, board[player['board']][player_new_y][player_new_x])
        engine_setting.remove_player_from_board(board[player['board']], player)
        engine_moving.move_monsters(monsters, player, board)
        validator.validate_turn(board, player_new_x, player_new_y, player)
        engine_setting.remove_boss_from_board(board, boss)
        engine_moving.move_boss(board, player, boss, boss_turn_counter)#
        engine_moving.change_board(player, gates)

    print("The end")
    input()