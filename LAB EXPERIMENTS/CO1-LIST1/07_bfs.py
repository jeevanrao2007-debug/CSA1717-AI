from collections import deque


def read_graph():
    count = int(input("Enter number of vertices: "))
    graph = {vertex: [] for vertex in range(count)}
    edge_count = int(input("Enter number of edges: "))
    for index in range(edge_count):
        first, second = map(int, input("Edge " + str(index + 1) + " (u v): ").split())
        graph[first].append(second)
        graph[second].append(first)
    return graph


def bfs(graph, start):
    order = []
    queue = deque([start])
    visited = {start}
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


graph = read_graph()
start = int(input("Enter starting vertex: "))
if start in graph:
    print("BFS traversal:", *bfs(graph, start))
else:
    print("Starting vertex does not exist.")
