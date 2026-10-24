INF = float("inf")

def floyd_warshall(graph):
    n = len(graph)

    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_matrix(dist, labels=None):
    n = len(dist)

    if labels is None:
        labels = [str(i) for i in range(n)]

    print("      " + " ".join(f"{l:>6}" for l in labels))

    for i in range(n):
        row = []

        for j in range(n):
            row.append("  INF " if dist[i][j] == INF else f"{dist[i][j]:>6}")

        print(f"{labels[i]:>4} |" + " ".join(row))