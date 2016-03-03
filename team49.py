#!/usr/bin/python
import copy
import random
import math

DEPTH = 4
best_depth = 10
MAX = 100

"""
	related to heuristic
"""
freemove = False
Three_in_a_Row = [
  [ 0, 1, 2 ],
  [ 3, 4, 5 ],
  [ 6, 7, 8 ],
  [ 0, 3, 6 ],
  [ 1, 4, 7 ],
  [ 2, 5, 8 ],
  [ 0, 4, 8 ],
  [ 2, 4, 6 ]
]

Cell_Heuristic = [
	[0, -10, -100, -1000],
	[10, 0, 50, 0],
	[100, -50, 0, 0],
	[1000, 0, 0, 0]
]

Block_Heuristic = [
	[0, -1000, -2000, -100000000],
	[1000, 0, 800, 0],
	[2000, -800, 0, 0],
	[100000000, 0, 0, 0]
]

def getOpponent(player):
	if player=='x':
		return 'o'
	else:
		return 'x'

def forking(line1,line2,block_status,player):
	opp = getOpponent(player)
	pl1 = 0
	ot1 = 0
	for e in Three_in_a_Row[line1]:
		if block_status[e] == player:
			pl1+=1
		elif block_status[e] == opp:
			ot1 += 1
	pl2 = 0
	ot2 = 0
	for e in Three_in_a_Row[line1]:
		if block_status[e] == player:
			pl2 += 1
		elif block_status[e] == opp:
			ot2 += 1

	if pl1 == 2 and ot1 == 0:
		if pl2 == 2 and ot2 == 0:
			return 1800
	if pl1 == 0 and ot1 == 2:
		if pl2 == 0 and ot2 == 2:
			return -1800
	return 0


def for_a_line(line,block_status,player): 
		opp = getOpponent(player)
		pl = 0
		ot = 0
		for j in Three_in_a_Row[line]:
			if block_status[j] == player:
				pl += 1
			elif block_status[j] == opp:
				ot += 1
		if pl == 3 and ot == 0:
			return 100
		elif ot == 3 and pl == 0:
			return -100		
		elif pl == 2 and ot == 0:
			return 30
		elif ot == 2 and pl == 0:
			return -30

		elif pl == 2 and ot == 1:
			return -35
		elif pl == 1 and ot == 2:
			return 35
		else:
			return 0


#explicitly check if the player has won the entire board
def checkWin(block_status, player):
	
	opp = getOpponent(player)
	
	for i in range(8):
		score = 0
		pl = 0
		ot = 0
		for j in range(3):
			if block_status[Three_in_a_Row[i][j]] == player:
				pl += 1
			elif block_status[Three_in_a_Row[i][j]] == opp:
				ot += 1

		score += Block_Heuristic[pl][ot]

		if abs(score) >= 100000000:
			return score

	return score

def blockUtility(game_board,block,player):
	score = 0
#	if player == 'x':
#		opp = 'o'
#	else:
#		opp = 'x'
	opp = getOpponent(player)
	for i in range(8):
		pl = 0
		ot = 0
		for j in range(3):
			if game_board[3*(block/3) + Three_in_a_Row[i][j]/3 ][3*(block)%3 + Three_in_a_Row[i][j]%3] == player:
				pl += 1
			elif game_board[3*(block/3) + Three_in_a_Row[i][j]/3 ][3*(block)%3 + Three_in_a_Row[i][j]%3] == opp:
				ot += 1
		#if ot == 3:
			## print Cell_Heuristic[pl][ot]
		score += Cell_Heuristic[pl][ot]
	return score

def boardUtility(game_board,player,block_status):
	score = 0
	opp = getOpponent(player)
	for block in range(9):
		score += blockUtility(game_board,block,player)

	#for board
	for i in range(8):
		ot = 0
		pl = 0
		for j in range(3):
			if block_status[Three_in_a_Row[i][j]] == player:
				pl+=1
			elif block_status[Three_in_a_Row[i][j]] == opp:
				ot+=1

		score += Block_Heuristic[pl][ot]

	#forking board
	row = [0,1,2]
	col = [3,4,5]
	dia = [6,7]
	for r in row:
		for c in col:
			score += forking(r,c,block_status,player)
		for d in dia:
			score+= forking(r,d,block_status,player)

	for c in col:
		for d in dia:
			score+= forking(c,d,block_status,player)

	#non centre
	for i in range(3):
		for j in range(3):
			if game_board[3+i][3+j] == opp:
				score -= 10
	return score

