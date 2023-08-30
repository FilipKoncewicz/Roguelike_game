import random

def put_boss(BOSS_ICON, board, position):
    for j in range(len(BOSS_ICON)):
        for i in range(len(BOSS_ICON[0])):
            board[position[0]+j][position[1]+i] = BOSS_ICON[j][i]

    return board


def create_board(number_of_rooms, width, height):
    '''
    Creates a new game board based on input parameters.
 
    Args:
    int: The width of the board
    int: The height of the board
 
    Returns:
    list: Game board
    '''
    board = []
    for _ in range(number_of_rooms):
        room = []
    
        top_wall = ["#"] * (width + 2)
        room.append(top_wall)
    
        for _ in range(height):
            row = ['#']
            for _ in range(width):
                row.append(" ")
            row.append("#")
            room.append(row)
    
        bottom_wall = ["#"] * (width + 2)
        room.append(bottom_wall)
        board.append(room)
    
    return board


def connect_gate(board, last_wall_choice, gate_x, gate_y):
    width = len(board[0])
    height = len(board)

    if last_wall_choice == "top":
        gate_x = gate_x
        gate_y = gate_y + height - 1
    elif last_wall_choice == "bottom":
        gate_x = gate_x
        gate_y = gate_y - height + 1
    elif last_wall_choice == "left":
        gate_x = gate_x + width -1
        gate_y = gate_y
    elif last_wall_choice == "right":
        gate_x = gate_x - width + 1
        gate_y = gate_y

    board[gate_y][gate_x] = ' '
    return board, gate_x, gate_y


def generate_random_gate(board, last_wall_choice):
    width = len(board[0])
    height = len(board)
 
    wall_choices = ["top", "bottom", "left", "right"]

    if last_wall_choice in wall_choices:
        wall_choices.remove(last_wall_choice)

    wall_choice = random.choice(wall_choices)
    
    if wall_choice == "top":
        gate_x = random.randint(1, width - 2)
        gate_y = 0
    elif wall_choice == "bottom":
        gate_x = random.randint(1, width - 2)
        gate_y = height - 1
    elif wall_choice == "left":
        gate_x = 0
        gate_y = random.randint(1, height - 2)
    elif wall_choice == "right":
        gate_x = width - 1
        gate_y = random.randint(1, height - 2)

    board[gate_y][gate_x] = ' '
    return board, wall_choice, gate_x, gate_y
 
 
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

 
def remove_player_from_board(board, player):
    x,y = player['position x'],player['position y']
    board[y][x] = ' '