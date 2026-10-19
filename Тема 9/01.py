class DirectedGraph:

    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = set()

    def add_edge(self, source, target):
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency[source].add(target)

    def get_vertices(self):
        return list(self.adjacency.keys())

    def get_edges(self):
        return [(u, v) for u in self.adjacency for v in self.adjacency[u]]

    def __repr__(self):
        lines = [f"  {u} → {sorted(self.adjacency[u])}"
                 for u in sorted(self.adjacency, key=str)]
        return "DirectedGraph:\n" + "\n".join(lines)