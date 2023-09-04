import random
import validator
# put, remove, board, move, fight

def change_direction(board, new_monster_position_x, new_monster_position_y, monster):
    if board[new_monster_position_y][new_monster_position_x] == "🌫️"  and monster["default turn"][0] == -1:
        monster["default turn"][0] = 1
    elif board[new_monster_position_y][new_monster_position_x] == "🌫️"  and monster["default turn"][0] == 1:
        monster["default turn"][0] = -1
    elif board[new_monster_position_y][new_monster_position_x] == "🌫️"  and monster["default turn"][1] == -1:
        monster["default turn"][1] = 1
    elif board[new_monster_position_y][new_monster_position_x] == "🌫️"  and monster["default turn"][1] == 1:
        monster["default turn"][1] = -1
    return monster

def move_monsters(monsters, player, board):
    for monster in monsters:
        if monster["board"] == player["board"]:
            new_monster_position_x = monster["position x"] + monster["default turn"][0]
            new_monster_position_y = monster["position y"] + monster["default turn"][1]
            board = put_monsters_on_board(board, monsters)
            if validator.validate_monster_turn(board[player["board"]], new_monster_position_x, new_monster_position_y):
                remove_monsters_from_board(board[player['board']], monsters)
                monster["position x"] = new_monster_position_x
                monster["position y"] = new_monster_position_y
            change_direction(board[player["board"]], new_monster_position_x, new_monster_position_y, monster)


def attack_boss(player,boss):
    min_boss = -2
    max_boss = 2
    inside = []

    for row in range(min_boss, max_boss + 1):
        for col in range(min_boss, max_boss + 1):
            inside.append([row, col])

    for position in inside:
        x = boss["position x"] + position[0]
        y = boss["position y"] + position[1]
        if [x, y] == [player["position x"], player["position y"]]:
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


# def move_monster(board, player, monster):
#     if abs(player["position x"] - monster["position x"]) == 1 and abs(player["position y"] - monster["position y"]) == 0 or abs(player["position x"] - monster["position x"]) == 1 and abs(player["position y"] - monster["position y"]) == 0:
#         return monster
#     if abs(player["position x"] - monster["position x"]) >= abs(player["position y"] - monster["position y"]):
#         if player["position x"] - monster["position x"] > 0:
#             monster["position x"] += 1
#         else:
#             monster["position x"] -= 1
#     elif abs(player["position y"] - monster["position y"]) >= abs(player["position x"] - monster["position x"]):
#         if player["position y"] - monster["position y"] > 0:
#             monster["position y"] += 1
#         else:
#             monster["position y"] -= 1

#     if validator.validate_boss_turn(board, monster, player):
#         return monster  


def check_boss_neighborhood(boss, player):
    area = []
    interior = []
    neighborhood = []

    min_boss = -2
    max_boss = 2
    min_around_boss = -3
    max_around_boss = 3

    for x in range(min_around_boss, max_around_boss + 1):
        for y in range(min_around_boss, max_around_boss + 1):
            area.append([x, y])

    for x in range(min_boss, max_boss + 1):
        for y in range(min_boss, max_boss + 1):
            interior.append([x, y])

    for position in area:
        if position not in interior:
            neighborhood.append(position)

    for position in neighborhood:
        x = boss["position x"] + position[0]
        y = boss["position y"] + position[1]
        if [x, y] == [player["position x"], player["position y"]]:
            return True
    return False


def move_boss(board, player, boss):
    if check_boss_neighborhood(boss, player):
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
    if boss["condition"] == 0:
        for j in range(len(boss["icon"][0])):
            for i in range(len(boss["icon"][0][0])):
                board[boss["board"]][boss["position y"]+j-2][boss["position x"]+i-2] = boss["icon"][0][j][i]
    elif boss["condition"] == 1:
        for j in range(len(boss["icon"][1])):
            for i in range(len(boss["icon"][1][0])):
                board[boss["board"]][boss["position y"]+j-2][boss["position x"]+i-2] = boss["icon"][1][j][i]

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
    for j in range(len(boss["icon"][0])):
        for i in range(len(boss["icon"][0][0])):
            board[boss["board"]][boss["position y"]+j-2][boss["position x"]+i-2] = ' '
    return board


def put_invetory_on_board(board, items):
    for item in items:
        x, y = item['position x'], item['position y']
        board[item['board']][y][x] = item["icon"]

    return board


def check_free_space(board):
    free_spaces = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(len(board[i][j])):
                if board[i][j][k] == " ":
                    free_spaces[i].append([j, k])
    return free_spaces
