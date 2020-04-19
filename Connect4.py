import numpy as np 

row_count=6 
column_count=7

def creating_board():
	board=np.zeros((row_count,column_count))
	return board

def drop_piece(board,row,selectColumn,piece):
	board[row][selectColumn]=piece

def is_valid_location(board,selectColumn):
	return board[row_count-1][selectColumn]==0

def get_next_open_row(board,selectColumn):
	for i in range(row_count):
		if board[i][selectColumn]==0:
			return i

def print_board(board):
	print(np.flip(board,0))   # 0 is X-axis

def winning_move(board,piece):
	# Check horizontal locations for win
	for i in range(column_count-3):
		for j in range(row_count):
			if board[j][i]==piece and board[j][i+1]==piece and board[j][i+2]==piece and board[j][i+3]==piece:
				return True

	# Check Vertical locations for win
	for i in range(column_count):
		for j in range(row_count-3):
			if board[j][i]==piece and board[j+1][i]==piece and board[j+2][i]==piece and board[j+3][i]==piece:
				return True

	# Check positively sloped diagonals
	for i in range(column_count-3):
		for j in range(row_count-3):
			if board[j][i]==piece and board[j+1][i+1]==piece and board[j+2][i+2]==piece and board[j+3][i+3]==piece:
				return True

	# Check negatively sloped diagonals	
	for i in range(column_count-3):
		for j in range(3,row_count):
			if board[j][i]==piece and board[j-1][i+1]==piece and board[j-2][i+2]==piece and board[j-3][i+3]==piece:
				return True

board= creating_board()
print_board(board)
game_over=False
turn=0 

while not game_over:
	# Ask for Player 1 Input
	if turn==0:
		selectColumn=int(input("Player 1 Make your Selection from (0-6):"))
		if is_valid_location(board,selectColumn):
			row=get_next_open_row(board,selectColumn)
			drop_piece(board,row,selectColumn,1)

			if winning_move(board,1):
				print("\nPlayer 1 Wins !!! YEYYYYY!!!")
				game_over=True

		else:
			print("\nWarning : Column filled... Please use other Column")
			turn=turn-1

	# Ask Player 2 Input
	else:
		selectColumn=int(input("Player 2 Make your Selection from (0-6):"))
		if is_valid_location(board,selectColumn):
			row=get_next_open_row(board,selectColumn)
			drop_piece(board,row,selectColumn,2)

			if winning_move(board,2):
				print("\nPlayer 2 Wins !!! YEYYYYY!!!")
				game_over=True

		else:
			print("\nWarning : Column filled... Please use other Column")
			turn=turn-1	

	print_board(board)

	turn=turn+1
	turn=turn%2
