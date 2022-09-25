# from enum import Enum
# class Color(Enum):
#     INGAME = 1
#     WINNER = 2
#     DRAW = 3

class Board:
    players_options = ('X', 'O')
     # create the other way to validate this, divide this into other arrays
    simple_array_winners = (
        {
            'is_variable': True,
            'x_steps': 3,
            'y_steps': 1,
        }, {
            'is_variable': True,
            'x_steps': 1,
            'y_steps': 3,
        },{
            'start_position': 0,
            'is_variable': False,
            'x_steps': 1,
            'y_steps': 4,
        },{
            'start_position': 2,
            'is_variable': False,
            'x_steps': 1,
            'y_steps': 2,
        }
    )

    # class instance
    def __init__(self, board_type):
        self.board_type = board_type
        self.reset()
    
    def reset(self):
        self.status = 'in game'
        self.board = ['-'] * 9
        self.player = 'X'
        self.player_turn = 'X'
        self.winner = None

    def is_position_available(self, position):
        # when using the board_types check with one I am using
        return self.board[position] == '-'

    def set_symbol(self, position):
        if not self.is_position_available(position):
            return False
        self.board[position] =  self.player_turn
        status = self.validate_board_status()
        if status and not self.winner:
            self.change_player()
        return status

    def change_player(self):
        self.player_turn = self.players_options[1 - self.players_options.index(self.player_turn)]

    def validate_board_status(self):
        for winner_route in self.simple_array_winners:
            for start_position in [0, 1, 2] if winner_route['is_variable'] else [winner_route['start_position']]:
                first = self.board[start_position * winner_route['x_steps']]
                second = self.board[start_position* winner_route['x_steps'] + winner_route['y_steps'] ]
                third = self.board[start_position * winner_route['x_steps'] + winner_route['y_steps'] *2 ]
                if first + second + third == self.player_turn * 3:
                    self.winner = self.player_turn
                    break
            if self.winner:
                break

        if self.winner != None:
            self.status = 'end'
        elif '-' not in self.board:
            self.status = 'end'
            self.winner = 'draw'

        return True


    # initializes all the 10 spaces with None
# b = [None] * 8
# print("Creating empty list of None: ", b)
 
# # initializes all the 10 spaces with A's
# c =  [[0] * 4] * 3
# print("Creating 2D empty list of zeros: ", c)



        """ 
            First solution to TIC TAC TOE
            X + Y * Z
            X = start position
            Y = steps
            Z = tic tac or toe
        """
