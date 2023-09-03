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

    player_name = "l"# input("Enter player's name: ")

    player = {
    "name": player_name,
    "icon": PLAYER_ICON, 
    "position x": PLAYER_START_X,
    "position y": PLAYER_START_Y,
    "board": 0,
    "lives": 10,
    "armor": 0,
    "strength": 1,
    "inventory": []
    }

    return player


def create_monsters(board):
    ghost_1 = {
    "name": "ghost 1",
    "icon": "👻",
    "position x": len(board[0][0]) - 3,
    "position y": 1,
    "default turn": [0, 1],
    "board": 0,
    "lives": 2,
    "strength": [0, 1]
    }

    ghost_2 = {
    "name": "ghost 2",
    "icon": "👻",
    "position x": 1,
    "position y": int(len(board[0])/2),
    "default turn": [1, 0],
    "board": 0,
    "lives": 2,
    "strength": [0, 1]
    }

    mummy_1 = {
    "name": "mummy 1",
    "icon": "👳", 
    "position x": len(board[0][0]) - 2,
    "position y": int(len(board[0])/2) + 3,
    "default turn": [-1, 0],
    "board": 0,
    "lives": 4,
    "strength": [1, 2]
    }

    mummy_2 = {
    "name": "mummy 2",
    "icon": "👳", 
    "position x": int(len(board[0][0])/2) + 3,
    "position y": len(board[0]) - 2,
    "default turn": [0, -1],
    "board": 1,
    "lives": 4,
    "strength": [1, 2]
    }

    mummy_3 = {
    "name": "mummy 3",
    "icon": "👳", 
    "position x": 3,
    "position y": 1,
    "default turn": [0, 1],
    "board": 1,
    "lives": 4,
    "strength": [1, 2]
    }

    demon_1 = {
    "name": "demon 1",
    "icon": "👹",
    "position x": 1,
    "position y": 2,
    "default turn": [1, 0],
    "board": 1,
    "lives": 6,
    "strength": [2, 3]
    }

    demon_2 = {
    "name": "demon 2",
    "icon": "👹",
    "position x": len(board[0][0]) - 2,
    "position y": int(len(board[0])/2) + 3,
    "default turn": [-1, 0],
    "board": 1,
    "lives": 6,
    "strength": [2, 3]
    }

    monsters = [ghost_1, ghost_2, mummy_1, mummy_2, mummy_3, demon_1, demon_2]

    return monsters
                

def create_boss(board):
    boss = {
    "name": "boss",
    "icon": [['👾', '👾', '👾', '👾', '👾'], ['👾', '👾', '👾', '👾', '👾'], ['👾', '👾', '👾', '👾', '👾'], ['👾', '👾', '👾', '👾', '👾'], ['👾', '👾', '👾', '👾', '👾']],
    #"icon": '%',
    "position x": int(len(board[0][0])/2),
    "position y": int(len(board[0])/2),
    "board": 2,
    "lives": 30,
    "strength": 5,
    "condition": 0,
    "attacks_in_cycle": 0
    }

    return boss

def create_items(board):
    armor = {
    "name": "Armor",
    "icon": "🥼",
    "position x": int(len(board[0][0])/2) + 3,
    "position y": len(board[0]) - 2,
    "default turn🪄": [0, 1],
    "board": 0,
    }
    wand = {
    "name": "Wand",
    "icon": "🪄",
    "position x": int(len(board[0][0])/2) + 6,
    "position y": len(board[0]) - 11,
    "default turn": [0, 1],
    "board": 1,
    }

    items =[armor,wand]

    return items