from itertools import permutations


count = int(input("Enter number of cities: "))
if count < 2:
    print("At least two cities are required.")
else:
    distances = []
    print("Enter the distance matrix row by row:")
    for row in range(count):
        values = list(map(int, input("Row " + str(row + 1) + ": ").split()))
        if len(values) != count:
            raise ValueError("Each row must contain exactly " + str(count) + " values.")
        distances.append(values)

    start = int(input("Enter starting city (0 to " + str(count - 1) + "): "))
    if not 0 <= start < count:
        print("Invalid starting city.")
    else:
        others = [city for city in range(count) if city != start]
        best_cost = float("inf")
        best_route = None
        for permutation in permutations(others):
            route = (start,) + permutation + (start,)
            cost = sum(distances[route[index]][route[index + 1]]
                       for index in range(len(route) - 1))
            if cost < best_cost:
                best_cost = cost
                best_route = route
        print("Best route:", " -> ".join(map(str, best_route)))
        print("Minimum cost:", best_cost)
