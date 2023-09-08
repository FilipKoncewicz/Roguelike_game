def display_board(board):
    '''
    Displays complete game board on the screen
 
    Returns:
    Nothing
    '''
    for row in board:
        for cell in row:
            if cell == ' ':
                print(cell, end = " ")
            else:
                print(cell, end = "")  
        print()


def display_boss_hud(boss):
    if boss['lives'] > 0:
        WEAK = 0
        STRONG = 1

        print(f"Boss's lives: {boss['lives']}") 
        
        print("Boss's defense condition: ", end = " ")
        if boss["condition"] == WEAK:
            print("WEAK - Attack boss!")
        elif boss["condition"] == STRONG:
            print("STRONG - Don't attack boss!")


def display_hud(player, boss, monsters):
    print(f"Player's name: {player['name']}")
    print(f"Lives: {player['lives'] * '❤️'}") 
    print(f"Armor: {player['armor'] * '🛡️'}")
    print(f"Strength: {player['strength']}")
    print(f"Points: {player['points']}")

    print("Inventory:", end = " ") 
    for item in player["inventory"]:
        print(item, end = " ")
    print()

    print("Used inventory: ", end = " ") 
    for item in player["used inventory"]:
        print(item, end = " ")
    print()

    if player["board"] == boss["board"]:
        display_boss_hud(boss)