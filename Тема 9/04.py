class AdjacencyListGraph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = set()

    def add_edge(self, source, target):
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency[source].add(target)

    def has_edge(self, source, target):
        return (source in self.adjacency
                and target in self.adjacency[source])

    def __repr__(self):
        lines = [f"  {u} → {sorted(self.adjacency[u])}"
                 for u in sorted(self.adjacency, key=str)]
        return "AdjacencyListGraph:\n" + "\n".join(lines)

def build_list_from_edges(edges, directed=True):
    g = AdjacencyListGraph()
    for u, v in edges:
        g.add_edge(u, v)
        if not directed:
            g.add_edge(v, u)
    return g