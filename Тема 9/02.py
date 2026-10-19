from collections import deque

def bfs(graph, start):
    if start not in graph.adjacency:
        return []

    visited = set()
    result = []
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.adjacency[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result