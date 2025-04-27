def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()
    print()

def is_safe(board, row, col, n, cols, diag1, diag2):
    # Check if the column or diagonals are attacked
    if cols[col] or diag1[row + col] or diag2[row - col + n - 1]:
        return False
    return True

def solve_n_queens(board, row, n, cols, diag1, diag2):
    if row == n:
        print_solution(board, n)
        return True

    found_solution = False
    for col in range(n):
        if is_safe(board, row, col, n, cols, diag1, diag2):
            # Place queen
            board[row][col] = 1
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True

            found_solution |= solve_n_queens(board, row + 1, n, cols, diag1, diag2)

            # Backtrack
            board[row][col] = 0
            cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    return found_solution

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    if not solve_n_queens(board, 0, n, cols, diag1, diag2):
        print("No solution exists")

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    n_queens(n)
