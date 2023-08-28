def validate_turn(board, player_new_coordinates):
    x,y = player_new_coordinates
    
    if board[y][x] == '#':
        return False
    
    return True