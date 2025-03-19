# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 14:26:24 2025

@author: Xhonklei
"""

from IPython import get_ipython
import time

def symbol_choice():
    '''
    This is the function that allows players to choose the symbol
    that they will have on the game.

    Returns
    -------
    player1 : string
        Used to store the symbol choice of First Player.
    player2 : type
        Used to store the left symbol choice of Second Player.

    '''
    player1 = ''
    player2 = ''
    
    while player1 not in ('X', 'x', 'O', 'o'):
        get_ipython().magic('clear')
        player1 = input('First player please choose your symbol, X or O: ')
        if player1 in ('X', 'x'):
            player1 = 'X'
            player2 = 'O'
            print(f"'{player1}' for first palyer and '{player2}' for second player.")
            print('Game ON')
        elif player1 in ('O', 'o'):
            player1 = 'O'
            player2 = 'X'
            print(f"'{player1}' for first palyer and '{player2}' for second player.")
            print('Game ON')
        else: 
            print('First player please choose between, X and O!')
            time.sleep(5)
    
    return player1, player2
    
a, b = symbol_choice()
# print(f'{a}  {b}')
    