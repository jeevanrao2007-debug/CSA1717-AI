from collections import deque

def water_jug(a, b, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (x, y), path = queue.popleft()
        if x == target or y == target:
            return path
        pour_xy = min(x, b - y)
        pour_yx = min(y, a - x)
        moves = [(a, y), (x, b), (0, y), (x, 0),
                 (x - pour_xy, y + pour_xy),
                 (x + pour_yx, y - pour_yx)]
        for n in moves:
            if n not in visited:
                visited.add(n)
                queue.append((n, path + [n]))
    return None

path = water_jug(4, 3, 2)
if path:
    print("Steps to measure 2 litres:")
    for s in path:
        print(s)
else:
    print("No solution")
