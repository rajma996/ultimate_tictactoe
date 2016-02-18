''' put everything in the class player7
first we find out which cells are valid '''


class player7:


        def get_block_list(old_move):

            if old_move[0]==-1 and old_move[1]==-1: ''' we are getting first move so all blocks are valid '''
                return range(9)

            

    	def move(self, temp_board, temp_block, old_move, flag):

            allowed_block_list = get_block_list(old_move);
