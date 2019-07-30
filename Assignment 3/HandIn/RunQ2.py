# Student Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT 317 A3Q2 Run File

import A3Q2 as q2_state
import A1Search as searching

# Run Q1
file = open('LatinSquares.txt', 'r')
i = file.readline().rsplit()
print('There are ' + i[0] + ' Latin Squares')
z = file.readlines()

square_list = []
square = []
squares = []

for line in z:
    words = line.split()
    size = 0
    if len(words) == 1 and words is not None:
        size = int(words[0])
        square = []
    elif len(words) > 1:
        square_list = []
        for w in words:
            if w == '_':
                w = '0'
            square_list.append(int(w))
        square.append(square_list)
    if len(square) <= size:
        squares.append(square)
    else:
        size = 0
i = 0
while i < len(squares):
    problem = q2_state.Problem(squares[i])
    state = problem.initial_state()
    go_search = searching.Search(problem, 10)
    print(go_search.DepthFirstSearch(state))
    i += 1















