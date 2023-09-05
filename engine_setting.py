def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.
 
    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates
 
    Returns:
    Nothing
    '''
    x, y = player['position x'], player['position y']
    board[y][x] = player["icon"]
 

def put_monsters_on_board(board, monsters):
    for monster in monsters:
        x, y = monster['position x'], monster['position y']
        board[monster['board']][y][x] = monster["icon"]

    return board


def put_boss_on_board(board, boss):
    if boss["lives"] > 0:
        for row in range(len(boss["icon"][boss["condition"]])):
            for col in range(len(boss["icon"][boss["condition"]][0])):
                x = boss["position x"] + col - 2
                y = boss["position y"] + row - 2
                board[boss["board"]][y][x] = boss["icon"][boss["condition"]][row][col]
    
    return board


def put_invetory_on_board(board, items):
    for item in items:
        x, y = item['position x'], item['position y']
        board[item['board']][y][x] = item["icon"]

    return board


def remove_monsters_from_board(board, monsters):
    for monster in monsters:
        x,y = monster['position x'],monster['position y']
        board[y][x] = ' '
    return board

 
def remove_player_from_board(board, player):
    x, y = player['position x'], player['position y']
    board[y][x] = ' '
    return board


def remove_boss_from_board(board, boss):
    for row in range(len(boss["icon"][0])):
        for col in range(len(boss["icon"][0][0])):
            x = boss["position x"] + col - 2
            y = boss["position y"] + row - 2
            board[boss["board"]][y][x] = ' '
    return board