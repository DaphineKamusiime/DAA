
board = [ 
    [3,0,5,0,1,0],
    [0,0,0,0,0,0],
    [2,0,6,0,0,0],
    [0,0,0,3,0,6],
    [0,0,0,0,0,0],
    [0,5,0,6,0,4]
   
    ]

def print_board(board):#Formatting the board 
    for row_ in range(len(board)):
        if row_ % 2== 0 and row_ != 0:
            print("* * * * * * *")

        for column in range(len(board[0])):
            if column % 3 == 0 and column != 0:
                print("|", end="")

            if column == 5:
                print(board[row_][column])
            else:
                print(str(board[row_][column]) + " ", end="")


def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet 
    # returning  row, col tuple (or (None, None) if there is none)

    #  we are using 0-5 for our indices
    
    for row_ in range(6):
        for column in range(6): 
            if puzzle[row_][column] == 0:
                return row_, column

    return None, None  # if no spaces in the puzzle are empty

def valid(puzzle, input, row, col):

    #  starting  with the row
    row_vals = puzzle[row]
    if input in row_vals:
        return False # if we've repeated, then our input is not valid!

    # then  the column
    column_vals = [puzzle[i][col] for i in range(6)]
    if input in column_vals:
        return False

    # and then the square
    row_start = (row // 2) * 2
    col_start = (col // 3) * 3

    for row_ in range(row_start, row_start + 2):
        for column in range(col_start, col_start + 3):
            if puzzle[row_][column] == input:
                return False

    return True

def solution(puzzle):

    row, col = find_next_empty(puzzle)

    #if there's no empty space  left, then we're done because we only allowed valid inputs
    if row is None:  # this is true if our find_next_empty function returns None, None
        return True 
    
    #if there is a place to put a number, then make an input between 1 and 6
    for input  in range(1, 7): 
        #check if this is a valid input
        if valid(puzzle, input, row, col):
            #if this is a valid input, then place it at that spot on the puzzle
            puzzle[row][col] = input
            # recursively calling our solver..............
            if solution(puzzle):
                return True
        
        #if invalid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = 0

    #if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False


print("ORIGINAL BOARD\n")
print_board(board)
solution(board)
print("\n\nSOLVED BOARD\n")
print_board(board)
