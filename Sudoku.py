SIZE = 9

matrix = [
    [0,0,0,0,0,0,6,0,0],
    [0,0,0,0,0,7,0,0,1],
    [2,0,8,0,0,0,0,4,0],
    [6,0,0,0,0,0,0,0,0],
    [0,5,1,4,0,9,0,0,0],
    [0,0,0,5,0,0,0,2,0],
    [0,0,4,0,0,0,0,5,0],
    [0,0,7,1,9,6,0,0,0],
    [0,8,0,0,0,0,3,0,0]]

def print_sudoku():
    for i in matrix:
        print (i)

def number_unassigned(row, col):
    num_unassign = 0
    for i in range(0,SIZE):
        for j in range (0,SIZE):
            if matrix[i][j] == 0:
                row = i
                col = j
                num_unassign = 1
                a = [row, col, num_unassign]
                return a
    a = [-1, -1, num_unassign]
    return a

def is_safe(n, r, c):
    for i in range(0,SIZE):
        if matrix[r][i] == n:
            return False
    for i in range(0,SIZE):
        if matrix[i][c] == n:
            return False
    row_start = (r//3)*3
    col_start = (c//3)*3;
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if matrix[i][j]==n:
                return False
    return True

def solve_sudoku():
    row = 0
    col = 0

    a = number_unassigned(row, col)
    if a[2] == 0:
        return True
    row = a[0]
    col = a[1]
    for i in range(1,10):

        if is_safe(i, row, col):
            matrix[row][col] = i

            if solve_sudoku():
                return True
            matrix[row][col]=0
    return False

if solve_sudoku():
    print_sudoku()
else:
    print("No solution")