def validate_turn(board, player_new_x, player_new_y, player):
    x = player_new_x
    y =  player_new_y
    if board[player["board"]][y][x] not in "🌫️👾👻👳👹️":
        player['position x'] = x
        player['position y'] = y

    return player


def validate_boss_turn(board, boss, player):
    for j in range(len(boss["icon"][0])):
        for i in range(len(boss["icon"][0][0])):
            if board[boss["board"]][boss["position x"]+j-2][boss["position y"]+i-2] != ' ':
                return False
            
    return True


def validate_monster_turn(board, new_monster_position_x, new_monster_position_y):
    x,y = new_monster_position_x, new_monster_position_y
    
    if board[y][x] != ' ':
        return False
    
    return True