"""
if ot == 3:
print "u lose idiot"
print Block_Heuristic[pl][ot]
if pl == 3:
print " u win re buffoon"
print Block_Heuristic[pl][ot]
"""

"""
	related to game
"""
def get_valid_moves(prev_move, game_board, block_status,player):

	blocks_allowed = get_blocks_allowed(prev_move, block_status,game_board,player);
	possible_moves = get_emtpy_cells(game_board,blocks_allowed )
	# print "blocks_allowed" , blocks_allowed
	# print "possible_moves" , possible_moves
	free_list=[]
	max_cells_allowed = []
	if len(possible_moves)>13:
	#	print "possible_moves more than 12"
		for i in blocks_allowed:
			if block_status[i]=='-':
				free_list.append((blockUtility(game_board,i,player),i))

		free_list.sort(reverse = True)
		k = 0
		# print "free_list" , free_list
		for i in free_list:
			#if k>2:
			#	break
			#blocks_allowed.append(i[1]);
			#k+=1
			block_list = []
			if len(max_cells_allowed) > 13:
				break
			block_list.append(i[1])
			# print "block_list" , block_list
			temp = get_emtpy_cells(game_board,block_list)
			for li in temp:
				if len(max_cells_allowed) > 13:
					break
				max_cells_allowed.append( li )
	#		print "cells" , max_cells_allowed
		return max_cells_allowed

	return possible_moves


def get_emtpy_cells(game_board, blocks_allowed):
	cells = []  # it will be list of tuples
	#Iterate over possible blocks and get empty cells
	
	for status in blocks_allowed:
		index1 = status/3
		index2 = status%3
		for i in range(index1*3,index1*3+3):
			for j in range(index2*3,index2*3+3):
				## print i,j
				if game_board[i][j] == '-':
					cells.append((i,j))

	# If all the possible blocks are full, you can move anywhere
	if cells == []:
		new_block_status = [0,1,2,3,4,5,6,7,8]
		for status in new_block_status:
			index1 = status/3
			index2 = status%3
			for i in range(index1*3,index1*3+3):
				for j in range(index2*3,index2*3+3):
					if game_board[i][j] == '-':
						cells.append((i,j))
	return cells


def free_move(block_status,game_board,player):
	# print "got a freemove"
	# print "block_status" , block_status
	freemove = True
	blocks_allowed=[]
	free_list = []
	for i in range(9):
		if block_status[i]=='-':
			blocks_allowed.append(i)
	
	return blocks_allowed


def get_blocks_allowed(prev_move, block_status,game_board,player):
	# print "blocks prev_move" , prev_move
	blocks_allowed = []
	if prev_move[0] < 0 or prev_move[1] <0:
		blocks_allowed = [4]
	elif prev_move[0] % 3 == 0 and prev_move[1] % 3 == 0:
		blocks_allowed = [1,3]
	elif prev_move[0] % 3 == 1 and prev_move[1] % 3 == 0:
		blocks_allowed = [0,6]
	elif prev_move[0] % 3 == 0 and prev_move[1] % 3 == 2:
		blocks_allowed = [1,5]
	elif prev_move[0] % 3 == 2 and prev_move[1] % 3 == 0:
		blocks_allowed = [3,7]
	elif prev_move[0] % 3 == 1 and prev_move[1] % 3 == 2:
		blocks_allowed = [2,8]
	elif prev_move[0] % 3 == 1 and prev_move[1] % 3 == 1:
		blocks_allowed = [4]
	elif prev_move[0] % 3 == 2 and prev_move[1] % 3 == 2:
		blocks_allowed = [5,7]
	elif prev_move[0] % 3 == 0 and prev_move[1] % 3 == 1:
		blocks_allowed = [0,2]	
	elif prev_move[0] % 3 == 2 and prev_move[1] % 3 == 1:
		blocks_allowed = [6,8]
	else:
		sys.exit(1)

	# print blocks_allowed
	final_blocks_allowed = []
	for i in blocks_allowed:
		if block_status[i] == '-':
			final_blocks_allowed.append(i)


	if len(final_blocks_allowed)==0:
		return free_move(block_status,game_board,player)
	else:
		return final_blocks_allowed


