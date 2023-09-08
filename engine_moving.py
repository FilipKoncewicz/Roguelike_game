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
    return monster

def move_monster(monster, player, board, monsters):
    if monster["board"] == player["board"]:
        # print(f"monster, ta sama plansza: {monster}")
        delta_x = abs(player["position x"] - monster["position x"])
        delta_y = abs(player["position y"] - monster["position y"])
        # print(f"delta x: {delta_x}")
        # print(f"delta y: {delta_y}")
        # print(f"player['position x']: {player['position x']}")
        # print(f"monster['position x']: {monster['position x']}")
        # print(f"delta x: {delta_x}")
        # print(f"player['position y']: {player['position y']}")
        # print(f"monster['position y']: {monster['position y']}")
        # print(f"delta x: {delta_y}")

        if delta_x <= 4 and delta_y <= 4:
            # print("Follow")
            new_monster_position_x, new_monster_position_y = follow_player(player, monster)
        else:
            new_monster_position_x = monster["position x"] + monster["default turn"][0]
            new_monster_position_y = monster["position y"] + monster["default turn"][1]
            change_direction(board[player["board"]], new_monster_position_x, new_monster_position_y, monster)

        board[player['board']] = engine_setting.remove_being_from_board(board[player['board']], monster)

        if validator.validate_monster_turn(board, new_monster_position_x, new_monster_position_y, player, monster):
            monster['position x'] = new_monster_position_x
            monster['position y'] = new_monster_position_y
        engine_setting.put_monsters_on_board(board, monsters)
    return monster


def move_monsters(monsters, player, board, monsters_turn_counter):
    if monsters_turn_counter % 2 == 0:
        for monster in monsters:
            move_monster(monster, player, board, monsters)

    
        

def follow_player(player, being):
    new_being_position_x = 0
    new_being_position_y = 0
    new_being_position_x = being["position x"]
    new_being_position_y = being["position y"]

    if abs(player["position x"] - being["position x"]) >= abs(player["position y"] - being["position y"]):
        if player["position x"] - being["position x"] > 0:
            new_being_position_x += 1
        else:
            new_being_position_x -= 1
    elif abs(player["position y"] - being["position y"]) >= abs(player["position x"] - being["position x"]):
        if player["position y"] - being["position y"] > 0:
            new_being_position_y += 1
        else:
            new_being_position_y -= 1

    return new_being_position_x, new_being_position_y


def move_boss(board, player, boss, boss_turn_counter):
    if (player["board"] == boss["board"]) and (boss_turn_counter % 5 == 0):
        if not engine_board.check_boss_neighborhood(boss, player):
                boss["condition"] = 0
        if engine_board.check_boss_neighborhood(boss, player):
            return boss
        boss["position x"], boss["position y"] = follow_player(player, boss)

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
    return player