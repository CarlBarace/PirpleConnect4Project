import sys
from termcolor import colored, cprint

def currentfield(playfield):
    for row in range (11):
        if row%2 == 0:
            ActualRow = int(row/2)
            print("|",end="")
            for column in range (13):
                if column%2 == 0:
                    Actualcolumn = int(column/2)
                    print(reverse[ActualRow][Actualcolumn],end="")
                else:
                    print("|", end="")
            print("|",end="")
        else:
            print("")
            print("-"*15)

def exceed (board, col):
    return board[5][col] == " "
def valid(board, turn):
     for r in range(6):
            if board[r][turn] == " ":
                return r
def winner (board,piece):
    #Check for Horizontal
    for row in range(11):
        if row%2 == 0:
            ActualRow = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    Actualcolumn = int(column/2)
                    for col in range(7-3):
                        for r in range(6):
                            if board[ActualRow][Actualcolumn] == piece and board[ActualRow][Actualcolumn+1] == piece and board[ActualRow][Actualcolumn+2] == piece and board[ActualRow][Actualcolumn+3] == piece:
                                return True
    #Check for Vertical
    for row in range(11):
        if row%2 == 0:
            ActualRow = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    Actualcolumn = int(column/2)
                    for col in range(7):
                        for r in range(6-3):
                            if board[ActualRow][Actualcolumn] == piece and board[ActualRow+1][Actualcolumn] == piece and board[ActualRow+2][Actualcolumn] == piece and board[ActualRow+3][Actualcolumn] == piece:
                                return True
  #Check for Diagonal
    for row in range(11):
        if row%2 == 0:
            ActualRow = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    Actualcolumn = int(column/2)
                    for col in range(7-3):
                        for r in range(6-3):
                            if board[ActualRow][Actualcolumn] == piece and board[ActualRow+1][Actualcolumn+1] == piece and board[ActualRow+2][Actualcolumn+2] == piece and board[ActualRow+3][Actualcolumn+3] == piece:
                                return True
    
    for row in range(11):
        if row%2 == 0:
            ActualRow = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    Actualcolumn = int(column/2)
                    for col in range(7-3):
                        for r in range(3,6):
                            if board[ActualRow][Actualcolumn] == piece and board[ActualRow-1][Actualcolumn+1] == piece and board[ActualRow-2][Actualcolumn+2] == piece and board[ActualRow-3][Actualcolumn+3] == piece:
                                return True


Player = 1
field = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
reverse = field[::-1]
currentfield(field)

game = True
while(game):
    print("")
    print("Player ",Player)
    column = int(input("Enter player column (0-6): "))
    if column <6:
        if Player == 1:
            piece = colored("X", 'red', attrs =['bold'])    
            row = valid(field,column)
            field[row][column] = piece
            if winner(field,piece):
                print("")
                print("Player 1 Wins")
                game = False           
            Player = 2
        else:
            piece = colored("0", 'yellow', attrs =['bold']) 
            row = valid(field, column)
            field[row][column] = piece
            if winner(field,piece):
                print("")
                print("Player 2 Wins")
                game = False           
            Player = 1
    reverse = field[::-1]
    currentfield(reverse)

        
   