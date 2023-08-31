def validate_turn(board, player_new_coordinates):
    x,y = player_new_coordinates
    
    if board[y][x] == '#':
        return False
    
    return True


def validate_boss_turn(board, boss, player):
    for j in range(len(boss["icon"])):
        for i in range(len(boss["icon"][0])):
            if board[boss["board"]][boss["position x"]+j-2][boss["position y"]+i-2] != ' ':
                return False
            
    return True