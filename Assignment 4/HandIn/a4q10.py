# Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT317 A4Q10

# This file includes all the script from A4Q1 - A4Q9
# All the script from previous question must run using this file

# Need to import the numpy to create the game board
from numpy import full

# Need to import the copy to deep copy
import copy as copy

# import the namedtuple for naming the state
from collections import namedtuple

# import the random in depth cutoff function
import random as random

# import the time for count time
import time as time


# Game state contains a player, utility, and game board
# Game state is used in the Game for showing player, utility, board
GameState = namedtuple('GameState', 'player, utility, board')

# set infinity as infinity
infinity = float('inf')


# This is the Board of the Game, and it can create a board and check if the queen is safety
class Board(object):

    # Initialize the Board, which contains the variables:
    # size: from user input, for board size which make N * N Game board
    # board: using full function from numpy lib to create a board
    # front_slash_lookup: for checking the right-side diagonal if placed Queen is attacked
    # back_slash_lookup: for checking the left-side diagonal if placed Queen is attacked
    # row_lookup: for checking the row if the placed Queen is attacked
    # col_lookup: for checking the col if the placed Queen is attacked
    def __init__(self, size):

        self.size = size
        self.board = full((size, size), False)

        self.front_slash_lookup = full((size * 2 - 1), False)
        self.back_slash_lookup = full((size * 2 - 1), False)
        self.row_lookup = full(size, False)
        self.col_lookup = full(size, False)

    # get_board() function
    # returns a copy the current board
    def get_board(self):
        return copy.deepcopy(self.board)

    # get the board size
    # returns the size of current board
    def get_board_size(self):
        return self.size

    # To place a new Queen on the board by the position (row, col)
    def place_a_queen(self, row, col):
        # to place the new Queen on the board
        # Need to setup all the variables in the board
        # (board, row_lookup, col_lookup, front_slash_lookup, back_slash_lookup)
        # on the position (row, col) has to be True
        self.board[row][col] = True
        self.row_lookup[row] = True
        self.col_lookup[col] = True
        self.front_slash_lookup[col + row] = True
        self.back_slash_lookup[row - col + (self.size - 1)] = True

    # is_safe() by using variables (row, col)
    # to check if the position (row, col) is safe to place a Queen
    def is_safe(self, row, col):
        # if all the variables in the Board are not False on the position
        # then return True
        return (
                not self.front_slash_lookup[row + col] and
                not self.back_slash_lookup[row - col + (self.size - 1)] and
                not self.row_lookup[row] and
                not self.col_lookup[col]
        )

    # print_board function
    # to print the current board
    def print_board(self):
        for i in range(self.size):
            print('', end='')
        print('')
        for i in range(self.size):
            for j in range(self.size):
                print('Q' if self.board[i][j] else 'X', end=' ')
            print(' ')

    # count_queen() function for count how many queens on the current board
    # return a number that current queens
    def count_queen(self):
        counter = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]:
                    counter += 1
                else:
                    counter += 0
        return counter

    # no_queen_row() function for getting which row has not been placed a queen
    # return a list of number of which col has no queen
    def no_queen_col(self):
        non_queen_col = []
        for i in range(self.size):
            if not self.col_lookup[i]:
                non_queen_col.append(i)
        return non_queen_col

    # get_queen_position(), take the variable col
    # to find which position constrains a queen on the given column
    # return a position x, y
    def get_queen_position(self, col):
        queen_pos = None
        for i in range(self.size):
            if self.board[i][col]:
                queen_pos = col, i

        return queen_pos


# This Move class contains x, y
# Which x is row, y is col
# (x,y) is a  position of the game board
class Move(object):

    # variable x, y are the position number
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # for printing
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


