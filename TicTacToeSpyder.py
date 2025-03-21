# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 18:10:19 2025

@author: Xhonklei
"""
def board_print(border_choice):
    '''
    Pass combined choices made by players on board.
    ----------
    border_choice : dictionary
        This is the function to print the game board. 
        By passing the choices made by players, the board changes its shape!

    Returns
    -------
    None.
    '''
    em_row= '     |     |     '
    border = '-'*17
    print(em_row)
    print(f'  {border_choice[1]}  |  {border_choice[2]}  |  {border_choice[3]}  ')
    print(em_row)
    print(border)
    print(em_row)
    print(f'  {border_choice[4]}  |  {border_choice[5]}  |  {border_choice[6]}  ')
    print(em_row)
    print(border)
    print(em_row)
    print(f'  {border_choice[7]}  |  {border_choice[8]}  |  {border_choice[9]} ')
    print(em_row)

#------------------------------------------------------
from IPython import get_ipython

def symbol_choice():
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
#-----------------------------------------------------
def player_choice(left_pos):
    choice = 'Empty'
    while choice not in left_pos:
        choice = input('Please choose an avaliable square on board: ')
        if choice not in left_pos:
            print(f'Choose a square in {left_pos}!')
    #Update left squares on the board
    left_pos.discard(choice)
    return int(choice),left_pos  

#----------------------------------------------------------
def update_board(choice, symbol, initial_b):
    initial_b[choice] = symbol
    return initial_b
#----------------------------------------------------
def winner_check(act_board, p1,p2):
    con1= act_board[1]==act_board[2] == act_board[3] and act_board[1] in ['X','O']
    con2 = act_board[4]==act_board[5] == act_board[6] and act_board[4] in ['X','O']
    con3= act_board[7]==act_board[8] == act_board[9] and act_board[7] in ['X','O']
    con4= act_board[1]==act_board[4] == act_board[7] and act_board[1] in ['X','O']
    con5 = act_board[2]==act_board[5] == act_board[8] and act_board[2] in ['X','O']
    con6= act_board[3]==act_board[6] == act_board[9] and act_board[3] in ['X','O']
    con7 = act_board[1]==act_board[5] == act_board[9] and act_board[1] in ['X','O']
    con8= act_board[3]==act_board[5] == act_board[7] and act_board[3] in ['X','O']

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
#-----------------------------------------------------------
import time 

def tic_tac_toe():
    print('Ready to play!')
    print('Keep the positions in mind!')
    board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    board_print(board)
    board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    left_pos = {'1','2','3','4','5','6','7','8','9'}
    
    
    game_on = 'True'
    p1, p2 = symbol_choice()
    time.sleep(5)
    get_ipython().magic('clear')
    board_print(board)
    
    while game_on:
        print("It's first player TURN!")
        p1_choice,left_pos = player_choice(left_pos)
        board = update_board(p1_choice, p1, board)
        get_ipython().magic('clear')
        board_print(board)
        if winner_check(board,p1,p2) == True:
            game_on = False
            break
        if len(left_pos) == 0:
            break
        print("It's second player TURN!")
        p2_choice,left_pos = player_choice(left_pos)
        board = update_board(p2_choice, p2, board)
        get_ipython().magic('clear')
        board_print(board)
        if winner_check(board,p1,p2) == True:
            game_on = False
            break
    
    if game_on and len(left_pos) == 0:
        print('It is a draw! Thank you for playing!')
    else:
        print('Thank you for playing!')


tic_tac_toe()