import math 
import random

def print_board(board):
    RED = "\033[31m"
    BLACK = "\033[37m"
    
    N = len(board)
    n = math.floor(math.sqrt(N))
    assert N == n*n

    board_string = ""
    for row in range(N):
        if row > 0 and row % n == 0:
            board_string += "\n"
        for col in range(N):
            if col > 0 and col % n == 0: 
                board_string += " "
            value = board[row][col]
            if value != 0:
                board_string += RED
            else:
                board_string += BLACK
            board_string += "[{:02.0f}]".format(value)
            
        board_string += "\n" + BLACK

    print(board_string)

#makes the puzzle given size N which should be a square
def make_puzzle(N):
    #makes a list of list using the shorthand
    puz = [[0 for i in range(N)]for q in range(N)]
    #gets random x and y index
    x = random.randint(0,N-1)
    y = random.randint(0,N-1)
    #makes empty sets
    row_sets = []
    col_sets = []
    reg_sets = []
    #find the sqrt of N aka why N should be a square
    n = int(math.sqrt(N))
    #for i in range N
    for i in range(1,N+1):
        #makes sure the x and y value dont have a value already there and if it does gets new x and y
        while puz[x][y] != 0:
            x = random.randint(0,N-1)
            y = random.randint(0,N-1)
        #sets puz x and y to the value of i
        puz[x][y] = i
    #looping through rows and collums
    for i in range(N):
        #makes empty sets
        rset = set()
        cset = set()
        #the loop for either col or rows
        for j in range(N):
            # if i j isnt zero adds it to row set and if j i isnt zero adds to colum set
            if puz[i][j] != 0:
                rset.add(puz[i][j])
            if puz[j][i] != 0:
                cset.add(puz[j][i])
        #adds the finished sets to col sets and row sets
        col_sets.append(cset)
        row_sets.append(rset)
    #for loops that break it into squares
    for i in range(n):
        for j in range(n):
            #reg set made
            gset = set()
            #goes through each value in the square
            for g in range(n):
                for k in range(n):
                    #if the value isnt equal to zero adds to reg set
                    if puz[n*i+g][n*j+k] != 0:
                        gset.add(puz[n*i+g][n*j+k])
            #adds reg set to list of reg sets
            reg_sets.append(gset)
    #returns dictionary of board and the list of sets for row col and reg
    puzzle = {"board":puz,"row_sets":row_sets,"col_sets":col_sets,"reg_sets":reg_sets}
    return puzzle


        
#gets the square and returns the value and the sets it is a part of
def get_square(puzzle, row, col):
    #gets the value rowset and colset and regset of given locationm
    value = puzzle["board"][row][col]
    rows = puzzle["row_sets"][row]
    cols = puzzle["col_sets"][col]
    n = math.sqrt(len(puzzle["board"][0]))
    regs = puzzle["reg_sets"][int((row//n*n)+(col//n))]
    #adds them to square dictionary and returns it
    square = {"value":value,"row_sets":rows,"col_sets":cols,"reg_sets":regs}
    return square

#adds a value to spot if it is empty and follows all rules
def move(puzzle, row, col, new_value):
    #gets the dictionary of the spot using get square
    spot = get_square(puzzle,row,col)
    #first checks if spot value equals to zero aka empty and if not returns false
    if spot["value"] == 0:
        #checks if the rowset colset and regset dont already contain the new value and if it does returns false
        if new_value in spot["row_sets"] or new_value in spot["col_sets"] or new_value in spot["reg_sets"]:
            return False
        else:
            #otherwise adds the newvalue to all areas and returns true
            puzzle["board"][row][col] = new_value
            puzzle["row_sets"][row].add(new_value)
            puzzle["col_sets"][col].add(new_value)
            n = math.sqrt(len(puzzle["board"][0]))
            puzzle["reg_sets"][int((row//n*3)+(col//n))].add(new_value)
            return True
    else:
        return False


#fills the puzzle to best of abilities
def fill_puzzle(puzzle):
    #gets the N length of the puzzle
    N = len(puzzle["board"][0])
    # runs for N**sqrt(N)
    for _ in range(N**int(math.sqrt(N))):
        #gets random number 1-N and random location
        new = random.randint(1,N)
        x = random.randint(0,N-1)
        y = random.randint(0,N-1)
        #while the x and y location isnt 0 re randomizez them till it gets a place that is empty
        while puzzle["board"][x][y] != 0:
            x = random.randint(0,N-1)
            y = random.randint(0,N-1)
        #then trys to call move with the location and new value
        move(puzzle,x,y,new)
    
#main
def main():
    N = 16
    print("Board size:", N, "x", N)
    puzzle = make_puzzle(N)
    print("Initial puzzle:")
    print(puzzle)
    print("Initial board:")
    print_board(puzzle['board'])
    fill_puzzle(puzzle)
    print_board(puzzle["board"])

     
main()
