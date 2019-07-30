# Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT317 A4Q2

# import MiniMaxSearchV1B from a4q10
from a4q10 import MiniMaxSearchV1B as minimax_search_v1b


# running function for a1q2
print("Size, Minimax Value,  Best Opening, Move Time in Second")
size = 1
# set up the size is <= 10
while size <= 10:
    minimaxSearch = minimax_search_v1b(size)
    minimax = minimaxSearch.minimax_decision(minimaxSearch.state)
    print(str(size) + '\t\t' + str(minimax[0]) + '\t\t' + str(minimax[1]) + '\t\t' + str(minimax[2])+'sec')
    size += 1

print('')
print('')
print('')

# testing larger size 11, 12
print('larger size testing:  ')
print("Size, Minimax Value,  Best Opening, Move Time in Second")
larger_size = 11
while larger_size <= 12:
    minimaxSearch = minimax_search_v1b(size)
    minimax = minimaxSearch.minimax_decision(minimaxSearch.state)
    print(str(larger_size) + '\t\t' + str(minimax[0]) + '\t\t' + str(minimax[1]) + '\t\t' + str(minimax[2]) + 'sec')
    larger_size += 1
