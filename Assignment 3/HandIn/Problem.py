import A3Q1 as State

class Problem(object):
    action_start = "load "
    action_add = "add "
    action_mult = "mult "
    action_subtr = "sub "
    action_div = "div "

    def __init__(self, target=None, choices = None):
        self.target = target
        self.choice = choices

    def is_goal(self, a_state:State):
        return a_state.value == self.target

    def actions(self, a_state:State):
        actions = []
        if a_state.expr is "":
            for c in self.choice:
                actions.append((self.action_start, c))
        else:
            for c in self.choice:
                actions.append(self.action_add, c)
                actions.append(self.action_mult, c)
                actions.append(self.action_subtr, c)
                actions.append(self.action_div, c)
        return actions

    def result(self, a_state:State, an_action):
        the_op = an_action[0]
        operand = an_action[1]

        if the_op is self.action_start:
            new_expr = str(operand)
            new_value = operand
        elif the_op is self.action_add:
            new_expr = '(' + a_state.expr + ' + ' + str ( operand) + ')'
            new_value = a_state.value + operand
        elif the_op is self.action_subtr:
            new_expr = '(' + a_state.expr + ' - ' + str(operand) + ')'
            new_value = a_state.value - operand
        elif the_op is self.action_mult:
            new_expr = '(' + a_state.expr + ' * ' + str(operand) + ')'
            new_value = a_state.value * operand
        elif the_op is self.action_div:
            new_expr = '(' + a_state.expr + ' // ' + str(operand) + ')'
            new_value = a_state.value // operand
        else:
            # it ’s not one of the known strings . Uh oh.
            new_expr = None
            new_value = None
            new_choices = a_state.choices.copy()
            new_choices.remove(operand)
        return State(new_value, new_expr, new_choices)
