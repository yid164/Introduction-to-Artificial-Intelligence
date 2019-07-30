# Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT317 A4Q4

# Alpha-Beta Pruning for Variation 1b Running file
# print the table

from a4q10 import AlphaBetaPruningV1B as alpha_beta_v1b

# running function for a4q4
print("Size, Minimax Value,  Best Opening, Move Time in Second")
size = 1
while size <= 10:
    minimaxSearch = alpha_beta_v1b(size)
    minimax = minimaxSearch.minimax_decision(minimaxSearch.state)
    print(str(size) + '\t\t' + str(minimax[0]) + '\t\t' + str(minimax[1]) + '\t\t' + str(minimax[2])+'sec')
    size += 1

print('')
print('')
print('')

# testing larger size
print('larger size testing:  ')
print("Size, Minimax Value,  Best Opening, Move Time in Second")
larger_size = 11
while larger_size <= 12:
    minimaxSearch = alpha_beta_v1b(size)
    minimax = minimaxSearch.minimax_decision(minimaxSearch.state)
    print(str(larger_size) + '\t\t' + str(minimax[0]) + '\t\t' + str(minimax[1]) + '\t\t' + str(minimax[2]) + 'sec')
    larger_size += 1


