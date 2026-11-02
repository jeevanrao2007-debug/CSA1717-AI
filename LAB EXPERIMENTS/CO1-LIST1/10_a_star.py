import heapq


def read_graph():
    count = int(input("Enter number of vertices: "))
    graph = {vertex: [] for vertex in range(count)}
    edge_count = int(input("Enter number of directed edges: "))
    for index in range(edge_count):
        first, second, cost = input("Edge " + str(index + 1) + " (from to cost): ").split()
        graph[int(first)].append((int(second), float(cost)))
    return graph


def a_star(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start)]
    parent = {start: None}
    cost_so_far = {start: 0}

    while queue:
        _, current_cost, current = heapq.heappop(queue)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], current_cost

        for neighbor, edge_cost in graph[current]:
            new_cost = current_cost + edge_cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(queue, (priority, new_cost, neighbor))
                parent[neighbor] = current
    return None, None


graph = read_graph()
print("Enter one heuristic value for each vertex:")
heuristic = {vertex: float(input("h(" + str(vertex) + "): ")) for vertex in graph}
start = int(input("Enter start vertex: "))
goal = int(input("Enter goal vertex: "))

if start not in graph or goal not in graph:
    print("Start or goal vertex does not exist.")
else:
    path, cost = a_star(graph, heuristic, start, goal)
    if path is None:
        print("No path exists.")
    else:
        print("Best path:", " -> ".join(map(str, path)))
        print("Path cost:", cost)
