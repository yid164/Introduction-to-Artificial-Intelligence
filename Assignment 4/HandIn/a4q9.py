# Name: Yinsheng Dong
# Student Number: 11148648
# NSID: yid164
# CMPT317 A4Q9

# import the PlayGame class from a4q10
from a4q10 import PlayGame as go_play_game

# running function for printing
print("Now testing when N = 10")
n = 10
# Test the 1st scenario N = 10
i = 0
win_1 = 0
lose_1 = 0
play_game = None
print("N"+"\t\t"+"Cut-off P1" + '\t\t' + "Cut-off P2" + '\t\t' + 'Win/Lose P1')
while i < n:
    play_game = go_play_game(n, 4, 4)
    if play_game.playing() == 'W':
        win_1 += 1
    else:
        lose_1 += 1
    i += 1
print(str(n) + '\t\t' + str(play_game.cutoff_p1) + '\t\t\t\t' + str(play_game.cutoff_p2) + '\t\t' + str(win_1)+'W' + ',' + str(lose_1)+'L')

# Test the 2nd scenario N = 10
j = 0
win_2 = 0
lose_2 = 0
while j < n:
    play_game = go_play_game(n, 5, 5)
    if play_game.playing() == 'W':
        win_2 += 1
    else:
        lose_2 += 1
    j += 1
print(str(n) + '\t\t' + str(play_game.cutoff_p1) + '\t\t\t\t' + str(play_game.cutoff_p2) + '\t\t' + str(win_2) + 'W' + ',' + str(lose_2) + 'L')

# Test the 3rd scenario N = 10
k = 0
win_3 = 0
lose_3 = 0
while k < n:
    play_game = go_play_game(n, 5, 3)
    if play_game.playing() == 'W':
        win_3 += 1
    else:
        lose_3 += 1
    k += 1
print(str(n) + '\t\t' + str(play_game.cutoff_p1) + '\t\t\t\t' + str(play_game.cutoff_p1) + '\t\t' + str(win_3) + 'W' + ',' + str(lose_3) + 'L')

# Test the 4th scenario N = 10
h = 0
win_4 = 0
lose_4 = 0
while h < n:
    play_game = go_play_game(n, 3, 5)
    if play_game.playing() == 'W':
        win_4 += 1
    else:
        lose_4 += 1
    h += 1
print(str(n) + '\t\t' + str(play_game.cutoff_p1) + '\t\t\t\t' + str(play_game.cutoff_p2) + '\t\t' + str(win_4) + 'W' + ',' + str(lose_4) + 'L')

print("")
print("")
print("")

n = 20

# Test the 1st scenario when N = 20
print("Now testing when N = 20")
i = 0
win_1 = 0
lose_1 = 0
print("N"+"\t\t"+"Cut-off P1" + '\t\t' + "Cut-off P2" + '\t\t' + 'Win/Lose P1')
while i < n:
    play_game = go_play_game(n, 4, 4)
    if play_game.playing() == 'W':
        win_1 += 1
    else:
        lose_1 += 1
    i += 1
print(str(n) +'\t\t' + str(play_game.cutoff_p1) + '\t\t\t\t' + str(play_game.cutoff_p2) + '\t\t' + str(win_1)+'W' + ',' + str(lose_1)+'L')

# Test the 2nd scenario N = 20
j = 0
win_2 = 0
lose_2 = 0
while j < n:
    play_game = go_play_game(n, 5, 5)
    if play_game.playing() == 'W':
        win_2 += 1
    else:
        lose_2 += 1
    j += 1
print(str(n) + '\t\t' + str(play_game.cutoff_p1) + '\t\t\t\t' + str(play_game.cutoff_p1) + '\t\t' + str(win_2) + 'W' + ',' + str(lose_2) + 'L')

# Test the 3rd scenario N = 20
k = 0
win_3 = 0
lose_3 = 0
while k < n:
    play_game = go_play_game(n, 5, 3)
    if play_game.playing() == 'W':
        win_3 += 1
    else:
        lose_3 += 1
    k += 1
print(str(n) + '\t\t' + str(play_game.cutoff_p1) + '\t\t\t\t' + str(play_game.cutoff_p2) + '\t\t' + str(win_3) + 'W' + ',' + str(lose_3) + 'L')

# Test the 4th scenario N = 20
h = 0
win_4 = 0
lose_4 = 0
while h < n:
    play_game = go_play_game(n, 3, 5)
    if play_game.playing() == 'W':
        win_4 += 1
    else:
        lose_4 += 1
    h += 1
print(str(n) + '\t\t' + str(play_game.cutoff_p1) + '\t\t\t\t' + str(play_game.cutoff_p2) + '\t\t' + str(win_4) + 'W' + ',' + str(lose_4) + 'L')
