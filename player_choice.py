# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 18:42:36 2025

@author: Xhonklei
"""

def player_choice(left_pos):
    '''
    Based on the left squares on the board, a player choose where
    to palce it symbol. Remove the taken square from left_pos
    ----------
    left_pos : set
        This set contains all the avaliable squares on the board.
        Start with left_pos = {'1', '2',....,'9'}

    Returns
    -------
    choice: As an integer, the taken square
    left_pos: The updated set of left squares
    '''
    choice = 'Empty'
    while choice not in left_pos:
        choice = input('Please choose an avaliable square on board: ')
        if choice not in left_pos:
            print(f'Choose a square in {left_pos}!')
    #Update left squares on the board
    left_pos.discard(choice)
    return int(choice),left_pos 