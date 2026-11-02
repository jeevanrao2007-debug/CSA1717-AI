from collections import deque


def read_state(prompt):
    while True:
        values = list(map(int, input(prompt + " (9 numbers, 0 is blank): ").split()))
        if len(values) == 9 and sorted(values) == list(range(9)):
            return tuple(values)
        print("Enter each number from 0 to 8 exactly once.")


def solve(start, goal):
    queue = deque([start])
    parent = {start: None}

    while queue:
        state = queue.popleft()
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        blank = state.index(0)
        row, column = divmod(blank, 3)
        for new_row, new_column in ((row - 1, column), (row + 1, column),
                                    (row, column - 1), (row, column + 1)):
            if 0 <= new_row < 3 and 0 <= new_column < 3:
                position = new_row * 3 + new_column
                next_state = list(state)
                next_state[blank], next_state[position] = (
                    next_state[position], next_state[blank]
                )
                next_state = tuple(next_state)
                if next_state not in parent:
                    parent[next_state] = state
                    queue.append(next_state)
    return None


def display(state):
    for index in range(0, 9, 3):
        print(*state[index:index + 3])
    print()


start = read_state("Enter initial state")
goal = read_state("Enter goal state")
path = solve(start, goal)

if path is None:
    print("No solution exists.")
else:
    print("Solution found in", len(path) - 1, "moves.")
    for step, state in enumerate(path):
        print("Step", step)
        display(state)
