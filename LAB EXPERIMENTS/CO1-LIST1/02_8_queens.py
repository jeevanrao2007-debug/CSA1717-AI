def solve_queens(size):
    solutions = []
    columns = set()
    diagonals = set()
    reverse_diagonals = set()
    board = [-1] * size

    def place(row):
        if row == size:
            solutions.append(board[:])
            return
        for column in range(size):
            if (column in columns or row - column in diagonals or
                    row + column in reverse_diagonals):
                continue
            board[row] = column
            columns.add(column)
            diagonals.add(row - column)
            reverse_diagonals.add(row + column)
            place(row + 1)
            columns.remove(column)
            diagonals.remove(row - column)
            reverse_diagonals.remove(row + column)

    place(0)
    return solutions


def display(solution):
    for column in solution:
        print(" ".join("Q" if index == column else "." for index in range(len(solution))))


size = int(input("Enter the number of queens: "))
if size < 1:
    print("The number of queens must be positive.")
else:
    solutions = solve_queens(size)
    print("Number of solutions:", len(solutions))
    if solutions:
        print("First solution:")
        display(solutions[0])
