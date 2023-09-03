from colorama import Fore, Back, Style


RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
WHITE = Fore.WHITE
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN


def display_board(board, boss):
    '''
    Displays complete game board on the screen
 
    Returns:
    Nothing
    '''
    for row in board:
        for cell in row:
            if cell == '🌫️':
                print(cell, end = " ")
            elif cell == '🧙':
                print(cell, end = "")
            elif cell == ' ':
                print(WHITE + cell, end = " ")
            elif cell in "👻👳👹️":
                print(cell, end = "")
            elif cell == "👾" and boss["condition"] == 0:
                print(cell, end = "")
            elif cell == "👾" and boss["condition"] == 1:
                print(cell, end = "")
            elif cell == "F":
                print(GREEN + cell, end = " ")
            elif cell in "SA":
                print(WHITE + cell, end = " ")
            elif cell == "K":
                print(YELLOW + cell, end = " ")
        print(Style.RESET_ALL)


def display_board_in_line(board):
    # All in line
    for row in range(len(board[0])):
        for cell in range(len(board[0][0])):
            print(board[0][row][cell], end = " ")
        print(" ", end = "")
        for cell in range(len(board[0][0])):
            print(board[1][row][cell], end = " ")
        print(" ", end = "")
        for cell in range(len(board[0][0])): 
            print(board[2][row][cell], end = " ")
        print(" ", end = "")
        print()


def display_boss_hud(boss):
    print("Boss's lives: ", end = " ") 
    print(boss["lives"])
    print("Boss's defense condition: ", end = " ")
    if boss["condition"] == 0:
        print("weak - Attack boss!")
    else:
        print("strong - Don't attack boss!")


def display_hud(player, boss):
    print("Lives: ", end = " ") 
    print(player["lives"])
    print("Armor: ", end = " ") 
    print(player["armor"])
    print("Inventory: ", end = " ") 
    for item in player["inventory"]:
        print(item, end = " ")
    print()

    if player["board"] == 2:
        display_boss_hud(boss)
        