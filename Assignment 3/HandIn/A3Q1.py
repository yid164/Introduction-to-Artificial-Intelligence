# Student Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT 317 A3Q1


# The Pair class for column and row
class Pairs(object):

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return ' (' + str(self.x) + ',' + str(self.y) + ')'


# The State Class
# Represent the problem
# include a list of blank location
class State(object):

    # need the square and create a list which contains all the blank variable in the table
    def __init__(self, square):
        self.square = square
        self.blank_list = []
        i = 0
        while i < len(self.square):
            j = 0
            while j < len(self.square):
                if 0 == square[i][j]:
                    pair = Pairs(i, j)
                    self.blank_list.append(pair)
                j = j + 1
            i = i + 1

    # to string
    def __str__(self):
        if self.blank_list is None:
            return ' < Initial state, ' + str(self.square) + ' > '
        else:
            return ' < ' + str(self.blank_list) + ' > '


# the problem class
class Problem(object):

    # actions
    action_add = 'Add a number on the position'
    action_done = 'Well Done'

    def __init__(self):
        self.choice = []

    # is_goal function, checks if state array is true Latin Square
    # If there is a black, it's definitely not a CLS
    # keep check if there are any blacks in the list
    def is_goal(self, a_state:State):

        j = 1
        while j <= len(a_state.square):
            self.choice.append(j)
            j += 1
        i = 0
        while i < len(a_state.square):
            new_set = set(a_state.square[i])
            if not new_set.difference(self.choice):
                return True
            i += 1
        return False

    # A black can be filled in with any 1..N
    # indicate which blank to fill in
    # Not need fill the blank yet
    def actions(self, a_state:State):
        actions = []

        if not a_state.blank_list:
            actions.append((self.action_done, Pairs(), 0))

        else:
            for p in a_state.blank_list:
                for c in self.choice:
                    actions.append((self.action_add, p, c))

        return actions

    # Create a new state object with the black filled in
    # Described in action
    # Copy the list and array
    def result(self, a_state:State, an_action):
        op = an_action[0]
        position = an_action[1]
        choice = an_action[2]
        x = position.x
        y = position.y

        if op is self.action_add:
            square = a_state.square
            square[x][y] = choice
            state = State(square)
            return state

        else:
            return a_state





