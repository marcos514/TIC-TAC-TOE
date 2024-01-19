import keyboard
from classes.board import Board
from copy import deepcopy
import os

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux
    else:
        _ = os.system('clear')

class CommandBoard(Board):
    # @property
    # def x(self):
    #     """I'm the 'x' property."""
    #     return self._x
    def __init__(self, board_type):
        super().__init__(board_type)
        self.position = 0
        
    def start_single_player_game(self):
        self.draw_board()
        while not self.winner:
            key_press = keyboard.read_event(suppress=False)
            self.key_press_callback(key_press)
    
    def start_basic_multiplayer_game(self):
        self.draw_board()
        while not self.winner:
            key_press = keyboard.read_event(suppress=False)
            self.key_press_callback(key_press)
    
    def set_symbol(self):
        board_status = super().set_symbol(self.position)
        return board_status

    def key_press_callback(self, key_press):
        # keyboard.on_release_key(72, callback) # up
        # keyboard.on_release_key(75, callback) # left
        # keyboard.on_release_key(77, callback) # right
        # keyboard.on_release_key(80, callback) # down
        # keyboard.on_release_key(28, callback) # enter
        if key_press.event_type == keyboard.KEY_UP:
            if not self.winner:
                if key_press.scan_code == 72:
                    self.position -= 3
                elif key_press.scan_code == 75:
                    if not(self.position % 3):
                        self.position +=2
                    else:
                        self.position -= 1
                elif key_press.scan_code == 77:
                    if (self.position % 3) == 2:
                        self.position -=2
                    else:
                        self.position += 1
                elif key_press.scan_code == 80:
                    self.position += 3
                elif key_press.scan_code == 28:
                    self.set_symbol()
                    self.position = 0

            if key_press.scan_code == 1:
                self.winner = 'Draw'
        
        # create horizontal teleport not move to top row
        board_length = len(self.board) - 1
        if self.position > board_length:
            self.position =  self.position - board_length - 1
        elif self.position < 0:
            self.position =  board_length + self.position +1
        self.draw_board()



    def draw_board(self):
        clear()
        aux_board = list(self.board)
        aux_board[self.position] = self.player_turn
        first_row = aux_board[:3]
        second_row = aux_board[3:6]
        third_row = aux_board[6:]
        line_divider = '\n-----\n'
        print('|'.join(first_row)+ line_divider+'|'.join(second_row)+ line_divider +'|'.join(third_row))
        if self.winner:
            if self.winner == 'Draw':
                print('Its a Draw')
            else:
                print('Winner is Player: ' + self.player_turn)
        else:
            print('Player Turn: ' + self.player_turn)
        
    # initializes all the 10 spaces with None
# b = [None] * 8
# print("Creating empty list of None: ", b)
 
# # initializes all the 10 spaces with A's
# c =  [[0] * 4] * 3
# print("Creating 2D empty list of zeros: ", c)



# X|-|X
# -----
# O|X|-
# -----
# O|-|-