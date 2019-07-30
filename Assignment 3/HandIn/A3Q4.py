# Student Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT317 A3Q4

import A1Search as go_search


# Pair class, which x is row, and y is column
class Pair(object):

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


# Variable class
# A variable should be an object with a current value, and a list domain
# current value can be None, when the variable is assigned value, the domain should be empty
# A variable does not need to know ots own identifier, but it could, so add the position
# Change the problem class so that each variable's domain is restricted to value that do not appear on the cell
# row and column
class Variable(object):
    def __init__(self, current_value=None, position: Pair=None):
        self.current_value = current_value
        self.position = position
        if current_value is not None:
            self.domain = []

    def __str__(self):
        if self.current_value is not None:
            return 'current value: ' + '< ' + str(self.current_value) + '> domain values ' + '< '+ str(self.domain) +'>'
        else:
            return 'current value is None'


# State class
# include boolean flag for to indicate if the state is known to be inconsistent
# State should consist of a collection of Variable
# collection is a list, to store Variables
# Each variable needs an identifier
# The identifier is used to find the variable by name, without having multiple references
# Variables start at unassigned, and assigned when they are goes on
class State(object):

    def __init__(self, square):
        self.un_assigned_variables = []
        self.square = square
        self.inconsistent = False
        i = 0
        while i < len(square):
            j = 0
            while j < len(square[i]):
                if square[i][j] == 0:
                    variable = Variable(square[i][j], Pair(i, j))
                    x = 1
                    while x <= len(self.square):
                        variable.domain.append(x)
                        x += 1
                    self.un_assigned_variables.append(variable)
                j += 1
            i += 1

    def __str__(self):
        return str(self.un_assigned_variables)


# Problem Class
class Problem(object):
    action_start = "start"
    action_add = "add"

    def __init__(self, square):
        self.square = square

    # initial state to create a State object
    def initial_state(self):
        state = State(self.square)
        i = 0
        while i < len(state.un_assigned_variables):
            position = state.un_assigned_variables[i].position
            col = position.x
            row = position.y
            j = 0
            while j < len(state.square):
                if j != col:
                    remove = state.square[j][row]
                    if remove in state.un_assigned_variables[i].domain:
                        state.un_assigned_variables[i].domain.remove(remove)
                if j != row:
                    remove = state.square[col][j]
                    if remove in state.un_assigned_variables[i].domain:
                        state.un_assigned_variables[i].domain.remove(remove)
                j += 1
            i += 1

        return state

    # is_goal function
    # with forward checking, every consistent partial assignment can be extended by one more variable (at least)
    # That means when the assignment is complete, it must be consistent
    # checks if the State is a solution to the LSCP
    # If there is any unassigned variable, it definitely not a completed Latin Square (Return False)
    # Do not have to keep checking if there are any variables still unassigned
    # Adapt code for A3Q1's function
    # Need to combine the information contained in the given square with the values assigned in the state
    def is_goal(self, a_state: State):

        if a_state.un_assigned_variables:
            return False
        else:
            a_state.inconsistent = True
            choice = []
            j = 1
            while j <= len(a_state.square):
                choice.append(j)
                j += 1
            i = 0
            while i < len(a_state.square):
                new_set = set(a_state.square[i])
                if not new_set.difference(choice):
                    print(a_state.square)
                    return True
                i += 1
            return False

    # actions function, returns a list of actions
    # Choose an unassigned variable and create an action for each allowable domain value
    # Do not actually make the assignment yet
    # Do it in the result
    # Check if the current state is inconsistent. If it is not consistent.
    # Return an empty list of actions
    # This prevents inconsistent state from having child
    def actions(self, a_state: State):
        actions = []
        if a_state.inconsistent:
            return []
        v = a_state.un_assigned_variables[0]
        for c in v.domain:
            actions.append((self.action_add, v.position, c))
        return actions

    # result function, return a state that result from current state
    # Create a new state
    # with the variable assigned the given value
    # As provided by action(),
    # Make sure the copy the variables appropriately, and change the copy
    # The action is a variable X and a domain value v
    # Copy the State as usual, make the assignment, and then remove the value v from the domain of any unassigned
    # variable in X's row and column
    def result(self, a_state:State, action):
        operation = action[0]
        position = action[1]
        num_assign = action[2]

        if operation == self.action_add:
            self.square[position.x][position.y] = num_assign
            state = State(self.square)
            i = 0
            while i < len(state.un_assigned_variables):
                position = state.un_assigned_variables[i].position
                col = position.x
                row = position.y
                j = 0
                while j < len(state.square):
                    if j != col:
                        remove = state.square[j][row]
                        if remove in state.un_assigned_variables[i].domain:
                            state.un_assigned_variables[i].domain.remove(remove)
                    if j != row:
                        remove = state.square[col][j]
                        if remove in state.un_assigned_variables[i].domain:
                            state.un_assigned_variables[i].domain.remove(remove)
                    j += 1
                i += 1
            return state
        else:
            return a_state


