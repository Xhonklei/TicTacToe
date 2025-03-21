# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 18:40:54 2025

@author: Xhonklei
"""

from IPython import get_ipython

def symbol_choice():
    '''
    Des: This function help the players to choose theirs symbol X or O
    ----
    arg : None

    
    Returns
    -------
    player1: string (p1 symbol) 
    player2: string (p2 symbol) 
    '''
    
    player1 = ''
    player2 = ''
    
    while player1 not in ('X', 'x', 'O', 'o'):
        player1 = input('First player please choose your symbol, X or O: ')
        if player1 in ('X', 'x'):
            player1 = 'X'
            player2 = 'O'
            print(f"'{player1}' for first palyer and '{player2}' for second player.")
            print('Game ON')
        elif player1 in ('O', 'o'):
            print('H2')
            player1 = 'O'
            player2 = 'X'
            print(f"'{player1}' for first palyer and '{player2}' for second player.")
            print('Game ON')
        else:
            get_ipython().magic('clear')
            print('First player please choose between, X and O!')
    
    return player1, player2