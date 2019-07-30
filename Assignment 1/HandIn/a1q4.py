import heapq

from a1q1 import *
from a1q2 import *

# priority queue
class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, priority, x):
        heapq.heappush(self.items, (-priority, x))

    def pop(self):
        _, x = heapq.heappop(self.items)
        return x

    def empty(self):
        return not self.items

# explored set
class Explored:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def delete(self):
        self.items.pop()

# Uniform-cost search
class UCS:
    def __init__(self, problem):
        self.queue = PriorityQueue()
        self.queue.push(problem.state)
        self.set = {}

    def ucs(self, problem):
        while not self.queue.empty():
            node = self.queue.pop()
            if problem.is_goal(node.state):
                self.set(node.state)
                for action in problem.actions(node.state, action):
                    child = child.node
                    if child.state not in explored:
                        self.queue.push(child)
                    elif child.state in explored:
                        self.queue.push(child.node, child)
        return None

#Greedy Best-first Search GBFS
class GBFS(problem):

    def __init__(self, problem):
        self.queue = PriorityQueue()
        self.queue.push(problem.state)

    def gbfs(self, problem):
        while not self.queue.empty():
            node = self.queue.pop()
            if problem.is_goal(node.state):
                for action in problem.actions(node.state, action):
                    child = child.node
                    if child.path_cost + node.path_cost == problem.state.t:
                        self.queue.push(child)
                    else:
                        return
        return None


#A*
def a_star_search(problem, h=None):
    h = 1
    while h < problem.state.path_cost:
        GBFS(problem)
        h += 1