def update_lists(game_board, block_stat, move_ret, fl):


	game_board[move_ret[0]][move_ret[1]] = fl

	block_no = (move_ret[0]/3)*3 + move_ret[1]/3	
	id1 = block_no/3
	id2 = block_no%3
	mflg = 0

	flag = 0
	for i in range(id1*3,id1*3+3):
		for j in range(id2*3,id2*3+3):
			if game_board[i][j] == '-':
				flag = 1


	if block_stat[block_no] == '-':
		if game_board[id1*3][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3+2][id2*3+2] and game_board[id1*3+1][id2*3+1] != '-' and game_board[id1*3+1][id2*3+1] != 'D':
			mflg=1
		if game_board[id1*3+2][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3][id2*3 + 2] and game_board[id1*3+1][id2*3+1] != '-' and game_board[id1*3+1][id2*3+1] != 'D':
			mflg=1
		if mflg != 1:
                    for i in range(id2*3,id2*3+3):
                        if game_board[id1*3][i]==game_board[id1*3+1][i] and game_board[id1*3+1][i] == game_board[id1*3+2][i] and game_board[id1*3][i] != '-' and game_board[id1*3][i] != 'D':
                                mflg = 1
                                break
		if mflg != 1:
                    for i in range(id1*3,id1*3+3):
                        if game_board[i][id2*3]==game_board[i][id2*3+1] and game_board[i][id2*3+1] == game_board[i][id2*3+2] and game_board[i][id2*3] != '-' and game_board[i][id2*3] != 'D':
                                mflg = 1
                                break
	if flag == 0:
		block_stat[block_no] = 'D'
	if mflg == 1:
		block_stat[block_no] = fl
	

	return block_stat


def max_play(prev_move, game_board, depth, block_status, playerFlag,alpha,beta):
	bs = copy.deepcopy(block_status)
	opp = getOpponent(playerFlag)
	bs = update_lists(game_board, bs, prev_move, opp)

	

#check for board win
	win_score = checkWin(bs, playerFlag)
	if abs(win_score) >= 100000000:
		return win_score
#


	if depth == DEPTH:
		uti = boardUtility(game_board,playerFlag,bs)
		# print "max ", uti
		return uti 
	moves = get_valid_moves(prev_move, game_board, bs,playerFlag)
	# print "max pr" , prev_move
	#print "max has moves" , moves
	#best_score = float('-inf')
	for move in moves:
		game = copy.deepcopy(game_board)
		game[move[0]][move[1]]=playerFlag
		#print_board(game)
		#print "max gave move", move
		score = min_play(move, game[:], depth+1, bs, playerFlag,alpha,beta)
		#print "max score" , score
		if alpha > beta:
			game_board[move[0]][move[1]]="-"
			return alpha
		if score > alpha:
			best_move = move
			alpha = score
			#print "alpha changed", alpha


		game_board[move[0]][move[1]]="-"
	block_status = copy.deepcopy(bs)
	#print "alpha return" , alpha
	return alpha



def min_play(prev_move, game_board, depth, block_status, playerFlag,alpha,beta):
	bs = copy.deepcopy(block_status)
	opp = getOpponent(playerFlag)
	bs = update_lists(game_board, bs, prev_move, playerFlag)


	#check for board win
	win_score = checkWin(bs, playerFlag)
	if abs(win_score) >= 100000000:
		return win_score
	#	

	if depth == DEPTH:
		uti = boardUtility(game_board,playerFlag,bs)
		#print "min uti" , uti
		return uti

	moves = get_valid_moves(prev_move, game_board, bs,opp)
	#best_score = float('inf')
	#print "min has moves" ,  moves
	for move in moves:
		game = copy.deepcopy(game_board)
		game[move[0]][move[1]]=opp
		#print_board(game)
		#print "min gave move" , move
		score = max_play(move, game[:], depth+1, bs, playerFlag,alpha,beta)
		#print "min score" , score
		game_board[move[0]][move[1]]="-"
		if alpha > beta:
			game_board[move[0]][move[1]]="-"
			#print "min prune" , alpha
			return beta
		if score < beta:
			best_move = move
			beta = score
			#print "beta changed", beta


	block_status = copy.deepcopy(bs)
	#print "min return" , beta
	return beta

