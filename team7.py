''' put everything in the class player7
first we find out which cells are valid '''
''' The next step is to make the update function which will update 
    the block state given an old move as we will surely require it 
    while traversing it on the minimax tree'''

import random
class Player7:

	def __init__(self):
		''' Variables Declared Here '''

		pass


	def get_block_list(self,old_move):
	    if old_move[0] == -1 and old_move[1] == -1 :
             # First Move therefore return all blocks
	     return range(9)
	    if old_move[0]%3 == 0 and old_move[1]%3 == 0 :
             # Top Left cell of block
             return [1,3]
            if old_move[0]%3 == 0 and old_move[1]%3 == 1 :
             # Top Middle cell of block
             return [0,2]
            if old_move[0]%3 == 0 and old_move[1]%3 == 2 :
             # Top Right cell of block
             return [1,5]
            if old_move[0]%3 == 1 and old_move[1]%3 == 0 :
             # Center Left cell of block
             return [0,6]
            if old_move[0]%3 == 1 and old_move[1]%3 == 1 :
             # Center Middle cell of block
             return [4]
            if old_move[0]%3 == 1 and old_move[1]%3 == 2 :
             # Center Right cell of block
             return [2,8]
            if old_move[0]%3 == 2 and old_move[1]%3 == 0 :
             # Bottom Left cell of block
             return [3,7]
            if old_move[0]%3 == 2 and old_move[1]%3 == 1 :
             # Bottom Middle cell of any block
             return [6,8]
            if old_move[0]%3 == 2 and old_move[1]%3 == 2 :
             # Bottom Right cell of any block
             return [5,7]
		
	def get_cell_list(self,allowed_block_list, board, block):

	    cell_list = []
            for i in range(len(allowed_block_list)) :
                print block[allowed_block_list[i]]
                if block[allowed_block_list[i]] != '-' : # the block is already won so we cannot move in that block
                    continue

                add_j = allowed_block_list[i]/3  # value to be added to first numbers from pairs  0,0 to 2,2 to get to block list
                add_k = allowed_block_list[i]%3  # value to be added to second numbers from pairs  0,0 to 2,2 to get to block list
                for j in range(3):
                 for k in range(3):
                        j_temp = j+add_j*3
                        k_temp = k+add_k*3    # j and k will give all elements of a given block

                        if(board[j_temp][k_temp]=='-') :  # if the cell is empty
                         cell_list.append( (j_temp,k_temp) )

            if len(cell_list) == 0 : #we have a free move
                 
                 for j in range(9) :
                    for k in range(9) :
                        if board[j][k] == '-' and block[(j/3)*3+k/3] == '-' :  # If the cell is empty
                            cell_list.append((j,k))
            return cell_list

        
        def get_block_number(self,old_move):  # returns the block number of a cell  tested and works fine
            return ((old_move[0]/3)*3+old_move[1]/3) 

        
        def get_cell_list_from_block(self,block_number):  #retruns the 9 cells within a block tested and works fine 
            cell_list = []
            add_j = block_number/3  # value to be added to first numbers from pairs  0,0 to 2,2 to get to block list
            add_k = block_number%3  # value to be added to second numbers from pairs  0,0 to 2,2 to get to block list
            for j in range(3):
                for k in range(3):
                    j_temp = j+add_j*3
                    k_temp = k+add_k*3    # j and k will give all elements of a given block
                    cell_list.append([j_temp,k_temp])
            return cell_list

        def update_block_list(self,old_move,board,block,flag):
            block_number = self.get_block_number(old_move)
            cell_list = self.get_cell_list_from_block(block_number) # Get All cells in the block where last move was played
            if(block[block_number] == '-'):
                    for a in range(0,9,3):
                        if board[cell_list[a][0]][cell_list[a][1]] == board[cell_list[a+1][0]][cell_list[a+1][1]]:
                            if board[cell_list[a+1][0]][cell_list[a+1][1]] == board[cell_list[a+2][0]][cell_list[a+2][1]] == flag:
                                block[block_number] = flag
                    for b in range(3):
                        if board[cell_list[b][0]][cell_list[b][1]] == board[cell_list[b+3][0]][cell_list[b+3][1]]:
                            if board[cell_list[b+3][0]][cell_list[b+3][1]] == board[cell_list[b+6][0]][cell_list[b+6][1]] == flag:
                                block[block_number] = flag
                    if board[cell_list[0][0]][cell_list[0][1]] == board[cell_list[4][0]][cell_list[4][1]] == board[cell_list[8][0]][cell_list[8][1]] == flag :
                        block[block_number] = flag
                    if board[cell_list[2][0]][cell_list[2][1]] == board[cell_list[4][0]][cell_list[4][1]] == board[cell_list[6][0]][cell_list[6][1]] == flag :
                        block[block_number] = flag
            return block


        def utility_func(temp_board) : # temprorary utility function
                return 5


        def tree_func(self,max_or_min , height , temp_alpha , temp_beta , temp_board , temp_block , old_move, flag):
            aplha = temp_alpha # initializing the alpha value as passed by the parent 
            beta = temp_beta # initializing the value of beta as passed by the parent
            board = temp_board # initializing the board
            block = temp_block # initializing the block
            if max_or_min == 0 :  # it is a min node and so our opponent
                value = float("inf") 
                if flag == 'x': # if our flag is x the opponent will move o
                    board[old_move[0]][old_move[1]] = 'o'
                else :
                    board[old_move[0]][old_move[1]] = 'x'
            else : # it is a max node so it is us
                value = -1*float("inf") 
                if flag == 'x': # if our flag is x the opponent will move o
                    board[old_move[0]][old_move[1]] = 'x'
                else :
                    board[old_move[0]][old_move[1]] = 'o'
            
            block = self.update_block_list(old_move,board,block,flag) # here the function added by motwani will be used

            if  height == 4 : # if height is 4 we return the utility 
                return utility_func(board)

            allowed_block_list = self.get_block_list(old_move)

            allowed_cell_list = self.get_cell_list(allowed_block_list,board,block) # getting the cell list for the next move

            best_move = [] # initializing the best move

            for i in range(len(allowed_cell_list)) :


                temp_value = tree_func((max_or_min+1)%2 , height+1,alpha,beta,board ,block,allowed_cell_list[i],flag)

                if max_or_min == 0 :  # minimizer, so updating the best move correspondingly
                    if temp_value < value :
                        value = temp_value 
                        best_move = allowed_cell_list[i]

                else : # maximizer , so updating the best move accordingly
                    if temp_value > value :
                        value = temp_value
            
                        best_move = allowed_cell_list[i]
            
                if max_or_min == 0 : # a minimizer node and value < aplha no need to check children further 
                    if value < alpha :
                        break 
                else :
                    if value > beta :
                        break

                if max_or_min == 0 : # a minimizer node , so updating the value of beta 
                    beta = min(beta,temp_value)
                else : # maximizer so upating the value of aplha
                    aplha = max(alpha ,temp_value) 

            return value

	def move(self,board,block,old_move,flag):

		allowed_block_list = self.get_block_list(old_move)

		allowed_cell_list = self.get_cell_list(allowed_block_list,board,block)

		#return allowed_cell_list[random.randrange(len(allowed_cell_list))]
                #a =  allowed_cell_list[random.randrange(len(allowed_cell_list))]
                #return a
                best_move = []
                value = -1*float("inf")     # initial value for the root node 
                alpha = -1*float("inf")  # initial alpha value for the root node 
                beta = float("inf")      # initial beta value for the root node
                for i in range(len(allowed_cell_list)):

                    temp_value = self.tree_func(0,1,aplha,beta,board,block,allowed_cell_list[i],flag) # first argument shows that the next node is minimizer
                                                                                            # second argument shows the depth of the new node
                    if temp_value > value : # next child having better value , so update the best move
                        value = temp_value
                        best_move = allowed_cell_list[i]

                    alpha = max(alpha,temp_value) # updating value of alpha

                    if value > beta:  # no need to check further children
                        break

                return (best_move[0],best_move[1])


if __name__ == '__main__':  # add test cases here

    '''old_move = [-1 , -1]
    flag = 'x'
    board = []
    block = []
    temp_l = []

    for i in range(9) :
        temp_list = []
        for j in range(9) :
            temp_list.append('-')
        board.append(temp_list)

    board[3][3]='o'
    old_move = [3 , 3]

    for i in range(9) :
        block.append('-')
	p = player7()
	temp_l = p.move(board,block,old_move,flag)

    print temp_l '''
    p = Player7()
    for i in range(9):
        cell_list = p.get_cell_list(i)
        for j in range(len(cell_list)):
            print str(cell_list[j][0])+' '+str(cell_list[j][1])+'    ' ,
