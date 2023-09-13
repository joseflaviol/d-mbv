from graph.graph_class import Graph
from graph.dfs         import DFS

class NPE:

    def __init__(self, graph: Graph, autostart = True):
        self.graph     = graph
        
        if autostart:
            self.n, self.d = DFS(self.graph).get_npe()
    
    def decode(self):
        edges = []
        roots = [None] * self.graph.number_of_vertices

        roots[0] = self.n[0]
        j        = 1

        while j < len(self.n):
            k = roots[self.d[j] - 1]
            edges.append((k, self.n[j]))
            roots[self.d[j]] = self.n[j]
            j = j + 1
        
        return edges
