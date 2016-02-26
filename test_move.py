from team7 import Player7


def test_update_block_list_function():
        old_move = [-1 , -1] 
        flag = 'o' 
        board = []
        block = []
        temp_l = []

        for i in range(9) :
                temp_list = []
                for j in range(9) :
                    temp_list.append('-')
                board.append(temp_list)


        for i in range(9) :
                block.append('-')

        p = Player7()
        raj = p.move(board,block,[-1,-1],flag)
        board[raj[0]][raj[1]] = flag 
        for i in range(9):
                print
                for j in range(9):
                        print board[i][j],

if __name__ == '__main__':  # add test cases here
    test_update_block_list_function()
