''' put everything in the class player7
first we find out which cells are valid '''


class player7:

	def __init__(self):
		''' Variables Declared Here '''

		pass


	def get_block_list(old_move):

		''' Check the below code for blocks again  '''

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
		
	def get_cell_list(allowed_block_list, board, block):

		cell_list = []
        for i in range(len(allowed_block_list)) :
            if temp_block[allowed_block_list[i]] != '-' : # the block is already won so we cannot move in that block
                continue

            add_j = allowed_block_list[i]/3  # value to be added to first numbers from pairs  0,0 to 2,2 to get to block list
            add_k = allowed_block_list[i]%3  # value to be added to second numbers from pairs  0,0 to 2,2 to get to block list
            for j in range(3):
                for k in range(3):
                    j_temp = j+add_j*3
                    k_temp = k+add_k*3    # j and k will give all elements of a given block

                    if(temp_board[j][k]=='-') :  # if the cell is empty
                        cell_list.append( [j_temp,k_temp] )

        if len(cell_list) == 0 : #we have a free move
             for j in len(8) :
                for k in len(8) :
                    if(board[j][k] == '-') :  # If the cell is empty
                        cell_list.append([j,k])
        return cell_list


	def move(self,board,block,old_move,flag):

		allowed_block_list = get_block_list(old_move)

		allowed_cell_list = get_cell_list(allowed_block_list,board,block)

		#return allowed_cell_list[random.randrange(len(allowed_cell_list))]

		return allowed_cell_list  # Return the complete list temprorarily for testing



if __name__ == '__main__':  # add test cases here

    old_move = [-1 , -1]
    flag = 'x'
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
	p = player7()
	temp_l = p.move(board,block,old_move,flag)

    print p,temp_l
