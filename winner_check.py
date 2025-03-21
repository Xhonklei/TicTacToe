# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 18:44:32 2025

@author: Xhonklei
"""

def winner_check(act_board, p1,p2):
    '''
    Based on the board state, and players symbols, check if there 
    is a winning condition if fullfilled or not. If yes, the winner 
    is shown, if not False is shown.
    ----------
    act_board: dict (The dictoniary containing the game board!)
    p1: string (p1 symbol) 
    p2: string (p2 symbol) 

    Returns
    -------
    True, if there is a winner.
    False, if no winner.
    '''

    # Winning conditions
    con1= act_board[1]==act_board[2] == act_board[3] and act_board[1] in ['X','O']
    con2 = act_board[4]==act_board[5] == act_board[6] and act_board[4] in ['X','O']
    con3= act_board[7]==act_board[8] == act_board[9] and act_board[7] in ['X','O']
    con4= act_board[1]==act_board[4] == act_board[7] and act_board[1] in ['X','O']
    con5 = act_board[2]==act_board[5] == act_board[8] and act_board[2] in ['X','O']
    con6= act_board[3]==act_board[6] == act_board[9] and act_board[3] in ['X','O']
    con7 = act_board[1]==act_board[5] == act_board[9] and act_board[1] in ['X','O']
    con8= act_board[3]==act_board[5] == act_board[7] and act_board[3] in ['X','O']

    #Check if any winning combination is achieved and check who wins
    if con1 or con2 or con3 or con4 or con5 or con6 or con7 or con8:
        if (con1 or con4 or con7) and act_board[1] == p1:
            print('First player is Winner!')
        elif (con2) and act_board[4] == p1:
            print('First player is Winner!')
        elif (con3) and act_board[7] == p1:
            print('First player is Winner!')
        elif (con5) and act_board[2] == p1:
            print('First player is Winner!')
        elif(con6 or con8) and act_board[3] == p1:
            print('First player is Winner!')
        else:
            print('Second player is Winner!')
        return True
    else:
        return False