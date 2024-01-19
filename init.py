import keyboard
from os import system, name
from classes.command_board import CommandBoard
import logging
import threading
import time

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


def single_player_start():
    commandBoard = CommandBoard('Start')
    commandBoard.start_single_player_game()
    return '\n\n\n\n\n\n WINEEEERRRRR: '+ commandBoard.winner
    

def close():
    print('Exiting TIC-TAC-TOE')

menu_actions = {
    'Single Player': single_player_start,
    'Multi Player': single_player_start,
    'Options': single_player_start,
    'Exit': close,
}

if __name__ == '__main__':
    position_selected = 0
    position = 0
    option_message = ''

    while position_selected != (len(menu_actions) - 1):
        clear()
        print(option_message)
        option_message = ''
        print(""" 
Select option

{menu_options}
            """.format(menu_options='\n'.join( '{index}) {option} {is_selected}'.format(index=index+1, option=option, is_selected= '<<<<' if position == index else '') for index, option in enumerate(menu_actions.keys()) )))
        key_press = keyboard.read_event(suppress=False)
        if key_press.event_type == keyboard.KEY_UP:
            if key_press.scan_code == 72:
                position -= 1
            elif key_press.scan_code == 80:
                position += 1
            elif key_press.scan_code == 28:
                position_selected = position
                option_message = list(menu_actions.values())[position]()
                position = 0

            board_length = len(menu_actions.keys())
            if position > board_length:
                position =  0
            elif position < 0:
                position =  board_length - 1
