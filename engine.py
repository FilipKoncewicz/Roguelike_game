import random
import validator

def attack_boss(player,boss):
    inside = []

    for i in range(-2, 3):
        for j in range(-2,3):
            inside.append([i, j])

    for position in inside:
        if [boss["position x"] + position[0], boss["position y"] + position[1]] == [player["position x"], player["position y"]]:
            return True
    return False


def fight_boss(boss, player):
    boss["lives"] -= player["strength"]
    boss["attacks_in_cycle"] += 1

    if boss["condition"] == 1:
        player["lives"] -= 5
        boss["condition"] = 0
    
    if boss["attacks_in_cycle"] == 2:
        boss["attacks_in_cycle"] = 0
        boss["condition"] = 1
    
    
    return boss, player

def move_monster(board, player, monster):
    if abs(player["position x"] - monster["position x"]) == 1 and abs(player["position y"] - monster["position y"]) == 0 or abs(player["position x"] - monster["position x"]) == 1 and abs(player["position y"] - monster["position y"]) == 0:
        return monster
    if abs(player["position x"] - monster["position x"]) >= abs(player["position y"] - monster["position y"]):
        if player["position x"] - monster["position x"] > 0:
            monster["position x"] += 1
        else:
            monster["position x"] -= 1
    elif abs(player["position y"] - monster["position y"]) >= abs(player["position x"] - monster["position x"]):
        if player["position y"] - monster["position y"] > 0:
            monster["position y"] += 1
        else:
            monster["position y"] -= 1

    if validator.validate_boss_turn(board, monster, player):
        return monster  

def check_boss_area(boss, player):
    area = []
    inside = []
    area_new = []


    for i in range(-3, 4):
        for j in range(-3,4):
            area.append([i, j])

    for i in range(-2, 3):
        for j in range(-2,3):
            inside.append([i, j])

    for position in area:
        if position not in inside:
            area_new.append(position)

    for position in area_new:
        if [boss["position x"] + position[0], boss["position y"] + position[1]] == [player["position x"], player["position y"]]:
            return True
    return False


def move_boss(board, player, boss):
    if check_boss_area(boss, player):
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


def put_boss_on_board(board, boss):
    for j in range(len(boss["icon"])):
        for i in range(len(boss["icon"][0])):
            board[boss["board"]][boss["position y"]+j-2][boss["position x"]+i-2] = boss["icon"][j][i]

    return board

 
def remove_player_from_board(board, player):
    x,y = player['position x'],player['position y']
    board[y][x] = ' '
    return board


def remove_boss_from_board(board, boss):
    for j in range(len(boss["icon"])):
        for i in range(len(boss["icon"][0])):
            board[boss["board"]][boss["position y"]+j-2][boss["position x"]+i-2] = ' '
    return board
    