# the Game class for Variation 1a (Problem class)
class Variation1AGame(object):

    # initialize the game board and a game state by using user-given "size"
    def __init__(self, size):
        self.initial = GameState('p1', 0, Board(size))
        self.size = size

    # function actions() need a state variable
    # return a list of actions (moves) which are legal in the given state
    # the function needs to examine the state to determine whose turn it is to move
    def actions(self, state: GameState):

        # action list
        action = []

        # if there are no more row or col to move, then return the empty list
        # because there are no movement can do
        if not state.board.no_queen_col():
            # action.append((self.finish, state.player))
            return action

        # else there does have more row or col to move, then
        else:
            # if the state player is p1, then check if there are still have legal movement
            # if so, append it to the action
            # if not, then return the emtpy list
            if state.player == 'p1':
                j = state.board.no_queen_col()[0]
                for i in range(state.board.size):
                    if state.board.is_safe(i, j):
                        new_move = Move(j, i)
                        action.append(new_move)
                return action

            # if the state player is p2, then check if there are still have legal movement
            # if so, append it to the action
            # if not, then p2 lose, return the empty list
            elif state.player == 'p2':
                j = state.board.no_queen_col()[0]
                for i in range(state.board.size):
                    if state.board.is_safe(i, j):
                        new_move = Move(j, i)
                        action.append(new_move)
                return action
        return action

    # return a new game state which is the result of taking the given action is the given state
    # state: GameState
    # action: an action move
    def result(self, state, action):

        # the movement from the action
        movement = action

        # we need to switch the player first, because a player can only place a queen once
        if state.player == 'p1':
            player = 'p2'
        else:
            player = 'p1'

        # if the action is empty, then calculate the state utility (since it should be terminal right now)
        if not action:
            utility = self.utility(state)
            new_state = GameState(player=player, utility=utility, board=state.board)

        # if not empty, then place a queen on the board by using movement that action gives
        else:
            utility = self.utility(state)
            new_board = copy.deepcopy(state.board)
            new_board.place_a_queen(movement.y, movement.x)
            new_state = GameState(player=player, utility=utility, board=new_board)

        return new_state

    # for utility function: return a numeric value
    # the state must be a terminal state
    def utility(self, state: GameState):
        # if the state is not terminal, then print it, and return 0
        if not self.is_terminal(state):
            # print("it is not terminal state")
            return 0

        # if the state game board has not more space to place
        # which means that the last placed player win, we need just check that
        if not state.board.no_queen_col():
            # if the board size is even, then the player 2 win
            if state.board.size % 2 == 0:
                return -1
            # if the board size is odd, then p1 win
            else:
                return 1

        # if the state game board has enough space, but it can not place more legal room
        # then we have to find the last legal move player
        if state.board.no_queen_col():

            # need to get the previous player:

            if state.player == 'p1':
                return -1
            else:
                return 1

        return 0

    # return a boolean. True if the given state has no more legal moves
    def is_terminal(self, state:GameState):
        # if the action list is empty, which means the state is terminal
        if not self.actions(state):
            return True
        else:
            return False

    # to show the state
    def display(self, state: GameState):
        print(state)

    def player(self, state: GameState):
        return state.player

    # Returns a boolean value
    # True if it's player 1's turn(max) in the given state
    def is_max_turn(self, state: GameState):
        if state.player == 'p1':
            return True
        else:
            return False

    # Returns a boolean value
    # True if it's player 2 's turn (min) in the given state
    def is_min_turn(self, state: GameState):
        if state.player == 'p2':
            return True
        else:
            return False

    # return a boolean. True if the search should be terminated at this state and depth
    def cutoff_test(self, state: GameState, depth):
        return state.board.size - state.board.no_queen_col()[0] > depth

    # returns an estimate of the Minimax value of the given state
    # Alternatively, your evaluation function can return a random utility value. This is easy
    # to start with, in any case.
    def eval(self, state: GameState):
        # if the state is terminal, then return the utility
        if self.is_terminal(state):
            return self.utility(state)
        # else, return a random num(win/lose) and action
        num = random.choice([1, -1])
        actions = self.actions(state)
        a_action = random.sample(actions, 1)[0]
        return num, a_action

    # print out
    def __repr__(self):
        return'<{}>'.format(self.__class__.__name__)


# the Game class for Variation 1b (Problem class)
class Variation1BGame(object):

    # initialize the game board and a game state by a user-given size
    def __init__(self, size):
        self.initial = GameState('p1', 0, Board(size))
        self.size = size

    # actions() function
    # return a list of actions (moves) which are legal in the given state
    # the function needs to examine the state to determine whose turn it is to move
    def actions(self, state: GameState):

        # action list
        action = []

        # if there are no more row or col to move, then return the empty list
        # because there are no movement can do
        if not state.board.no_queen_col():
            # action.append((self.finish, state.player))
            return action

        # else if there still have legal room to place
        else:
            # if the state player is p1, then check if there are still have legal movement
            # if so, append it to the action
            # if not, then return the emtpy list
            if state.player == 'p1':
                j = state.board.no_queen_col()[0]
                for i in range(state.board.size):
                    if state.board.is_safe(i, j):
                        new_move = Move(j, i)
                        action.append(new_move)
                return action
            # if the state player is p2, then check if there are still have legal movement
            # if so, append it to the action
            # if not, then p2 lose, return the empty list
            elif state.player == 'p2':
                j = state.board.no_queen_col()[0]
                for i in range(state.board.size):
                    if state.board.is_safe(i, j):
                        new_move = Move(j, i)
                        action.append(new_move)
                return action
        return action

    # return a new game state which is the result of taking the given action is the given state
    def result(self, state, action):

        # the movement from the action
        movement = action

        # we need to switch the player first, because a player can only take a movement once
        if state.player == 'p1':
            player = 'p2'
        else:
            player = 'p1'

        # calculate the state utility
        if not action:
            utility = self.utility(state)
            new_state = GameState(player=player, utility=utility, board=state.board)

        # if not empty, then place a movement on the board
        else:

            utility = self.utility(state)
            new_board = copy.deepcopy(state.board)
            new_board.place_a_queen(movement.y, movement.x)
            new_state = GameState(player=player, utility=utility, board=new_board)
        return new_state

    # for v2 utility function: return a numeric value (the score)
    # the state must be a terminal state
    def utility(self, state: GameState):
        # the score k
        k = 1
        # if the state is not terminal, then print it, and return 0
        if not self.is_terminal(state):
            # print("it is not terminal state")
            return 0

        # if the state game board has not more space to place
        # which means that the last placed player win, we need just check that
        if not state.board.no_queen_col():
            # if the board size is even, then the player 2 win
            if state.board.size % 2 == 0:
                # the k must be a negative and calculated
                k = -1 * state.board.size / 2
            # if the board size is odd, then p1 win
            else:
                # the k must be a positive and calculated
                k = (state.board.size + 1) / 2

        # if the state game board has enough space, but it can not place more legal room
        # then we have to find the last legal move player
        if state.board.no_queen_col():

            # need to get the previous player:
            if state.player == 'p1':
                # calculate the k
                k = -1 * ((state.board.size - len(state.board.no_queen_col()))/2 + 1)
            else:
                k = (state.board.size - len(state.board.no_queen_col()) + 1)/2

        return int(k)

    # return a boolean. True if the given state has no more legal moves
    def is_terminal(self, state:GameState):
        # if the action list is empty, which means the state is terminal
        if not self.actions(state):
            return True
        else:
            return False

    # to show the state
    def display(self, state: GameState):
        print(state)

    def player(self, state: GameState):
        return state.player

    # Returns a boolean value
    # True if it's player 1's turn(max) in the given state
    def is_max_turn(self, state: GameState):
        if state.player == 'p1':
            return True
        else:
            return False

    # Returns a boolean value
    # True if it's player 2 's turn (min) in the given state
    def is_min_turn(self, state: GameState):
        if state.player == 'p2':
            return True
        else:
            return False

    # return a boolean. True if the search should be terminated at this state and depth
    def cutoff_test(self, state: GameState, depth):

        return state.board.size - state.board.no_queen_col()[0] > depth

    # returns an estimate of the Minimax value of the given state
    # Alternatively, your evaluation function can return a random utility value. This is easy
    # to start with, in any case.
    def eval(self, state: GameState):
        # is the state is terminal, then returns the utility
        if self.is_terminal(state):
            return self.utility(state)
        # else, return a random value that from max score to min score
        num = random.choice([state.board.size/2, -state.board.size/2])
        actions = self.actions(state)
        a_action = random.sample(actions, 1)[0]
        return int(num), a_action

    # print out
    def __repr__(self):
        return'<{}>'.format(self.__class__.__name__)


