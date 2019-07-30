## Name: Yinsheng Dong
## Student Number: 11148648
## NSID: yid164
## A1Q1 Implementation

import re

# problem state class


class ProblemState(object):

    def __init__(self, list_given, target, expr):
        self.t = target
        self.list_given = list_given
        self.expr = expr


    def __str__(self):
        return self.expr

    def __getitem__(self, item):
        print(item)


# problem class
class Problem:

    def __init__(self, state):

        self.state = state

    # is_goal method
    def is_goal(self, a_state):

        return eval(a_state.expr) == self.state.t


    # actions method
    def actions(self, a_state):

        action = []

        el = [int(e) for e in a_state.expr.split() if e.isdigit()]


        plus = str(a_state.t) + ' - ' + a_state.expr
        minus = str(a_state.t) + ' + ' + a_state.expr
        multiply = str(a_state.t) + ' / ' + a_state.expr
        divide = str(a_state.t) + ' * ' + a_state.expr

        if eval(plus) in a_state.list_given:
            action.append("add " + str(eval(plus)))
            return action
        if eval(minus) in a_state.list_given:
            action.append("minus " + str(eval(minus)))
            return action
        if eval(multiply) in a_state.list_given:
            action.append("multiply " + str(eval(multiply)))
            return action
        if eval(divide) in a_state.list_given:
            action.append("divide " + str(eval(divide)))
            return action

        if eval(a_state.expr) < a_state.t:
            if (a_state.t - eval(divide)) > (a_state.t / eval(minus)):
                action.append("add to " + str(a_state.list_given[0]))
            else:
                action.append("multiply to " + str(a_state.list_given[0]))
        elif eval(a_state.expr) < a_state.t:
            if eval(divide) - eval(a_state.expr) >= (eval(minus) / a_state.t):
                action.append("minus to " + str(a_state.list_given[0]))
            else:
                action.append("divide to " + str(a_state.list_given[0]))

        return action

    # the result method
    def result(self, a_state, an_action):
        if an_action in self.actions(a_state):
            if an_action[:11] == "initialize ":
                s = re.search(r'\d+$', an_action)
                a_state.expr = s.group();
            if an_action[:4] == "add ":
                s = re.search(r'\d+$', an_action)
                a_state.expr = '( ' + a_state.expr + ' + ' + s.group() + ' )'
                return ProblemState(a_state.t, a_state.list_given, a_state.expr)
            elif an_action[:6] == "minus ":
                s = re.search(r'\d+$', an_action)
                a_state.expr = '( ' + a_state.expr + ' - ' + s.group() + ' )'
                return ProblemState(a_state.t, a_state.list_given, a_state.expr)
            elif an_action[:9] == "multiply ":
                s = re.search(r'\d+$', an_action)
                a_state.expr = a_state.expr + ' * ' + s.group()
                return ProblemState(a_state.t, a_state.list_given, a_state.expr)
            elif an_action[:7] == "divide ":
                s = re.search(r'\d+$', an_action)
                a_state.expr = a_state.expr + ' / ' + s.group()
                return ProblemState(a_state.t, a_state.list_given, a_state.expr)
            elif an_action[:7] == "add to ":
                s = re.search(r'\d+$', an_action)
                a_state.expr = '( ' + a_state.expr + ' + ' + s.group() + ' )'
                return ProblemState(a_state.t, a_state.list_given, a_state.expr)
            elif an_action[:9] == "minus to ":
                s = re.search(r'\d+$', an_action)
                a_state.expr = '( ' + a_state.expr + ' - ' + s.group() + ' )'
                return ProblemState(a_state.t, a_state.list_given, a_state.expr)
            elif an_action[:12] == "multiply to ":
                s = re.search(r'\d+$', an_action)
                a_state.expr = a_state.expr + ' * ' + s.group()
                return ProblemState(a_state.t, a_state.list_given, a_state.expr)
            elif an_action[:10] == "divide to ":
                s = re.search(r'\d+$', an_action)
                a_state.expr = a_state.expr + ' / ' + s.group()
                return ProblemState(a_state.t, a_state.list_given, a_state.expr)

        else:
            return False

    # the path cost method
    def path_cost(self, c, state_1, state_2, action):
        if self.result(state_1, action) == state_2:
            c += 1


l = [1, 2, 3, 4, 5, 7]
expr = ''
problem_state = ProblemState(l,4,'3')
problem = Problem(problem_state)
actions = problem.actions(problem_state)
print(actions)
problem.result(problem_state, actions[0])
print(problem_state.expr)






