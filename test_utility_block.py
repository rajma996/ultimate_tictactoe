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
        board[0+6][0+6] = 'x';board[0+6][1+6] = 'o';board[0+6][2+6] = 'x';
        board[1+6][0+6] = 'o';board[1+6][1+6] = 'x';board[1+6][2+6] = 'o';        
        board[2+6][0+6] = 'o';board[2+6][1+6] = 'o';board[2+6][2+6] = 'x';

        ans = p.get_utility_block(board,8,flag)
        print ans



if __name__ == '__main__':  # add test cases here
    test_update_block_list_function()
