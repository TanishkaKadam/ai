#practical 4
#Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and
Backtracking for n-queens problem or a graph coloring problem.


def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print("1" if board[i][j] else "0", end=" ")
        print()
    print()


def solve_nqueens_bnb(n):
    board = [[0]*n for _ in range(n)]
    row_lookup = [False]*n
    slash_lookup = [False]*(2*n-1)
    backslash_lookup = [False]*(2*n-1)

    def is_safe(row, col):
        return not row_lookup[row] and not slash_lookup[row + col] and not backslash_lookup[row - col + n - 1]

    def place_queen(col):
        if col >= n:
            print_board(board, n)
            return True  # Found at least one solution

        res = False
        for row in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                row_lookup[row] = True
                slash_lookup[row + col] = True
                backslash_lookup[row - col + n - 1] = True

                res = place_queen(col + 1) or res  # Try for next column

                # Backtrack
                board[row][col] = 0
                row_lookup[row] = False
                slash_lookup[row + col] = False
                backslash_lookup[row - col + n - 1] = False
        return res

    if not place_queen(0):
        print("No solution exists")


# ===== MAIN CODE =====
n = int(input("Enter number of queens for N-Queens (Branch & Bound): "))
solve_nqueens_bnb(n)



output :
tanishka@tanishka-Latitude-5490:~$ python3 nqueen4.py
Enter number of queens for N-Queens (Branch & Bound): 4
0 0 1 0 
1 0 0 0 
0 0 0 1 
0 1 0 0 

0 1 0 0 
0 0 0 1 
1 0 0 0 
0 0 1 0 

tanishka@tanishka-Latitude-5490:~$ python3 nqueen4.py
Enter number of queens for N-Queens (Branch & Bound): 2
No solution exists
tanishka@tanishka-Latitude-5490:~$ python3 nqueen4.py
Enter number of queens for N-Queens (Branch & Bound): 6
0 0 0 1 0 0 
1 0 0 0 0 0 
0 0 0 0 1 0 
0 1 0 0 0 0 
0 0 0 0 0 1 
0 0 1 0 0 0 



