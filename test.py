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

        board[3][5]='o'
        board[4][4]='o'
        board[5][3]='o'
        old_move = [3 , 3]

        for i in range(9) :
                block.append('-')

        print block
        p = Player7()
        #temp_l = p.move(board,block,old_move,flag)
        
        #for i in range(9):
        p.update_block_list((5,5),board,block,flag)
        print block
        #for j in range(len(cell_list)):
        #    print str(cell_list[j][0])+' '+str(cell_list[j][1])+'    ' ,
        for i in range(9):
                print
                for j in range(9):
                        print board[i][j],

if __name__ == '__main__':  # add test cases here
    test_update_block_list_function()
