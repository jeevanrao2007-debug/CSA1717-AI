from collections import deque


def safe(missionaries, cannibals):
    return (missionaries == 0 or missionaries >= cannibals) and 0 <= missionaries <= 3 and 0 <= cannibals <= 3


def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    queue = deque([start])
    parent = {start: None}
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        state = queue.popleft()
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]
        left_m, left_c, boat = state
        for moved_m, moved_c in moves:
            if boat == 0:
                next_state = (left_m - moved_m, left_c - moved_c, 1)
            else:
                next_state = (left_m + moved_m, left_c + moved_c, 0)
            right_m, right_c = 3 - next_state[0], 3 - next_state[1]
            if (safe(next_state[0], next_state[1]) and
                    safe(right_m, right_c) and next_state not in parent):
                parent[next_state] = state
                queue.append(next_state)
    return None


path = solve()
if path is None:
    print("No solution exists.")
else:
    for step, (missionaries, cannibals, boat) in enumerate(path):
        side = "left" if boat == 0 else "right"
        print("Step", step, ": left =", missionaries, "missionaries,",
              cannibals, "cannibals; boat on", side)
