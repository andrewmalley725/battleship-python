import random
from numpy import *
from numpy.linalg import *

ships = {'B':5,'C':4,'S':3,'D':4} #ship name & length
BOARD_SIZE = 7 #must be 2 greater than length of biggest ship to work w/out bugs
NUM_TRYS = 8 #number of times the user can miss


def Missed(board,i,j):
    board[i][j] = 'O'
    

def PlayerBoard(board,i,j):
    board[i][j] = 'X'

                    
def PlaceHoriz(board): #this function basically checks if there is space enough to place a ship horizontally
    vool = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] in ships: #loop through entire board to see if token matches a key in ships dictionary
                x = ships[board[i][j]] - 1 #varible = key value minus one
                if x <= len(board) - (j+1):
                    while x > 0:
                        board[i][j+x] = board[i][j]
                        x-=1
                        vool = True                     #logic determines if ship extends left or right
                elif x <= j:
                    while x > 0:
                        board[i][j-x] = board[i][j]
                        x-=1
                        vool = True
                break
    return vool
            
def PlaceShips(board):
    if PlaceHoriz(board):
        PlaceHoriz(board)
        
def PrintBoard(board): #prints board in a good format
    lst = [' ']
    for i in range(1,BOARD_SIZE + 1):   #makes header for board
        lst.append(str(i))
    print(' '.join(lst))
    for i in range(len(board)):
        print(str(i+1), ' '.join(board[i]))
        
def ValidPoint(char):
    for i in ships:
        if char == i:
            return True
    return False

def Terminate(dit):
    kill = 0
    for i in dit:
        if dit[i] == 0: #checks to see which keys have a 0 value
            kill += 1 #increment kill if yes
    if kill == len(dit): #when kill reaches the length of the ships dictionary, the user has won
        return True
    return False

if __name__ == '__main__':
    
    board = [["*" for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)] #board with all solutions
    playerBoard = [["*" for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)] #board that gets displayed
    
    lst = list(range(1,BOARD_SIZE + 1)) #generates list of numbers from 1 to BOARD_SIZE
    lst2 = list(range(1,BOARD_SIZE + 1))
    random.shuffle(lst)  #randomly shuffles list
    random.shuffle(lst2)
    lst = lst[:4] #takes first 4 elements
    lst2 = lst2[:4]
    
    br = lst[0]
    bc = lst2[0]
    
    cr = lst[1]
    cc = lst2[1]
    
    sr = lst[2]
    sc = lst2[2]
    
    dr = lst[3]
    dc = lst2[3]
    
    board[br-1][bc-1] = "B" #places first letter of each ship on board based off random indexes generated above
    board[cr-1][cc-1] = "C"
    board[sr-1][sc-1] = "S"
    board[dr-1][dc-1] = "D"
    
    PlaceShips(board)

    k = random.randint(0,2)

    if k == 0: #randomly transpose board
        board = array(board).T
    
    PrintBoard(playerBoard)
    
    numTrys = 0

    
    while numTrys < NUM_TRYS:
        
        
        if Terminate(ships):
            print('You win!')
            PrintBoard(board)

        
        #add more logic statements to debug
        else:
            row = int(input("Guess row: "))
            col = int(input("Guess column: "))
            
            i = row - 1
            j = col - 1
        
            ship = board[i][j]
            
            if ship == 'B':
                print('**HIT**')
                board[i][j] = "X"
                PlayerBoard(playerBoard,i,j)
                ships[ship] -= 1
                if ships[ship] == 0: 
                    print('You sunk my Battleship!')  
            elif ship == 'C':
                print('**HIT**')
                board[i][j] = "X"
                PlayerBoard(playerBoard,i,j)
                ships[ship] -= 1
                if ships[ship] == 0:
                    print('You sunk my Cuiser!')
            elif ship == 'D':
                print('**HIT**')
                board[i][j] = "X"
                PlayerBoard(playerBoard,i,j)
                ships[ship] -= 1
                if ships[ship] == 0:
                    print('You sunk my Destroyer!')
            elif ship == 'S':
                print('**HIT**')
                board[i][j] = "X"
                PlayerBoard(playerBoard,i,j) 
                ships[ship] -= 1
                if ships[ship] == 0:
                    print('You sunk my Ship!')
            elif ValidPoint(ship) == False: #FIXME check for numbers out of range
                if numTrys < NUM_TRYS - 1:
                    if playerBoard[i][j] == 'X':
                        print('You already hit there!')
                    elif playerBoard[i][j] != 'X':
                        print('**MISS**')
                        numTrys += 1
                        Missed(playerBoard,i,j)
                        Missed(board,i,j)
                elif numTrys == NUM_TRYS - 1:
                    Missed(playerBoard,i,j)
                    Missed(board,i,j)
                    print()
                    print('Outta guesses!')
                    PrintBoard(board)
                    break

        print()
        PrintBoard(playerBoard)           
        print()
