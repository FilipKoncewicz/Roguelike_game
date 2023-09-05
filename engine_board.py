import random


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
    
        top_wall = ["🌫️"] * (width + 2)
        room.append(top_wall)
    
        for _ in range(height):
            row = ['🌫️']
            for _ in range(width):
                row.append(" ")
            row.append("🌫️")
            room.append(row)
    
        bottom_wall = ["🌫️"] * (width + 2)
        room.append(bottom_wall)
        board.append(room)
    
    return board


def generate_random_gate(board, mid_board, last_wall_choice):
    width = len(board[0])
    height = len(board)
 
    wall_choices = ["top", "bottom", "left", "right"]

    if last_wall_choice in wall_choices:
        wall_choices.remove(last_wall_choice)

    wall_choice = random.choice(wall_choices)
    
    if wall_choice == "top":
        gate_x = random.randint(1, width - 2)
        gate_y = 0
        gate_x1 = gate_x
        gate_y1 = gate_y + height - 1
    elif wall_choice == "bottom":
        gate_x = random.randint(1, width - 2)
        gate_y = height - 1
        gate_x1 = gate_x
        gate_y1 = gate_y - height + 1
    elif wall_choice == "left":
        gate_x = 0
        gate_y = random.randint(1, height - 2)
        gate_x1 = gate_x + width -1
        gate_y1 = gate_y
    elif wall_choice == "right":
        gate_x = width - 1
        gate_y = random.randint(1, height - 2)
        gate_x1 = gate_x - width + 1
        gate_y1 = gate_y

    board[gate_y][gate_x] = ' '
    mid_board[gate_y1][gate_x1] = ' '
    return board, mid_board, wall_choice, gate_x, gate_y, gate_x1, gate_y1


def get_gates(board):
    board[0], board[1], last_wall_choice, gate_x_0_1, gate_y_0_1, gate_x_1_0, gate_y_1_0 = generate_random_gate(board[0], board[1], None)
    board[2], board[1], last_wall_choice, gate_x_2_1, gate_y_2_1, gate_x_1_2, gate_y_1_2 = generate_random_gate(board[2], board[1], last_wall_choice)
    gates = [[gate_x_0_1, gate_y_0_1], [gate_x_1_0, gate_y_1_0], [gate_x_1_2,gate_y_1_2], [gate_x_2_1,gate_y_2_1]]
    return gates


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


def check_free_space(board):
    free_spaces = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(len(board[i][j])):
                if board[i][j][k] == " ":
                    free_spaces[i].append([j, k])
    return free_spaces


def check_boss_neighborhood(boss, player):
    neighborhood = []
    min_around_boss = -3
    max_around_boss = 3

    for x in range(min_around_boss, max_around_boss + 1):
        for y in range(min_around_boss, max_around_boss + 1):
            if min_around_boss in (x, y) or max_around_boss in (x, y):
                neighborhood.append([x, y])

    for position in neighborhood:
        x = boss["position x"] + position[0]
        y = boss["position y"] + position[1]
        if [x, y] == [player["position x"], player["position y"]]:
            return True
    return False