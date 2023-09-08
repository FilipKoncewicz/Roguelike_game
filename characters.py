import random
import copy


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    PLAYER_ICON = '🧙'
    PLAYER_START_X = 3
    PLAYER_START_Y = 3

    player_name = input("Enter player's name: ")

    player = {
    "name": player_name,
    "icon": PLAYER_ICON, 
    "position x": PLAYER_START_X,
    "position y": PLAYER_START_Y,
    "board": 0,
    "lives": 10,
    "armor": 0,
    "strength": 10,#1
    "inventory": [],
    "used inventory": []
    }

    return player


def develop_player(icon, player):
    if icon == "🍎":
        player["lives"] += 5
        if player["lives"] > 10:
            player["lives"] = 10
    elif icon == "🥼":
        player["armor"] += 5
        if player["armor"] > 5:
            player["armor"] = 5
    elif icon == "🪄":
        player["strength"] += 2

    return player


def create_monsters(board):
    common_ghost = {
    "name": "ghost",
    "icon": "👻",
    "lives": 2,
    "strength": [0, 1]
    }

    common_mummy = {
    "name": "mummy",
    "icon": "👳", 
    "lives": 4,
    "strength": [0, 2]
    }

    common_bat = {
    "name": "bat",
    "icon": "🦇",
    "lives": 6,
    "strength": [0, 3]
    }

    ghost_1 = {
    **common_ghost,
    "position x": len(board[0][0]) - 3,
    "position y": 1,
    "default turn": [0, 1],
    "board": 0,
    }

    ghost_2 = {
    **common_ghost,
    "position x": 1,
    "position y": int(len(board[0])/2),
    "default turn": [1, 0],
    "board": 0,
    }

    mummy_1 = {
    **common_mummy,
    "position x": len(board[0][0]) - 2,
    "position y": int(len(board[0])/2) + 3,
    "default turn": [-1, 0],
    "board": 0,
    }

    mummy_2 = {
    **common_mummy, 
    "position x": int(len(board[0][0])/2) + 3,
    "position y": len(board[0]) - 2,
    "default turn": [0, -1],
    "board": 1,
    }

    mummy_3 = {
    **common_mummy,
    "position x": 3,
    "position y": 1,
    "default turn": [0, 1],
    "board": 1,
    }

    bat_1 = {
    **common_bat,
    "position x": 1,
    "position y": 2,
    "default turn": [1, 0],
    "board": 1,
    }

    bat_2 = {
    **common_bat,
    "position x": len(board[0][0]) - 2,
    "position y": int(len(board[0])/2) + 3,
    "default turn": [-1, 0],
    "board": 1,
    }

    monsters = [ghost_1, ghost_2, mummy_1, mummy_2, mummy_3, bat_1, bat_2]
    return monsters
                

def create_boss(board):
    BOSS_SIZE = 5
    boss = {
    "name": "boss",
    "icon": [[['👾' for _ in range(BOSS_SIZE)] for _ in range(BOSS_SIZE)], 
             [['👹' for _ in range(BOSS_SIZE)] for _ in range(BOSS_SIZE)]],
    "position x": int(len(board[0][0])/2),
    "position y": int(len(board[0])/2),
    "board": 2,
    "lives": 30,
    "strength": 5,
    "condition": 0,
    "attacks_in_cycle": 0
    }

    return boss


def create_items(free_spaces):
    armor = {
    "icon": "🥼",
    "colected": 0,
    "board": 0,
    "position x": None,
    "position x": None
    }

    wand = {
    "icon": "🪄",
    "colected": 0,
    "board": 1,
    "position x": None,
    "position x": None
    }

    key = {
    "icon": "🗝️",
    "colected": 0,
    "board": 0,
    "position x": None,
    "position x": None
    }

    common_apple = {
    "icon": "🍎",
    "colected": 0,
    "position x": None,
    "position x": None
    }

    apple_1 = {
    **common_apple,
    "board": 0,
    }

    apple_2 = {
    **common_apple,
    "board": 1,
    }

    items = [armor, wand, key, apple_1, apple_2]
    give_position_items(items, free_spaces)

    return items


def give_position_items(items, free_spaces):
    for item in items:
        temp = random.choice(free_spaces[item["board"]])
        item["position y"] = temp[0]
        item["position x"] = temp[1]
        free_spaces[item["board"]].remove(temp)
        print(items)

    return items


