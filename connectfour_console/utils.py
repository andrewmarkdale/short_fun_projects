import os

def get_turn(gameboard, player):
    """Returns gameboard with piece at the appropriate location"""
    valid_input = False
    while not valid_input:
        column = input(f"\n{'Red' if player == 'R' else 'Blue'}"
                           + " player where would you like to put your piece? [0-6]: ")
        if (column.isnumeric() 
            and int(column) >= 0 
            and int(column) < len(gameboard[0]) 
            and gameboard[0][int(column)] == 'O'):
            
            valid_input = True
            column = int(column)
        else: 
            print("Invalid entry, please try again.")
    
    return place_piece(gameboard, column, player)

def place_piece(gameboard, column, player):
    """Places piece at appropriate location and returns the resulting gameboard."""
    for i in range(1, len(gameboard)+1):
        if gameboard[-i][column] == 'O':
            gameboard[-i][column] = 'R' if player == 'R' else 'B'
            break
    return gameboard

def swap_player(player):
    """Swaps current player."""
    if player == 'R':
        return 'B'
    else:
        return 'R'
    
    
def check_row(gameboard, player):
    """Checks rows for win condition"""
    for r in range(len(gameboard)):
        for c in range(len(gameboard)-3):
            if (gameboard[r][c] 
                == gameboard[r][c+1] 
                == gameboard[r][c+2] 
                == gameboard[r][c+3] 
                == player):
                return True
    return False

def check_column(gameboard, player):
    """Checks columns for win condition."""
    for c in range(len(gameboard)):
        for r in range(len(gameboard)-3):
            if (gameboard[r][c] 
                == gameboard[r+1][c] 
                == gameboard[r+2][c] 
                == gameboard[r+3][c] 
                == player):
                return True         
    return False

def check_negative_diagonal(gameboard, player):
    """Checks for negative diagonal win condition."""
    for r in range(len(gameboard)-3):
        for c in range(len(gameboard)-2):
            if(gameboard[r][c]
               == gameboard[r+1][c+1]
               == gameboard[r+2][c+2]
               == gameboard[r+3][c+3]
               == player):
                return True
    return False

def check_positive_diagonal(gameboard, player):
    """Checks for positive diagonal win condition."""
    for r in range(len(gameboard)-3):
        for c in range(len(gameboard)-2):
            if(gameboard[-r-1][c]
               == gameboard[-r-2][c+1]
               == gameboard[-r-3][c+2]
               == gameboard[-r-4][c+3]
               == player):
                return True
    return False

def check_win_condition(gameboard, player):
    """Checks for win condition from row, column and positive/negative diagonal"""
    if check_row(gameboard, player):
        return True
    if check_column(gameboard, player):
        return True
    if check_negative_diagonal(gameboard, player):
        return True
    if check_positive_diagonal(gameboard, player):
        return True
    return False


def check_draw_condition(gameboard):
    """Checks for draw condition."""
    for i in range(len(gameboard)):
        for j in range(len(gameboard)):
            if gameboard[i][j] == 'O':
                return False
    return True

def clear():
    """Clears screen for cleaner gameplay."""
    os.system('cls' if os.name == 'nt' else 'clear')