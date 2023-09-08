import engine_board


def validate_player_turn(board, player_new_x, player_new_y, player, monsters):
    x = player_new_x
    y =  player_new_y

    if board[player["board"]][y][x] not in "🌫️👾👻👳🦇👹️🔒🍎🗝️🥼🪄":
        return True
    elif board[player["board"]][y][x] == "🔒" and "🗝️" in player["inventory"] and engine_board.get_number_od_monsters(monsters, player) == 0:
        return True
        
    return False


def validate_monster_turn(board, monster_new_x, monster_new_y, player, monster):
    x = monster_new_x
    y =  monster_new_y
    if board[monster["board"]][y][x] not in "🌫️👾👻👳🦇👹️" and [x, y] != [player["position x"], player["position y"]]:
        return True
        
    return False


def validate_boss_turn(board, boss, player):
    for j in range(len(boss["icon"][0])):
        for i in range(len(boss["icon"][0][0])):
            if board[boss["board"]][boss["position x"]+j-2][boss["position y"]+i-2] != ' ':
                return False
            
    return True