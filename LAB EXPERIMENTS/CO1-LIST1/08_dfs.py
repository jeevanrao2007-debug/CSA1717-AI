def read_graph():
    count = int(input("Enter number of vertices: "))
    graph = {vertex: [] for vertex in range(count)}
    edge_count = int(input("Enter number of edges: "))
    for index in range(edge_count):
        first, second = map(int, input("Edge " + str(index + 1) + " (u v): ").split())
        graph[first].append(second)
        graph[second].append(first)
    return graph


def dfs(graph, start):
    order = []
    visited = set()

    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order


graph = read_graph()
start = int(input("Enter starting vertex: "))
if start in graph:
    print("DFS traversal:", *dfs(graph, start))
else:
    print("Starting vertex does not exist.")
