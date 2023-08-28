def display_board(board):
    '''
    Displays complete game board on the screen
 
    Returns:
    Nothing
    '''
    for row in board:
        for cell in row:
            print(cell, end='')
        print()  
