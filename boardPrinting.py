# -*- coding: utf-8 -*-
"""
18/03/2025

Created by Xhonklei Hoxha
"""

def border_print(border_choice):
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

initial_board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
border_print(initial_board)
