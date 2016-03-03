from team7 import Player7
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
    a = [0, 0, 0, 3, 0, 6, 0, 8, 1, 1, 1, 4, 1, 5, 1, 7, 2, 2, 2, 4, 2, 6 ,3, 0, 3, 1 ,3, 2, 3 ,7, 4 ,2, 4 ,4 ,5, 5, 5, 6, 5, 7, 5, 8, 7, 5, 8, 3]
    b = [0, 2, 0, 4, 0, 5, 0, 6, 1, 3, 1, 8, 2, 3, 2, 5, 3, 3, 3, 8, 4, 1, 4, 3, 5, 0, 5, 3, 6, 0, 6, 3, 6, 4, 6, 5, 6, 8, 7, 8, 8, 0, 8, 5 ,8, 8]
    for i in range(0,len(a),2):
        board[a[i]][a[i+1]] = 'x'
    for i in range(0,len(b),2):
        board[b[i]][b[i+1]] = 'o'
    for i in range(len(board)):
        for j in range(len(board[i])):
                print board[i][j],
        print
    old_move = (6,0)
    block[0] = block[2] = block[3] = block [5] = 'x'
    block[4] = block [7] = block[8] = 'o'
    block[1]='D'
    for i in range(0,len(block),3):
                print block[i],block[i+1],block[i+2] 
    flag = 'x'
    allowed_block_list = p.get_block_list(old_move)
    allowed_cell_list = p.get_cell_list(allowed_block_list,board,block)
    print allowed_cell_list
    
if __name__ == '__main__':
    test_minimax()
'''
0, 0, 0, 3, 0, 6, 0, 8, 1, 1, 1, 4, 1, 5, 1, 7, 2, 2, 2, 4, 2, 6 ,3, 0, 3, 1 ,3, 2, 3 ,7, 4 ,2, 4 ,4 ,5, 5, 5, 6, 5, 7, 5, 8, 7, 5, 7, 3
0, 2, 0, 4, 0, 5, 0, 6, 1, 3, 1, 8, 2, 3, 2, 5, 3, 3, 3, 8, 4, 1, 4, 3, 5, 0, 5, 3, 6, 0, 6, 3, 6, 4, 6, 5, 6, 8, 7, 8, 8, 0, 8, 5, ,8, 8
Our Real Turn 691 (6, 0) 0.00833201408386 82904.661575
Player 2 made the move: (6, 0) with o
=========== Game Board ===========
x - o  x o o  x o x
- x -  o x x  - x o
- - x  o x o  x - -

x x x  o - -  - x o
- o x  o x -  - - -
o - -  o - x  x x x

o - -  o o o  - - o
- - -  - - x  - - o
o - -  x - o  - - o
==================================
=========== Block Status =========
x D x
x o x
- o o
==================================
'''
