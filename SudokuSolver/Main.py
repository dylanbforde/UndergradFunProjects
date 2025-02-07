import SudokuSolver.SudokuSolver as s

if __name__=="__main__":

    to_solve = s.SudokuSolver()

    to_solve.grid = [[0, 0, 7, 3, 0, 8, 1, 0, 0],
        [0, 4, 0, 9, 0, 2, 0, 8, 0],
        [0, 0, 9, 0, 5, 0, 7, 0, 0],
        [9, 5, 0, 0, 0, 0, 0, 1, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 8, 0, 0, 0, 0, 0, 2, 7],
        [0, 0, 1, 0, 4, 0, 2, 0, 0],
        [0, 0, 0, 2, 0, 6, 0, 5, 0],
        [0, 0, 5, 1, 0, 7, 9, 0, 0]]
        
    # if success print the grid
    if(to_solve.solve_sudoku(to_solve.grid)):
        to_solve.print_grid(to_solve.grid)
    else:
        print ("No solution exists")