# A4Q1
# To implement Minimax Search for Variation 1a
class MiniMaxSearchV1A(object):
    # initialize the search, which size is the board size
    # initialize the Variation1AGame, and get the initial state
    def __init__(self, size):
        self.size = size
        self.game = Variation1AGame(size)
        self.state = self.game.initial

    # max_value() function for a4q1
    # returns the best max value of current state
    def max_value(self, a_state: GameState):
        # if the game is terminal then the best must be the utility value
        if self.game.is_terminal(a_state):
            best = self.game.utility(a_state)
        # if the game is not terminal, then the best is the -inf
        # and for all the actions that state can do, find the largest one by using min_value()
        # return the best
        else:
            # for A4Q8 change the scale
            # best = -1
            best = -infinity
            for act in self.game.actions(a_state):
                val = self.min_value(self.game.result(a_state, act))
                if val > best:
                    best = val
        return best

    # min value() function for a4q1
    def min_value(self, a_state: GameState):
        # if the game is terminal then the best must be the utility value
        if self.game.is_terminal(a_state):
            best = self.game.utility(a_state)
        # if the game is not terminal, then the best is the inf
        # and for all the actions that state can do, find the smallest one by using max_value()
        # return the best
        else:
            # for A4Q8 change the scale
            # best = 1
            best = infinity
            for act in self.game.actions(a_state):
                val = self.max_value(self.game.result(a_state, act))
                if val < best:
                    best = val
        return best

    # min max decision function for a4q1
    # returns the best_value, best_action, and time_consume
    def minimax_decision(self, a_state: GameState):
        # count time
        start_time = time.time()
        # the best action
        best_action = None
        # the best value
        best = 0

        # if it's the max_turn, then using the min_value() to find the largest one
        # then get the best value and best action
        if self.game.is_max_turn(a_state):
            # for A4Q8 change the scale
            # best = -1
            best = -infinity
            for act in self.game.actions(a_state):
                new_state = self.game.result(a_state, act)
                val = self.min_value(new_state)
                if val > best:
                    best = val
                    best_action = act
        # if it's the min_turn, then using the max_value() to find the smallest one
        # then get the best value and best action
        elif self.game.is_min_turn(a_state):
            # for A4Q8 change the scale
            # best = -1
            best = infinity
            for act in self.game.actions(a_state):
                new_state = self.game.result(a_state,act)
                val = self.max_value(new_state)
                if val < best:
                    best = val
                    best_action = act
        now = time.time()
        # return best_value, best action, and time consummation
        return best, best_action, now-start_time


# A4Q2
# To implement Minimax Search for Variation 1a
class MiniMaxSearchV1B(object):
    # initialize the search, which size is the board size
    # initialize the Variation1AGame, and get the initial state
    def __init__(self, size):
        self.size = size
        self.game = Variation1BGame(size)
        self.state = self.game.initial

    # max value function for a4q2
    # returns the best max value of current state
    def max_value(self, a_state: GameState):
        # if the game is terminal then the best must be the utility value
        if self.game.is_terminal(a_state):
            best = self.game.utility(a_state)
        # if the game is not terminal, then the best is the -inf
        # and for all the actions that state can do, find the largest one by using min_value()
        # return the best
        else:
            # for A4Q8 change the scale
            # best = -1
            best = -infinity
            for act in self.game.actions(a_state):
                val = self.min_value(self.game.result(a_state, act))
                if val > best:
                    best = val
        return best

    # min value function for a4q1
    def min_value(self, a_state: GameState):
        # if the game is terminal then the best must be the utility value
        if self.game.is_terminal(a_state):
            best = self.game.utility(a_state)
        # if the game is not terminal, then the best is the inf
        # and for all the actions that state can do, find the min one by using max_value()
        # return the best
        else:
            # for A4Q8 change the scale
            # best = 1
            best = infinity
            for act in self.game.actions(a_state):
                val = self.max_value(self.game.result(a_state, act))
                if val < best:
                    best = val
        return best

    # min max decision function for a4q2
    # returns the best_value, best_action, and time_consume
    def minimax_decision(self, a_state: GameState):
        # count time
        start_time = time.time()
        # the best action
        best_action = None
        # the best value
        best = 0

        # if it's the max_turn, then using the min_value() to find the largest one
        # then get the best value and best action
        if self.game.is_max_turn(a_state):
            # for A4Q8 change the scale
            # best = -1
            best = -infinity
            for act in self.game.actions(a_state):
                new_state = self.game.result(a_state, act)
                val = self.min_value(new_state)
                if val > best:
                    best = val
                    best_action = act
        # if it's the min_turn, then using the max_value() to find the smallest one
        # then get the best value and best action
        elif self.game.is_min_turn(a_state):
            # for A4Q8 change the scale
            # best = 1
            best = infinity
            for act in self.game.actions(a_state):
                new_state = self.game.result(a_state,act)
                val = self.max_value(new_state)
                if val < best:
                    best = val
                    best_action = act
        now = time.time()
        # return best_value, best action, and time consummation
        return best, best_action, now-start_time


