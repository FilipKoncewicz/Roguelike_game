def display_board(board):
    '''
    Displays complete game board on the screen
 
    Returns:
    Nothing
    '''
    for row in range(len(board[0])):
        for cell in range(len(board[0][0])):
            print(board[0][row][cell], end = "")
        print(" ", end = "")
        for cell in range(len(board[0][0])):
            print(board[1][row][cell], end = "")
        print(" ", end = "")
        for cell in range(len(board[0][0])):
            print(board[2][row][cell], end = "")
        print(" ", end = "")
        print()