# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 18:43:52 2025

@author: Xhonklei
"""

def update_board(choice, symbol, prev_board):
    '''
    Based on the made choice, the player's turn and on
    the previous board state, update the board.
    ----------
    choice : integer (chosen square)
    symbol : string (X or O)
    prev_board: dict (The dictoniary containing the game board!)

    Returns
    -------
    prev_board: dict (The updated board of the game!)
    '''
    prev_board[choice] = symbol
    return prev_board