def minimax(prev_move, game_board, depth, block_status, playerFlag):
	moves = get_valid_moves( prev_move, game_board, block_status,playerFlag)
	best_move = moves[0]
	best_score = float('-inf')
	#print "minimax has moves" , moves
	for move in moves:

		game = copy.deepcopy(game_board)
		game[move[0]][move[1]]=playerFlag
		#print_board(game_board)
		#print "try minimax move", move
		score = min_play(move, game[:], depth+1, block_status, playerFlag,float('-inf'),float('inf'))
		#print "minimax move" , move , best_move
		#print "minimax score" ,score , best_score
		if score > best_score:
			best_move = move
			best_score = score

		game_board[move[0]][move[1]]="-"
	return best_move

def print_board(game_board):
	for i in range(9):
		 print game_board[i]

def update_block_status(game_board):
		block_status = ['-','-','-','-','-','-','-','-','-']
		for i in range(9):
			for j in range(9):
				if game_board[i][j]!='-':
					block_status = update_lists(game_board, block_status, (i,j), game_board[i][j])
		return block_status

class Player49:

	def __init__(self):
		pass

	def getInput(self):
		b = []
		for i in range(0,9):
			l = []
			a = raw_input()
			for j in a:
				if j == '-' or j == 'x' or j == 'o':
					l.append(j)
			
			b.append(l)

		return b;

	def move(self, game_board, block_status, prev_move, playerFlag):
		#print block_status
		if prev_move[0] < 0 or prev_move[1] < 0:
			return (3,3)
		mov = minimax(prev_move, game_board[:], 0, block_status, playerFlag)
		# print mov
		return mov

"""
player = Player49()

game_board = player.getInput()
a = raw_input()
#print a
b = int(a.split()[0])
c = int(a.split()[1])
tup = (b, c) 
block_status = update_block_status(game_board);

print player.move(game_board, block_status, tup, "x")
"""
"""
for block in range(0,8):
	start_row = 3*(block/3);
	start_column = 3*(block%3);
	small_board = []
	for row in range( start_row, start_row + 3 ):
		for col in range(start_column, start_column + 3):
			small_board.append(game_board[row][col])
	#print small_board
	evaluatePosition(small_board,'x')



binaryPermutations("",3,9)
print len(game_dict)

"""
"""
	# block win
	for i in range(9):
		if block_status[i] == player:
			score += 15
		elif block_status[i] == opp:
			score += -15
"""

"""	
	#corner cell
	row = [0,2,3,5,6,8]
	
	for i in row:
		for j in row:
			if game_board[i][j] == player:
				score += 1
			elif game_board[i][j] == opp:
				score += -1
"""
"""
elif utility == alpha:
			if depth < best_depth:
				best_move = move
				alpha = utility
				best_depth = depth
"""

""" 
def boardUtility(game_board, player, block_status):
	score = 0
	if player == 'x':
		opp = 'o'
	else:
		opp = 'x'

	#win state

	for block in range(9):
		for i in range(8):
			pl = 0
			ot = 0
			for j in range(3):
				if game_board[3*(block/3) + Three_in_a_Row[i][j]/3 ][3*(block)%3 + Three_in_a_Row[i][j]%3] == player:
					pl += 1
				elif game_board[3*(block/3) + Three_in_a_Row[i][j]/3 ][3*(block)%3 + Three_in_a_Row[i][j]%3] == opp:
					ot += 1
			if pl == 3 and ot == 0:
				score += 20
			elif ot == 3 and pl == 0:
				score -= 40
			elif pl == 2 and ot == 0:
				score += 10
			elif ot == 2 and pl == 0:
				score -= 10

	#center block
	if block_status[4] == player:
		score += 10
	elif block_status[4] == opp:
		score += -10

	corner_block = [0, 2, 6, 8]
	for i in corner_block:
		if block_status[i] == player:
			score += 5
		elif block_status[i] == opp:
			score += -5

	#center cell
	row = [1,3,7]
	col = [1,3,7]
	for i in row:
		for j in col:
			if game_board[i][j] == player:
				score += -3
			elif game_board[i][j] == opp:
				score += +3

	#game board
	for i in range(8):
		score+= for_a_line(i,block_status,player)

	#forking board
	row = [0,1,2]
	col = [3,4,5]
	dia = [6,7]
	for r in row:
		for c in col:
			score += forking(r,c,block_status,player)
		for d in dia:
			score+= forking(r,d,block_status,player)

	for c in col:
		for d in dia:
			score+= forking(c,d,block_status,player)




	

	#print score
	return score
"""

"""
	center = [1,3,7]
	for i in center:
		for j in center:
			if game_board[i][j] == player:
				score -= 20
			elif game_board[i][j] == opp:
				score += 15
"""
