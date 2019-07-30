# Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT317 A4Q7

from a4q10 import AlphaBetaPruningCutoff as alpha_beta_cutoff_v1a

# Testing list get v1a and v1b
v1a_list = []
v1b_list = []
size = 1
# append the v1a and v1b to the list
while size <= 20:
    minimaxSearch = alpha_beta_cutoff_v1a(size, 4)
    minimax_v1 = minimaxSearch.minimax_decision_v1a(minimaxSearch.state_v1a)
    minimax_v2 = minimaxSearch.minimax_decision_v1b(minimaxSearch.state_v1b)
    v1a_list.append((minimax_v1[0], minimax_v1[1], minimax_v1[2]))
    v1b_list.append((minimax_v2[0], minimax_v2[1], minimax_v2[2]))
    size += 1


# print it
size = 0
print("\t\t\t\t\t" + "Variation 1a")
print("Size, Minimax Value,  Best Opening, Move Time in Second")
for a1 in v1a_list:
    print(str(size) + '\t\t' + str(a1[0]) + '\t\t' + str(a1[1]) + '\t\t' + str(a1[2]) + 'sec')
    size +=1

print("\t\t\t\t\t" + "Variation 1b")
print("Size, Minimax Value,  Best Opening, Move Time in Second")
size = 1
for a2 in v1b_list:
    print(str(size) + '\t\t' + str(a2[0]) + '\t\t' + str(a2[1]) + '\t\t' + str(a2[2]) + 'sec')
    size += 1

