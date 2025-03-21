# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 18:45:35 2025

@author: Xhonklei
"""

import boardPrinting as board_print
import symbolChoice as symbol_choice
import player_choice
import update_board
import winner_check
import time 
from IPython import get_ipython

def tic_tac_toe():
    '''
    Makes use of the other functions and develops the logic of the game.
    ----------
    args: None 

    Returns
    -------
    None
    '''
    # This is where the game starts.
    print('Ready to play!')
    print('Keep the positions in mind!')
    # Shows the players each identifier (pos) for each square on board
    # Board is shown as a dictionary with keys identifying squares on the board.
    board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    board_print(board)

    # Initializing board and set of the left squares on the board.
    board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    left_pos = {'1','2','3','4','5','6','7','8','9'}
    
    # Start the game and ask players to make their symbols choices.
    game_on = 'True'
    p1, p2 = symbol_choice()
    time.sleep(5)
    # Show the starting board.
    get_ipython().magic('clear')
    board_print(board)

    # The game start
    while game_on:
        # First player makes the choice
        print("It's first player TURN!")
        p1_choice,left_pos = player_choice(left_pos)
        board = update_board(p1_choice, p1, board)
        get_ipython().magic('clear')
        
        # The updated board is shown
        board_print(board)

        # If first player is the winner stop the game
        if winner_check(board,p1,p2) == True:
            game_on = False
            break
        # If all squares are filled, stop the game
        if len(left_pos) == 0:
            break

        # Same logic for second player.
        print("It's second player TURN!")
        p2_choice,left_pos = player_choice(left_pos)
        board = update_board(p2_choice, p2, board)
        get_ipython().magic('clear')
        board_print(board)
        if winner_check(board,p1,p2) == True:
            game_on = False
            break

    # Check if it was a draw or not.
    if game_on and len(left_pos) == 0:
        print('It is a draw! Thank you for playing!')
    else:
        print('Thank you for playing!')