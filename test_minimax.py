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
    board[0][1] = board[1][0] = board[1][3] = board[4][3] = 'o'
    board[0][2] = board[6][4] = board[7][0] = board[7][1] = 'x'
    for i in range(len(board)):
        for j in range(len(board[i])):
                print board[i][j],
        print
    time.sleep(2)
    old_move = (4,3)
    flag = 'x'
    move = p.move(board,block,old_move,flag)
    print move
    
if __name__ == '__main__':
    test_minimax()
