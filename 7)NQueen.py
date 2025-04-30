# N-Queens Problem using Backtracking and Branch and Bound

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print('Q' if board[i][j] else '.', end=' ')
        print()
    print()

# Function to solve N-Queens
def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Branch and Bound helpers
    column = [False] * n
    left_diagonal = [False] * (2 * n - 1)  # (row - col + n-1)
    right_diagonal = [False] * (2 * n - 1)  # (row + col)

    # Recursive function for solving
    def solve(row):
        if row == n:
            print_solution(board, n)
            return
        
        for col in range(n):
            if not column[col] and not left_diagonal[row - col + n - 1] and not right_diagonal[row + col]:
                # Place queen
                board[row][col] = 1
                column[col] = left_diagonal[row - col + n - 1] = right_diagonal[row + col] = True

                # Recurse to next row
                solve(row + 1)

                # Backtrack
                board[row][col] = 0
                column[col] = left_diagonal[row - col + n - 1] = right_diagonal[row + col] = False

    solve(0)

# User input
print("Enter number of queens (N):")
n = int(input())

# Solve N-Queens
solve_n_queens(n)
