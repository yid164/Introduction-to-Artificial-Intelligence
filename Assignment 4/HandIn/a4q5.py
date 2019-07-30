# Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT317 A4Q5


from a4q10 import MiniMaxSearchDepthCutoffV1A as minimax_depth_cutoff_v1a

# running function for a4q5 when the cutoff = 4 and N <= 20
print("the cutoff is 4: ")
print("Size, Minimax Value,  Best Opening, Move Time in Second")
size = 1
while size <= 20:
    minimaxSearch = minimax_depth_cutoff_v1a(size, 4)
    minimax = minimaxSearch.minimax_decision(minimaxSearch.state)
    print(str(size) + '\t\t' + str(minimax[0]) + '\t\t' + str(minimax[1]) + '\t\t' + str(minimax[2])+'sec')
    size += 1





