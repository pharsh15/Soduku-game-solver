N = 9 # number of rows/columns

# To check if it is okay to assign a number (1-9) to a cell
def isSafe(sudoku, row, col, num):

    # checks if same number in a row
    for i in range(9):
        if sudoku[row][i]==num:
            return False

    # checks if same number in a column
    for i in range(9):
        if sudoku[i][col]==num:
            return False

    # calculations so that we can be in the same grid until all the cells in a grid checked.
    startRow = row - row % 3
    startCol = col - col % 3

    # checks if same number in a grid
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startCol + j]==num:
                return False

    # returned if a number is unique at its place as per the rules
    return True

# assigning values to unassigned cells
def solveSudoku(sudoku, row, col):
    if row==N-1 and col==N:
        return True

    if col==N:
        row +=1
        col = 0

    if sudoku[row][col]>0:
        return solveSudoku(sudoku, row, col+1)

    for num in range(1, N+1):
        if isSafe(sudoku, row, col, num):
            sudoku[row][col] = num

            if solveSudoku(sudoku, row, col+1):
                return True

        sudoku[row][col]=0
    return False

# driver function
def solver(sudoku):
    if solveSudoku(sudoku, 0, 0):
        return sudoku
    else:
        return "No"