# A4Q3
# To implement Minimax Search with Alpha-Beta Pruning for Variation 1a
class AlphaBetaPruningV1A(object):
    # initialize the search, which size is the board size
    # initialize the Variation1AGame, and get the initial state
    def __init__(self, size):
        self.game = Variation1AGame(size)
        self.state = self.game.initial

    # Alpha-Beta Pruning Implementation for max value
    # return max value
    def max_value(self, state: GameState, maxs_best, mins_best):
        # if the state in the game is terminal, then return its utility
        if self.game.is_terminal(state):
            best_for_max_here = self.game.utility(state)
        # else, then set best_for_max as -inf, and the the actions from by using game.actions()
        # get the best_for_max_here by using the min_value()
        # when we get the best_for_max_here is larger than mins_best, then return it
        else:
            best_for_max_here = -infinity
            actions = self.game.actions(state)
            for act in actions:
                res = self.game.result(state, act)
                val = self.min_value(res, maxs_best, mins_best)
                if val > best_for_max_here:
                    best_for_max_here = val
                if best_for_max_here >= mins_best:
                    return best_for_max_here
                maxs_best = max(maxs_best, best_for_max_here)

        return best_for_max_here

    # Alpha-Beta Implementation for Min Value
    # return min_value
    def min_value(self, state: GameState, maxs_best, mins_best):
        # if the state in the game is terminal, then return its utility
        if self.game.is_terminal(state):
            best_for_min_here = self.game.utility(state)
        # else, then set best_for_min_here as inf, and the the actions from by using game.actions()
        # get the best_for_min_here by using the max_value()
        # when we get the best_for_min_here is smaller than maxs_best, then return it
        else:
            best_for_min_here = infinity
            actions = self.game.actions(state)
            for act in actions:
                res = self.game.result(state, act)
                val = self.max_value(res, maxs_best, mins_best)
                if val < best_for_min_here:
                    best_for_min_here = val
                if best_for_min_here <= maxs_best:
                    return best_for_min_here
                mins_best = min(mins_best, best_for_min_here)
        return best_for_min_here

    # Alpha-Beta implementation for Minimax-Value
    # return minimax value
    def minimax_value(self, state: GameState):
        if self.game.is_max_turn(state):
            return self.max_value(state, -infinity, infinity)
        else:
            return self.min_value(state, -infinity, infinity)

    # Alpha-Beta for Q3 implementation: Max-Decision
    # return the best_max decisions and actions
    def max_decision(self, state: GameState):
        # setup maxs and min best as -inf and inf
        maxs_best = -infinity
        mins_best = infinity
        # get action
        actions = self.game.actions(state)
        best_for_max_here = -infinity
        best_action = None
        # search actions if the value is max by using min_value
        for act in actions:
            res = self.game.result(state, act)
            val = self.min_value(res, maxs_best, mins_best)

            if val > best_for_max_here:
                best_for_max_here = val
                best_action = act
            maxs_best = max(maxs_best, best_for_max_here)
        return best_for_max_here, best_action

    # Alpha-Beta implementation: Min-Decision
    # return the best_min decisions and actions
    def min_decision(self, state: GameState):
        # setup maxs and min best as -inf and inf
        maxs_best = -infinity
        mins_best = infinity
        # get action
        actions = self.game.actions(state)
        best_for_min_here = infinity
        best_action = None
        # search actions if the value is min by using min_value
        for act in actions:
            res = self.game.result(state, act)
            val = self.min_value(res, maxs_best, mins_best)

            if val < best_for_min_here:
                best_for_min_here = val
                best_action = act
            mins_best = min(mins_best, best_for_min_here)
        return best_for_min_here, best_action

    # Alpha-Beta implementation: Minimax-Decision
    # return the minimax_value, best_action, and time count
    def minimax_decision(self, state: GameState):
        # if it is the max turn, then go to the max_decision
        if self.game.is_max_turn(state):
            start_time = time.time()
            go_max = self.max_decision(state)
            now = time.time()
            return go_max[0], go_max[1], now-start_time
        # if it is the min turn, then go ot the min_decision
        else:
            start_time = time.time()
            go_min = self.min_decision(state)
            now = time.time()
            return go_min[0], go_min[1], now-start_time


