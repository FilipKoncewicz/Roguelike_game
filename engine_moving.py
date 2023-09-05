import validator
import engine_setting
import engine_board


def get_key(is_running, key, player, DIRECTIONS_X, DIRECTIONS_Y, boss_turn_counter):
    if key == 'q':
        is_running = False
    elif key in 'wasd':
        player_new_x = player['position x'] + DIRECTIONS_X[key]
        player_new_y = player['position y'] + DIRECTIONS_Y[key]
        boss_turn_counter += 1
    
    return is_running, player_new_x, player_new_y, boss_turn_counter


def change_direction(board, new_monster_position_x, new_monster_position_y, monster):
    if board[new_monster_position_y][new_monster_position_x] == "🌫️":
        monster["default turn"][0] = -monster["default turn"][0]
        monster["default turn"][1] = -monster["default turn"][1]


def move_monsters(monsters, player, board):
    for monster in monsters:
        if monster["board"] == player["board"]:
            new_monster_position_x = monster["position x"] + monster["default turn"][0]
            new_monster_position_y = monster["position y"] + monster["default turn"][1]
            board = engine_setting.put_monsters_on_board(board, monsters)
            if validator.validate_monster_turn(board[player["board"]], new_monster_position_x, new_monster_position_y):
                engine_setting.remove_monsters_from_board(board[player['board']], monsters)
                monster["position x"] = new_monster_position_x
                monster["position y"] = new_monster_position_y
            change_direction(board[player["board"]], new_monster_position_x, new_monster_position_y, monster)


def move_boss(board, player, boss, boss_turn_counter):
    if (player["board"] == boss["board"]) and (boss_turn_counter % 5 == 0):
        if not engine_board.check_boss_neighborhood(boss, player):
                boss["condition"] = 0
        if engine_board.check_boss_neighborhood(boss, player):
            return boss
        if abs(player["position x"] - boss["position x"]) >= abs(player["position y"] - boss["position y"]):
            if player["position x"] - boss["position x"] > 0:
                boss["position x"] += 1
            else:
                boss["position x"] -= 1
        elif abs(player["position y"] - boss["position y"]) >= abs(player["position x"] - boss["position x"]):
            if player["position y"] - boss["position y"] > 0:
                boss["position y"] += 1
            else:
                boss["position y"] -= 1

        if validator.validate_boss_turn(board, boss, player):
            return boss  


def change_board(player, gates):
    x, y = player['position x'], player['position y']

    if [x, y] == gates[0]:
        player['board'] = 1
        player['position x'], player['position y'] = gates[1]
    elif [x, y] == gates[1]:
        player['board'] = 0
        player['position x'], player['position y'] = gates[0]
    elif [x, y] == gates[2]:
        player['board'] = 2
        player['position x'], player['position y'] = gates[3]
    elif [x, y] == gates[3]:
        player['board'] = 1
        player['position x'], player['position y'] = gates[2]



    # def move_monster(board, player, monster):
#     if abs(player["position x"] - monster["position x"]) == 1 and abs(player["position y"] - monster["position y"]) == 0 or abs(player["position x"] - monster["position x"]) == 1 and abs(player["position y"] - monster["position y"]) == 0:
#         return monster
#     if abs(player["position x"] - monster["position x"]) >= abs(player["position y"] - monster["position y"]):
#         if player["position x"] - monster["position x"] > 0:
#             monster["position x"] += 1
#         else:
#             monster["position x"] -= 1
#     elif abs(player["position y"] - monster["position y"]) >= abs(player["position x"] - monster["position x"]):
#         if player["position y"] - monster["position y"] > 0:
#             monster["position y"] += 1
#         else:
#             monster["position y"] -= 1

#     if validator.validate_boss_turn(board, monster, player):
#         return monster  
