import numpy as np
from utils import *
from art import game_art


def game_loop():
    
    # Fill gameboard
    gameboard = np.full((6,7), 'O')
    game_active = True
    
    # Get valid starting player colour
    valid_input = False
    while not valid_input:
        player = input("Welcome! Player one, what colour do you want? Enter 'B' or 'R': ")
        if player == 'R' or player == 'B':
            valid_input = True
        else:
            print("Invalid input, please enter 'B' or 'R'\n" )
            
    # Main game loop
    while game_active:
        clear()
        print(game_art)
        print(gameboard)
        
        # Player makes turn, code checks for winning conditions.
        get_turn(gameboard, player)
        if(check_win_condition(gameboard, player)):
            clear()
            print(game_art)
            print(f"{'Red player' if player == 'R' else 'Blue player'} wins!")
            print("Final board: ")
            print(gameboard)
            game_active = False
        elif(check_draw_condition(gameboard)):
            clear()
            print(game_art)
            print("No move more moves left. Draw!")
            print("Final board: ")
            print(gameboard)
            game_active = False
            
        # Swap players.
        player = swap_player(player)