# A4Q4
# To implement MiniMax Search with Alpha-Beta Pruning for Variation 1b
class AlphaBetaPruningV1B(object):
    # initialize the search, which size is the board size
    # initialize the Variation1BGame, and get the initial state
    def __init__(self, size):
        self.game = Variation1BGame(size)
        self.state = self.game.initial

    # Alpha-Beta Pruning Implementation for max value v1b
    # return max value
    def max_value(self, state: GameState, maxs_best, mins_best):
        # if the state in the game is terminal, then return its utility
        if self.game.is_terminal(state):
            best_for_max_here = self.game.utility(state)
        # else, then set best_for_max as -inf, and the the actions from by using game.actions()
        # get the best_for_max_here by using the min_value()
        # when we get the best_for_max_here is larger than mins_best, then return it
        else:
            best_for_max_here = -infinity
            actions = self.game.actions(state)
            for act in actions:
                res = self.game.result(state, act)
                val = self.min_value(res, maxs_best, mins_best)
                if val > best_for_max_here:
                    best_for_max_here = val
                if best_for_max_here >= mins_best:
                    return best_for_max_here
                maxs_best = max(maxs_best, best_for_max_here)

        return best_for_max_here

    # Alpha-Beta Implementation for Min Value for v1b
    # return min_value
    def min_value(self, state: GameState, maxs_best, mins_best):
        # if the state in the game is terminal, then return its utility
        if self.game.is_terminal(state):
            best_for_min_here = self.game.utility(state)
        # else, then set best_for_min_here as inf, and the the actions from by using game.actions()
        # get the best_for_min_here by using the max_value()
        # when we get the best_for_min_here is smaller than maxs_best, then return it
        else:
            best_for_min_here = infinity
            actions = self.game.actions(state)
            for act in actions:
                res = self.game.result(state, act)
                val = self.max_value(res, maxs_best, mins_best)
                if val < best_for_min_here:
                    best_for_min_here = val
                if best_for_min_here <= maxs_best:
                    return best_for_min_here
                mins_best = min(mins_best, best_for_min_here)
        return best_for_min_here

    # Alpha-Beta implementation for Minimax-Value for v1b
    # return minimax value
    def minimax_value(self, state: GameState):
        if self.game.is_max_turn(state):
            return self.max_value(state, -infinity, infinity)
        else:
            return self.min_value(state, -infinity, infinity)

    # Alpha-Beta for Q4 implementation: Max-Decision
    # return the best_max decisions and actions
    def max_decision(self, state: GameState):
        # setup maxs and min best as -inf and inf
        maxs_best = -infinity
        mins_best = infinity
        # get action
        actions = self.game.actions(state)
        best_for_max_here = -infinity
        best_action = None
        # search actions if the value is max by using min_value
        for act in actions:
            res = self.game.result(state, act)
            val = self.min_value(res, maxs_best, mins_best)

            if val > best_for_max_here:
                best_for_max_here = val
                best_action = act
            maxs_best = max(maxs_best, best_for_max_here)
        return best_for_max_here, best_action

    # Alpha-Beta for Q4 implementation: Min-Decision
    # return the best_min decisions and actions
    def min_decision(self, state: GameState):
        # setup maxs and min best as -inf and inf
        maxs_best = -infinity
        mins_best = infinity
        # get action
        actions = self.game.actions(state)
        best_for_min_here = infinity
        best_action = None
        # search actions if the value is min by using min_value
        for act in actions:
            res = self.game.result(state, act)
            val = self.min_value(res, maxs_best, mins_best)

            if val < best_for_min_here:
                best_for_min_here = val
                best_action = act
            mins_best = min(mins_best, best_for_min_here)
        return best_for_min_here, best_action

    # Alpha-Beta for Q4 implementation: Minimax-Decision
    # return the minimax_value, best_action, and time count
    def minimax_decision(self, state: GameState):
        # if it is the max turn, then go to the max_decision
        if self.game.is_max_turn(state):
            start_time = time.time()
            go_max = self.max_decision(state)
            now = time.time()
            return go_max[0], go_max[1], now-start_time
        # if it is the min turn, then go ot the min_decision
        else:
            start_time = time.time()
            go_min = self.min_decision(state)
            now = time.time()
            return go_min[0], go_min[1], now-start_time


# A4Q5
# To implement a depth-cutoff and a heuristic evaluation function for Minimax Search
# To allow playing in Variation 1a larger than N = 10
class MiniMaxSearchDepthCutoffV1A(object):
    # to initialize the game, the depth, the size
    # get the initial state from the game
    # invoke the Variation1A Game
    def __init__(self, size, depth):
        self.size = size
        self.game = Variation1AGame(size)
        self.state = self.game.initial
        self.depth = depth

    # max value function for a4q5
    # return the max_value
    def max_value(self, state: GameState, depth):
        # if the state is terminal
        # then best =  utility()
        if self.game.is_terminal(state):
            best = self.game.utility(state)
        # if the cutoff_test is true of the given state
        # best =  eval()
        elif self.game.cutoff_test(state, depth):
            best = self.game.eval(state)[0]
        # else, go search by using min_value() to find the largest one
        else:
            best = -infinity
            for act in self.game.actions(state):
                val = self.min_value(self.game.result(state, act), depth + 1)
                if val > best:
                    best = val

        return best

    # min value function for a4q5
    # returns the min_value
    def min_value(self, state: GameState, depth):
        # if the state is terminal
        # then best =  utility()
        if self.game.is_terminal(state):
            best = self.game.utility(state)
        # if the cutoff_test is true of the given state
        # best =  eval()
        elif self.game.cutoff_test(state, depth):
            best = self.game.eval(state)[0]
        # else, go search by using max_value() to find the smallest one
        else:
            best = infinity
            for act in self.game.actions(state):
                val = self.max_value(self.game.result(state, act), depth + 1)
                if val < best:
                    best = val
        return best

    # min max decision for a4q5
    # returns the minimax_value, best_action, and the time count
    def minimax_decision(self, state: GameState):
        # start to count the time
        start_time = time.time()
        # initial the best_action
        best_action = None

        # if the the current state not the cutoff_test
        # then do the normal search
        if not self.game.cutoff_test(state, self.depth):
            # the max_turn, return the max by using min_value()
            if self.game.is_max_turn(state):
                best = -infinity
                for act in self.game.actions(state):
                    new_state = self.game.result(state, act)
                    val = self.min_value(new_state, self.depth)
                    if val > best:
                        best = val
                        best_action = act
            # the min_turn, return the min by using max_value()
            else:
                best = infinity
                for act in self.game.actions(state):
                    new_state = self.game.result(state, act)
                    val = self.max_value(new_state, self.depth)
                    if val < best:
                        best = val
                        best_action = act
        # else, the best = eval(), and the action is also returned by eval()
        else:
            this_best = self.game.eval(state)
            best = this_best[0]
            best_action = this_best[1]
        now = time.time()
        # return
        return best, best_action, now-start_time


