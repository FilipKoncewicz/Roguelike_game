import util
import engine_board
import engine_fight
import engine_moving
import engine_setting
import ui
import validator
import characters
import hall_of_fame


NUMBER_OF_ROOMS = 3
BOARD_WIDTH = 15
BOARD_HEIGHT = 10
DIRECTIONS_X = {'w': 0, 'd': 1, 's': 0, 'a': -1}
DIRECTIONS_Y = {'w': -1, 'd': 0, 's': 1, 'a': 0}

def get_key(is_running, key, player, boss_turn_counter, monsters_turn_counter, board):
    if key == 'q':
        is_running = False
    elif key in 'wasd':
        player_new_x = player['position x'] + DIRECTIONS_X[key]
        player_new_y = player['position y'] + DIRECTIONS_Y[key]
        boss_turn_counter += 1
        monsters_turn_counter += 1
        return is_running, player_new_x, player_new_y, boss_turn_counter, monsters_turn_counter
    elif key == 'i':
        engine_board.collect_inventory(board, player)
        return
    

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
    items = characters.create_items(free_spaces)
    engine_setting.put_invetory_on_board(board, items)
    game(board, player, gates, monsters, boss, items)

    
def game(board, player, gates, monsters, boss, items):
    boss_turn_counter = 0
    monsters_turn_counter = 0
    is_running = True
    
    while player["lives"] > 0 and is_running:
        util.clear_screen()

        engine_setting.put_player_on_board(board[player['board']], player)
        engine_setting.put_monsters_on_board(board, monsters)
        engine_setting.put_invetory_on_board(board, items)
        engine_setting.put_boss_on_board(board, boss)

        ui.display_board(board[player['board']])
        ui.display_hud(player, boss, monsters)

        key = util.key_pressed()

        if key == 'q':
            is_running = False
        elif key in 'wasd':
            player, key, monsters, board, gates, boss, boss_turn_counter, monsters_turn_counter = move_characters(
                player, key, monsters, board, gates, boss, boss_turn_counter, monsters_turn_counter)
        elif key == 'i':
            engine_board.collect_inventory(board, player, items)

        engine_setting.remove_inventory_from_board(board[player["board"]], items)
    
    util.clear_screen
    print("The end")
    hall_of_fame.save_to_hall_of_fame("hall_of_fame.txt", player["name"], player["points"])
    hall_of_fame.display_dict("hall_of_fame.txt")
    input()


def move_characters(player, key, monsters, board, gates, boss, boss_turn_counter, monsters_turn_counter):
    player_new_x = player['position x'] + DIRECTIONS_X[key]
    player_new_y = player['position y'] + DIRECTIONS_Y[key]
    boss_turn_counter += 1
    monsters_turn_counter += 1

    engine_fight.fight_boss(boss, player, board[player['board']][player_new_y][player_new_x])
    engine_fight.fight_monsters(monsters, player, player_new_x, player_new_y)
    
    engine_setting.remove_being_from_board(board[player['board']], player)
    if validator.validate_player_turn(board, player_new_x, player_new_y, player, monsters):
        player['position x'] = player_new_x
        player['position y'] = player_new_y
    engine_moving.change_board(player, gates)
    engine_moving.move_monsters(monsters, player, board, monsters_turn_counter)
    engine_setting.remove_boss_from_board(board, boss)
    engine_moving.move_boss(board, player, boss, boss_turn_counter)

    return player, key, monsters, board, gates, boss, boss_turn_counter, monsters_turn_counter