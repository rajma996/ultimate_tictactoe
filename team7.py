''' put everything in the class player7
first we find out which cells are valid '''


class player7:


        def get_block_list(old_move):  ''' Check the below code for blocks again  '''

            if old_move[0]==-1 and old_move[1]==-1: ''' we are getting first move so all blocks are valid '''
                return range(9)
            if old_move[0]%3==0 and old_move[1]%3==0 ''' top left cell of any block '''
                return [1,3]
            if old_move[0]%3==0 and old_move[1]%3==1 ''' top center cell of any block '''
                return [0,2]
            if old_move[0]%3==0 and old_move[1]%3==2 ''' top right cell of any block '''
                return [1,5]
            if old_move[0]%3==1 and old_move[1]%3==0 ''' center left cell of any block '''
                return [0,6]
            if old_move[0]%3==1 and old_move[1]%3==1 ''' center center cell of any block '''
                return [4]
            if old_move[0]%3==1 and old_move[1]%3==2 ''' center right cell of any block '''
                return [2,8]
            if old_move[0]%3==2 and old_move[1]%3==0 ''' bottom left cell of any block '''
                return [3,7]
            if old_move[0]%3==2 and old_move[1]%3==1 ''' bottom center cell of any block '''
                return [6,8]
            if old_move[0]%3==2 and old_move[1]%3==2 ''' bottom right cell of any block '''
                return [5,7]



        def get_cell_list(allowed_block_list,temp_board,temp_block):

            cell_list = []
            for i in range(len(allowed_block_list)):
                if temp_block[allowed_block_list[i]]!='-' : ''' the block is already won so we cannot move in that block'''
                    continue ;

                add_j = allowed_block_list[i]/3; '''  value to be added to first numbers from pairs  0,0 to 2,2 to get to block list'''
                add_k = allowed_block_list[i]%3; '''  value to be added to second numbers from pairs  0,0 to 2,2 to get to block list'''
                for j in range(3):
                    for k in range(3):
                        j_temp = j+add_j*3;
                        k_temp = k+add_k*3;   ''' j and k will give all elements of a given block'''

                        if(temp_board[j][k]=='-') :  ''' if the cell is empty '''
                            cell_list.append( [j_temp,k_temp] );

           if len(cell_list)==0 : ''' we have a free move '''
            for j in len(8):
                for k in len(8):
                    if(temp_board[j][k]=='-') :  ''' if the cell is empty '''
                        cell_list.append([j,k]);

            return cell_list;

    	def move(self, temp_board, temp_block, old_move, flag):

            allowed_block_list = get_block_list(old_move);

            get_cell_list(allowed_block_list,temp_board,temp_block)