# A4Q6
class MiniMaxSearchDepthCutoffV1B(object):
    # to initialize the game, the depth, the size
    # get the initial state from the game
    # invoke the Variation2B Game
    def __init__(self, size, depth):
        self.size = size
        self.game = Variation1BGame(size)
        self.state = self.game.initial
        self.depth = depth

    # max value function for a4q6
    # return the max_value
    def max_value(self, state: GameState, depth):
        # if the state is terminal
        # then best =  utility()
        if self.game.is_terminal(state):
            best = self.game.utility(state)
        # if the cutoff_test is true of the given state
        # best =  eval()
        elif self.game.cutoff_test(state, depth):
            best = self.game.eval(state)[0]
        # else, go search by using min_value() to find the largest one
        else:
            best = -infinity
            for act in self.game.actions(state):
                val = self.min_value(self.game.result(state, act), depth + 1)
                if val > best:
                    best = val

        return best

    # min value function for a4q6
    # returns the min_value
    def min_value(self, state: GameState, depth):
        # if the state is terminal
        # then best =  utility()
        if self.game.is_terminal(state):
            best = self.game.utility(state)
        # if the cutoff_test is true of the given state
        # best =  eval()
        elif self.game.cutoff_test(state, depth):
            best = self.game.eval(state)[0]
        # else, go search by using max_value() to find the smallest one
        else:
            best = infinity
            for act in self.game.actions(state):
                val = self.max_value(self.game.result(state, act), depth + 1)
                if val < best:
                    best = val
        return best

    # min max decision for a4q6
    # returns the minimax_value, best_action, and the time count
    def minimax_decision(self, state: GameState):
        # start to count the time
        start_time = time.time()
        # initial the best_action
        best_action = None

        # if the the current state not the cutoff_test
        # then do the normal search
        if not self.game.cutoff_test(state, self.depth):
            # the max_turn, return the max by using min_value()
            if self.game.is_max_turn(state):
                best = -infinity
                for act in self.game.actions(state):
                    new_state = self.game.result(state, act)
                    val = self.min_value(new_state, self.depth)
                    if val > best:
                        best = val
                        best_action = act
            # the min_turn, return the min by using max_value()
            else:
                best = infinity
                for act in self.game.actions(state):
                    new_state = self.game.result(state, act)
                    val = self.max_value(new_state, self.depth)
                    if val < best:
                        best = val
                        best_action = act
        # else, the best = eval(), and the action is also returned by eval()
        else:
            this_best = self.game.eval(state)
            best = this_best[0]
            best_action = this_best[1]
        now = time.time()
        # return
        return best, best_action, now-start_time


