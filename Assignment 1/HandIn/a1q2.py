# Student Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT317 Assignment Q2

from a1q1 import Problem
from a1q1 import ProblemState
from collections import deque


class SearchNode:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<SearchNode {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, other):
        return isinstance(other, SearchNode) and self.state == other.state

# Breadth First Search
def bfs(problem):
    # frontier
    frontier = deque([SearchNode(problem.state)]) #queue

    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        for action in problem.actions(node.state):
            new_states = problem.result(node.state, action)
            for new_state in new_states:
                node = SearchNode(new_state)
                frontier.append(node)
    return None

# Depth First Search
def dfs(problem):

    frontier = [SearchNode(problem.state)] #stack
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        for action in problem.actions(node.state):
            new_states = problem.result(node.state, action)
            for new_state in new_states:
                node = SearchNode(new_state)
                frontier.append(node)
    return None

# Depth Limit Search

def dls(problem, limit):
    frontier = [SearchNode(problem.state)] #stack
    cutoff =False
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        else:
            if node.depth < limit:
                for action in problem.actions(node.state):
                    new_states = problem.result(node.state, action)
                    for new_state in new_states:
                        node = SearchNode(new_state)
                        frontier.append(node)
            else:
                cutoff = True
        if not cutoff:
            return None
        else:
            print("No solution")
    return None


# Iterative Deep Search
def ids(problem):

    limit = 0
    while True:
        result = dls(problem, limit)
        if result is not None:
            return "success"
        if result == "No solution":
            return None
        limit = limit + 1


l = [1, 2, 3, 4, 5, 7]
t = 3

problem_state = ProblemState(l, t, '1')
problem = Problem(problem_state)
dfs(problem)
