import util
import engine
import ui
import validator
import characters


NUMBER_OF_ROOMS = 3
BOARD_WIDTH = 15
BOARD_HEIGHT = 10

DIRECTIONS_X = {'w': 0, 'd': 1, 's': 0, 'a': -1}
DIRECTIONS_Y = {'w': -1, 'd': 0, 's': 1, 'a': 0}


def initiate_game():
    util.clear_screen
    player = characters.create_player()
    board = engine.create_board(NUMBER_OF_ROOMS, BOARD_WIDTH, BOARD_HEIGHT)
    board[0], last_wall_choice, gate_x_0_1, gate_y_0_1 = engine.generate_random_gate(board[0], None)
    board[1], gate_x_1_0, gate_y_1_0 = engine.connect_gate(board[1], last_wall_choice, gate_x_0_1, gate_y_0_1)
    board[2], last_wall_choice, gate_x_2_1, gate_y_2_1 = engine.generate_random_gate(board[2], last_wall_choice)
    board[1], gate_x_1_2, gate_y_1_2 = engine.connect_gate(board[1], last_wall_choice, gate_x_2_1, gate_y_2_1)

    gates = [[gate_x_0_1, gate_y_0_1], [gate_x_1_0, gate_y_1_0], [gate_x_1_2,gate_y_1_2], [gate_x_2_1,gate_y_2_1]]
    monsters = characters.create_monsters(board)
    boss = characters.create_boss(board)
    engine.put_monsters_on_board(board, monsters)
    engine.put_boss_on_board(board, boss)
    free_spaces = engine.check_free_space(board)
    items = characters.create_items(board, free_spaces)
    engine.put_invetory_on_board(board, items)

    board = game(board, player, gates, monsters, boss, items)

    
def game(board, player, gates, monsters, boss, items):
    boss_turn_counter = 0
    is_running = True

    while player["lives"] > 0 and is_running:
        util.clear_screen()
        engine.put_player_on_board(board[player['board']], player)
        engine.put_monsters_on_board(board, monsters)
        engine.put_invetory_on_board(board, items)

        if boss["lives"] > 0:
            engine.put_boss_on_board(board, boss)

        ui.display_board(board[player['board']])
        # ui.display_board_in_line(board)

        ui.display_hud(player, boss)

        key = util.key_pressed()

        if key == 'q':
            is_running = False
        elif key in 'wasd':
            player_new_x = player['position x'] + DIRECTIONS_X[key]
            player_new_y = player['position y'] + DIRECTIONS_Y[key]
            boss_turn_counter += 1
        
        if board[player['board']][player_new_y][player_new_x] == "👾" or board[player['board']][player_new_y][player_new_x] == "👹":
            engine.fight_boss(boss, player)
        
        engine.remove_being_from_board(board[player['board']], player)
        engine.move_monsters(monsters, player, board)

        if validator.validate_turn(board[player['board']], (player_new_x, player_new_y)):
            player['position x'] = player_new_x
            player['position y'] = player_new_y

        board = engine.remove_boss_from_board(board, boss)

        if (player["board"] == boss["board"]) and (boss_turn_counter % 5 == 0):
            if not engine.check_boss_neighborhood(boss, player):
                boss["condition"] = 0
            engine.move_boss(board, player, boss)

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

    print("The end")
    input()