# A4Q7 To implement a depth-cutoff and a heuristic evaluation function
# for Minimax Search with AlphaBeta pruning, to allow play in games larger than N = 10.
class AlphaBetaPruningCutoff(object):

    # initialize the Variation1A and Variation1B by using the given size
    # initialize the state_v1a from Variation1A and state_v1b Variation1B
    # set up the depth
    def __init__(self, size, depth):
        self.game_v1a = Variation1AGame(size)
        self.game_v1b = Variation1BGame(size)
        self.depth = depth
        self.state_v1a = self.game_v1a.initial
        self.state_v1b = self.game_v1b.initial

    # Alpha-Beta Implementation for max value for v1a
    # return the max_vlaue for v1a
    def max_value_v1a(self, state: GameState, maxs_best, mins_best, depth):
        # if the state is terminal, then best_for_max_here is its utility
        if self.game_v1a.is_terminal(state):
            best_for_max_here = self.game_v1a.utility(state)
        # if the state is through out the cutoff test
        # then the best_for_max is the eval
        elif self.game_v1a.cutoff_test(state, depth):
            best_for_max_here = self.game_v1a.eval(state)[0]
        # else, then set best_for_max as -inf, and the the actions from by using game.actions()
        # get the best_for_max_here by using the min_value_v1a()
        # when we get the best_for_max_here is larger than mins_best, then return it
        else:
            best_for_max_here = -infinity
            actions = self.game_v1a.actions(state)

            for act in actions:
                res = self.game_v1a.result(state, act)
                val = self.min_value_v1a(res, maxs_best, mins_best, depth + 1)
                if val > best_for_max_here:
                    best_for_max_here = val
                if best_for_max_here >= mins_best:
                    return best_for_max_here
                maxs_best = max(maxs_best, best_for_max_here)

        return best_for_max_here

    # Alpha-Beta Implementation for Min Value for v1a
    # return the min_value cut-off for v1a
    def min_value_v1a(self, state: GameState, maxs_best, mins_best, depth):
        # if the state is terminal, then best_for_min_here is its utility
        if self.game_v1a.is_terminal(state):
            best_for_min_here = self.game_v1a.utility(state)
        # if the state is through out the cutoff test
        # then the best_for_min is the eval
        elif self.game_v1a.cutoff_test(state, depth):
            best_for_min_here = self.game_v1a.eval(state)[0]
        # else, then set best_for_min as inf, and the the actions from by using game.actions()
        # get the best_for_min_here by using the max_value_v1a()
        # when we get the best_for_max_here is smaller than max_best, then return it
        else:
            best_for_min_here = infinity
            actions = self.game_v1a.actions(state)
            for act in actions:
                res = self.game_v1a.result(state, act)
                val = self.max_value_v1a(res, maxs_best, mins_best, depth + 1)
                if val < best_for_min_here:
                    best_for_min_here = val
                if best_for_min_here <= maxs_best:
                    return best_for_min_here
                mins_best = min(mins_best, best_for_min_here)
        return best_for_min_here

    # Alpha-Beta implementation for Minimax-Value for v1a
    # return the minimax_vlaue for v1a
    def minimax_value_v1a(self, state: GameState, depth):
        # if it's the max turn, then return the max_value_v1a
        if self.game_v1a.is_max_turn(state):
            return self.max_value_v1a(state, -infinity, infinity, depth)
        # else it's the min turn, then return the min_value_v1a
        else:
            return self.min_value_v1a(state, -infinity, infinity, depth)

    # Alpha-Beta implementation: Max-Decision for v1a
    # return the max_value and its action
    def max_decision_v1a(self, state: GameState, depth):
        # setup max_best and mins_best as -inf and inf
        maxs_best = -infinity
        mins_best = infinity
        # getting the actions from the game
        actions = self.game_v1a.actions(state)
        # setup the best_for max here as -inf
        best_for_max_here = -infinity
        # initialize the actions as None
        best_action = None
        # getting the actions
        for act in actions:
            res = self.game_v1a.result(state, act)
            val = self.min_value_v1a(res, maxs_best, mins_best, depth + 1)
            if val > best_for_max_here:
                best_for_max_here = val
                best_action = act
            maxs_best = max(maxs_best, best_for_max_here)
        return best_for_max_here, best_action

    # Alpha-Beta implementation: Min-Decision for v1a
    # return the min_value and its action
    def min_decision_v1a(self, state: GameState, depth):
        # setup max_best and mins_best as -inf and inf
        maxs_best = -infinity
        mins_best = infinity
        # setup the best_for max here as -inf
        actions = self.game_v1a.actions(state)
        best_for_min_here = infinity
        # initialize the actions as None
        best_action = None
        for act in actions:
            res = self.game_v1a.result(state, act)
            val = self.min_value_v1a(res, maxs_best, mins_best, depth + 1)

            if val < best_for_min_here:
                best_for_min_here = val
                best_action = act
            mins_best = min(mins_best, best_for_min_here)
        return best_for_min_here, best_action

    # Alpha-Beta implementation: Minimax-Decision for v1a
    # return the minimax best decision
    def minimax_decision_v1a(self, state: GameState):
        # if the state is not throughout the cutoff test, then do the normal search
        if not self.game_v1a.cutoff_test(state, self.depth):
            # if its the max turn, then get the max by using max_decision_v1a
            if self.game_v1a.is_max_turn(state):
                start_time = time.time()
                go_max = self.max_decision_v1a(state, self.depth)
                now = time.time()
                return go_max[0], go_max[1], now-start_time
            # if its the min turn, then get the max by using min_decision_v1a
            else:
                start_time = time.time()
                go_min = self.min_decision_v1a(state, self.depth)
                now = time.time()
                return go_min[0], go_min[1], now-start_time
        # else, go to the eval() function, and return it
        else:
            start_time = time.time()
            best = self.game_v1a.eval(state)[0]
            best_action = self.game_v1a.eval(state)[1]
            now = time.time()
            return best, best_action, now-start_time

    # Alpha-Beta Implementation for max value for v1b
    # return the max_vlaue for v1b
    def max_value_v1b(self, state: GameState, maxs_best, mins_best, depth):
        # if the state is terminal, then best_for_max_here is its utility
        if self.game_v1b.is_terminal(state):
            best_for_max_here = self.game_v1b.utility(state)
        # if the state is through out the cutoff test
        # then the best_for_max is the eval
        elif self.game_v1b.cutoff_test(state, depth):
            best_for_max_here = self.game_v1b.eval(state)[0]
        # else, then set best_for_max as -inf, and the the actions from by using game.actions()
        # get the best_for_max_here by using the min_value_v1b()
        # when we get the best_for_max_here is larger than mins_best, then return it
        else:
            best_for_max_here = -infinity
            actions = self.game_v1b.actions(state)

            for act in actions:
                res = self.game_v1b.result(state, act)
                val = self.min_value_v1b(res, maxs_best, mins_best, depth + 1)
                if val > best_for_max_here:
                    best_for_max_here = val
                if best_for_max_here >= mins_best:
                    return best_for_max_here
                maxs_best = max(maxs_best, best_for_max_here)

        return best_for_max_here

    # Alpha-Beta Implementation for Min Value for v1b
    # return the min_value cut-off for v1b
    def min_value_v1b(self, state: GameState, maxs_best, mins_best, depth):
        # if the state is terminal, then best_for_min_here is its utility
        if self.game_v1b.is_terminal(state):
            best_for_min_here = self.game_v1b.utility(state)
        # if the state is through out the cutoff test
        # then the best_for_min is the eval
        elif self.game_v1b.cutoff_test(state, depth):
            best_for_min_here = self.game_v1b.eval(state)[0]
        # else, then set best_for_min as inf, and the the actions from by using game.actions()
        # get the best_for_min_here by using the max_value_v1b()
        # when we get the best_for_max_here is smaller than max_best, then return it
        else:
            best_for_min_here = infinity
            actions = self.game_v1b.actions(state)
            for act in actions:
                res = self.game_v1b.result(state, act)
                val = self.max_value_v1b(res, maxs_best, mins_best, depth + 1)
                if val < best_for_min_here:
                    best_for_min_here = val
                if best_for_min_here <= maxs_best:
                    return best_for_min_here
                mins_best = min(mins_best, best_for_min_here)
        return best_for_min_here

    # Alpha-Beta implementation for Minimax-Value
    def minimax_value_v1b(self, state: GameState, depth):
        # if it's the max turn, then return the max_value_v1b
        if self.game_v1b.is_max_turn(state):
            return self.max_value_v1b(state, -infinity, infinity, depth)
        # else it's the min turn, then return the min_value_v1b
        else:
            return self.min_value_v1b(state, -infinity, infinity, depth)

    # Alpha-Beta implementation: Max-Decision for v1b
    # return the max_value and its action
    def max_decision_v1b(self, state: GameState, depth):
        # setup max_best and mins_best as -inf and inf
        maxs_best = -infinity
        mins_best = infinity
        # getting the actions from the game
        actions = self.game_v1b.actions(state)
        best_for_max_here = -infinity
        # getting the actions
        best_action = None
        # getting the actions
        for act in actions:
            res = self.game_v1b.result(state, act)
            val = self.min_value_v1b(res, maxs_best, mins_best, depth + 1)
            # return best_action and value when val > best_for_best
            if val > best_for_max_here:
                best_for_max_here = val
                best_action = act
            maxs_best = max(maxs_best, best_for_max_here)
        return best_for_max_here, best_action

    # Alpha-Beta implementation: Min-Decision for v1b
    # return the min_value and its action
    def min_decision_v1b(self, state: GameState, depth):
        # setup max_best and mins_best as -inf and inf
        maxs_best = -infinity
        mins_best = infinity
        # getting the actions from the game
        actions = self.game_v1b.actions(state)
        best_for_min_here = infinity
        # initialize the actions as None
        best_action = None
        # getting the actions
        for act in actions:
            res = self.game_v1b.result(state, act)
            val = self.min_value_v1b(res, maxs_best, mins_best, depth + 1)
            # return if the best_for_min_here is smaller than val
            if val < best_for_min_here:
                best_for_min_here = val
                best_action = act
            mins_best = min(mins_best, best_for_min_here)
        return best_for_min_here, best_action

    # Alpha-Beta implementation: Minimax-Decision for v1b
    # return the minimax best decision
    def minimax_decision_v1b(self, state: GameState):
        # if the state is not throughout the cutoff test, then do the normal search
        if not self.game_v1b.cutoff_test(state, self.depth):
            # if its the max turn, then get the max by using max_decision_v1b
            if self.game_v1b.is_max_turn(state):
                start_time = time.time()

                go_max = self.max_decision_v1b(state, self.depth)
                now = time.time()
                return go_max[0], go_max[1], now-start_time
            # if its the min turn, then get the max by using min_decision_v1b
            else:
                start_time = time.time()
                go_min = self.min_decision_v1b(state, self.depth)
                now = time.time()
                return go_min[0], go_min[1], now-start_time
        # else, go to the eval() function, and return it
        else:
            start_time = time.time()
            best = self.game_v1b.eval(state)[0]
            best_action = self.game_v1b.eval(state)[1]
            now = time.time()
            return best, best_action, now-start_time


