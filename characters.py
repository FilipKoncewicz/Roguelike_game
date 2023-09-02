def create_monsters(board):
    spider_1 = {
    "name": "spider 1",
    "icon": "X", 
    "position x": len(board[0][0]) - 3,
    "position y": 1,
    "board": 0,
    "lives": 2,
    "strength": [0, 1]
    }

    spider_2 = {
    "name": "spider 2",
    "icon": "X", 
    "position x": 1,
    "position y": int(len(board[0])/2),
    "board": 0,
    "lives": 2,
    "strength": [0, 1]
    }

    mummy_1 = {
    "name": "mummy_1",
    "icon": "M", 
    "position x": len(board[0][0]) - 2,
    "position y": int(len(board[0])/2) + 3,
    "board": 0,
    "lives": 4,
    "strength": [1, 2]
    }

    mummy_2 = {
    "name": "mummy_2",
    "icon": "M", 
    "position x": int(len(board[0][0])/2) + 3,
    "position y": len(board[0]) - 2,
    "board": 1,
    "lives": 4,
    "strength": [1, 2]
    }

    mummy_3 = {
    "name": "mummy_3",
    "icon": "M", 
    "position x": 3,
    "position y": 1,
    "board": 1,
    "lives": 4,
    "strength": [1, 2]
    }

    zombie_1 = {
    "name": "zombie_1",
    "icon": "Z", 
    "position x": 1,
    "position y": 2,
    "board": 1,
    "lives": 6,
    "strength": [2, 3]
    }

    zombie_2 = {
    "name": "zombie_2",
    "icon": "Z", 
    "position x": len(board[0][0]) - 2,
    "position y": int(len(board[0])/2) + 3,
    "board": 1,
    "lives": 6,
    "strength": [2, 3]
    }

    monsters = [spider_1, spider_2, mummy_1, mummy_2, mummy_3, zombie_1, zombie_2]

    return monsters
                

def create_boss(board):
    boss = {
    "name": "boss",
    "icon": [['%', '%', '%', '%', '%'], ['%', '%', '%', '%', '%'], ['%', '%', '%', '%', '%'], ['%', '%', '%', '%', '%'], ['%', '%', '%', '%', '%']],
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