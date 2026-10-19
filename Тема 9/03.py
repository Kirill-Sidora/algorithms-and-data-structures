class AdjacencyMatrixGraph:

    def __init__(self, vertices=None):
        self.vertices = []
        self.index = {}
        self.matrix = []

        if vertices:
            for v in vertices:
                self.add_vertex(v)

    def add_vertex(self, vertex):
        if vertex in self.index:
            return
        self.index[vertex] = len(self.vertices)
        self.vertices.append(vertex)
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * len(self.vertices))

    def add_edge(self, source, target):
        if source not in self.index:
            self.add_vertex(source)
        if target not in self.index:
            self.add_vertex(target)
        i, j = self.index[source], self.index[target]
        self.matrix[i][j] = 1

    def has_edge(self, source, target):
        if source not in self.index or target not in self.index:
            return False
        return self.matrix[self.index[source]][self.index[target]] == 1

    def __repr__(self):
        header = "      " + " ".join(f"{v:>3}" for v in self.vertices)
        rows = [header]
        for i, v in enumerate(self.vertices):
            row = f"{v:>3} | " + " ".join(f"{x:>3}" for x in self.matrix[i])
            rows.append(row)
        return "\n".join(rows)

def build_matrix_from_edges(edges, directed=True):
    g = AdjacencyMatrixGraph()
    for u, v in edges:
        g.add_edge(u, v)
        if not directed:
            g.add_edge(v, u)
    return g