# A4Q9 To implement an interactive script/application that plays N-Queens
# there are 2 players p1, p2 to play this game
class PlayGame(object):
    # initialize the game by using Variation1AGame
    # Getting the size, and setup cutoff p1 and p2 by invoking the AlphaBetaPruningCutoff
    def __init__(self, size, cutoff_p1, cutoff_p2):
        self.game = Variation1AGame(size)
        self.cutoff_p1 = cutoff_p1
        self.cutoff_p2 = cutoff_p2
        self.state = self.game.initial
        self.alpha_beta_cutoff_p1 = AlphaBetaPruningCutoff(size, cutoff_p1)
        self.alpha_beta_cutoff_p2 = AlphaBetaPruningCutoff(size, cutoff_p2)

    # p1_turn() function for getting the new state after this turn
    # return the new state after p1's turn
    def p1_turn(self, state: GameState):
        # if the state is not terminal, then do the alpha_beta_cutoff search for p1
        # get the new action and state
        if not self.game.is_terminal(state):
            action = self.alpha_beta_cutoff_p1.minimax_decision_v1a(state)[1]
            new_state = self.game.result(state, action)
        # if the state is terminal, then copy the current state
        else:
            new_state = copy.deepcopy(state)
        return new_state

    # p2_turn() function for getting the new state after this turn
    # return the new state after p2's turn
    def p2_turn(self, state: GameState):
        # if the state is not terminal, then do the alpha_beta_cutoff search for p2
        # get the new action and state
        if not self.game.is_terminal(state):
            action = self.alpha_beta_cutoff_p2.minimax_decision_v1a(state)[1]
            new_state = self.game.result(state, action)
        # if the state is terminal, then copy the current state
        else:
            new_state = copy.deepcopy(state)
        return new_state

    # playing the game function
    # returns the 'W' for the player1 Win or Lose
    def playing(self):
        # while game is not terminated, then recursively run p1 and p2
        while not self.game.is_terminal(self.state):
            if self.state.player == 'p1':
                self.state = self.p1_turn(self.state)
            else:
                self.state = self.p2_turn(self.state)
        # getting the win_or_lose number by using utility
        # then return
        win_or_lose = self.game.utility(self.state)
        if win_or_lose == 1:
            return 'W'
        else:
            return 'L'
