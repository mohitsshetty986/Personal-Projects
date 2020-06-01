import numpy as np 
import pygame
import sys
import math

RED=(255,0,0)
BLACK=(0,0,0)
YELLOW=(255, 255, 0)
GREEN=(0,255,0)

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
	print(np.flip(board,0),"              0 is for unoccupied positions")   # 0 inside flip function is X-axis

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

'''PYgame introduction'''

# Hey Mohit pygame website documentation check out

def draw_board(board):
	for m in range(column_count):
		for n in range(row_count):
			pygame.draw.rect(screen,RED,(m*positionsize,n*positionsize+positionsize,positionsize,positionsize))
			pygame.draw.circle(screen,BLACK,(int(m*positionsize+positionsize/2),int(n*positionsize+positionsize+positionsize/2)),circleradius)
	
	for m in range(column_count):
		for n in range(row_count):
			if board[n][m]==1:
				pygame.draw.circle(screen,YELLOW,(int(m*positionsize+positionsize/2),height-int(n*positionsize+positionsize/2)),circleradius)
			elif board[n][m]==2:
				pygame.draw.circle(screen,GREEN,(int(m*positionsize+positionsize/2),height-int(n*positionsize+positionsize/2)),circleradius)	
	pygame.display.update()

pygame.init()

positionsize=100 

width= column_count*positionsize
height=(row_count+1)*positionsize

size=(width,height)
circleradius=int(positionsize/2 - 5)

screen=pygame.display.set_mode(size)     

draw_board(board)

winningfont=pygame.font.SysFont("monospace",20)
while not game_over:

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()

		if event.type==pygame.MOUSEMOTION:
			pygame.draw.rect(screen,BLACK,(0,0,width,positionsize))
			position_x=event.pos[0]
			if turn==0:
				pygame.draw.circle(screen,YELLOW,(position_x,int(positionsize/2)),circleradius)
			else:
				pygame.draw.circle(screen,GREEN,(position_x,int(positionsize/2)),circleradius)
		pygame.display.update()

		if event.type==pygame.MOUSEBUTTONDOWN:
			#print(event.pos)
			# Ask for Player 1 Input
			if turn==0:
				position_x=event.pos[0]   #between 0 and 700
				selectColumn= int(math.floor(position_x/positionsize))

				if is_valid_location(board,selectColumn):
					row=get_next_open_row(board,selectColumn)
					drop_piece(board,row,selectColumn,1)

					if winning_move(board,1):
						label=winningfont.render("Player 1 Wins !!! YEYYYYY!!!",1,(RED))
						screen.blit(label,(40,10)) #label prints in the specified position
						game_over=True

				else:
					label=winningfont.render("Warning : Column filled... Please use other Column",1,(RED))
					screen.blit(label,(40,10))
					turn=turn-1

			# Ask Player 2 Input
			else:
				position_x=event.pos[0]   #between 0 and 700
				selectColumn= math.floor(position_x/positionsize)
				if is_valid_location(board,selectColumn):
					row=get_next_open_row(board,selectColumn)
					drop_piece(board,row,selectColumn,2)

					if winning_move(board,2):
						label=winningfont.render("Player 2 Wins !!! YEYYYYY!!!",1,(RED))
						screen.blit(label,(40,10)) #label prints in the specified position
						game_over=True

				else:
					label=winningfont.render("Warning : Column filled... Please use other Column",1,(RED))
					screen.blit(label,(40,10))
					turn=turn-1	

			print_board(board)
			draw_board(board)

			turn=turn+1
			turn=turn%2

			if game_over:
				pygame.time.wait(10000)



'''
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
'''