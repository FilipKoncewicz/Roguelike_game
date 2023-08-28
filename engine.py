import random
 
def create_board(width, height):
    '''
    Creates a new game board based on input parameters.
 
    Args:
    int: The width of the board
    int: The height of the board
 
    Returns:
    list: Game board
    '''
    board = []
 
    top_wall = ["#"] * (width + 2)
    board.append(top_wall)
 
    for _ in range(height):
        row = ['#']
        for _ in range(width):
            row.append(" ")
        row.append("#")
        board.append(row)
 
    bottom_wall = ["#"] * (width + 2)
    board.append(bottom_wall)
    board = generate_random_gate(board)
    return board
 
def generate_random_gate(board):
    width = len(board[0])
    height = len(board)
    print(width)
    print(height)
    print(board)
 
    wall_choice = random.choice(["top", "bottom", "left", "right"])
 
    if wall_choice == "top":
        exit_x = random.randint(1, width - 2)
        board[0][exit_x] = 'G'
    elif wall_choice == "bottom":
        exit_x = random.randint(1, width - 2)
        board[height - 1][exit_x] = 'G'
    elif wall_choice == "left":
        exit_y = random.randint(1, height - 2)
        board[exit_y][0] = 'G'
    elif wall_choice == "right":
        exit_y = random.randint(1, height - 2)
        board[exit_y][width - 1] = 'G'
 
    return board
 
 
def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.
 
    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates
 
    Returns:
    Nothing
    '''
    x,y = player['position x'],player['position y']
    board[y][x]= player ["icon"]
 
 
def remove_player_from_board(board, player):
    x,y = player['position x'],player['position y']
    board[y][x] = ' '