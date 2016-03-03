from team7 import Player7
from team49 import Player49
import time

def test_minimax():
    p = Player7()
    board = []
    block = []
    temp_l = []
    for i in range(9) :
        block.append('-')

    for i in range(9) :
        temp_list = []
        for j in range(9) :
            temp_list.append('-')
        board.append(temp_list)
    a= [0, 0 ,0, 3, 0, 8, 2, 8, 3, 0, 3, 7, 3, 8, 4, 1, 4, 4, 4, 7, 5, 2, 5, 4, 5, 7, 6, 6 ,7 ,4]
    b = [0, 4 ,1, 4, 2, 4, 1, 7, 1, 8, 3, 2, 3, 3, 3, 4, 3, 5, 3, 6, 5, 6, 5 ,8 ,6 ,0, 6, 1, 6, 2 ]
    for i in range(0,len(a),2):
        board[a[i]][a[i+1]] = 'x'
    for i in range(0,len(b),2):
        board[b[i]][b[i+1]] = 'o'
    for i in range(len(board)):
        for j in range(len(board[i])):
                print board[i][j],
        print
    old_move = (1,8)
    flag = 'x'
    move = p.move(board,block,old_move,flag)
    print move
    
if __name__ == '__main__':
    test_minimax()


'''0 0 0 3 0 8 2 8 3 0 3 7 3 8 4 1 4 4 4 7 5 2 5 4 5 7 6 6 7 4 
0 4 1 4 2 4 1 7 1 8 3 2 3 3 3 4 3 5 3 6 5 6 5 8 6 0 6 1 6 2
Player 2 made the move: (1, 8) with o
=========== Game Board ===========
x - -  x o -  - - x
- - -  - o -  - o o
- - -  - o -  - - x

x - o  o o o  o x x
- x -  - x -  - x -
- - x  - x -  o x o

o o o  - - -  x - -
- - -  - x -  - - -
- - -  - - -  - - -
==================================
=========== Block Status =========
- o -
x o x
o - -
==================================
'''
