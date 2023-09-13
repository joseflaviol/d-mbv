from graph.graph_class import Graph
from random            import shuffle

class DFS:

    def __init__(self, graph: Graph):
        self.graph   = graph
        self.visited = [False] * self.graph.number_of_vertices
        self.depth   = [None]  * self.graph.number_of_vertices
        self.n       = []
        self.d       = []
        c = 0
        for v in range(self.graph.number_of_vertices):
            if not self.visited[v]:
                c += 1
                self.visited[v] = True 
                self.depth[v]   = 0
                self.dfs_visit(v)
        if c > 1:
            print("nao conectado")

    def dfs_visit(self, u: int):
        
        self.n.append(u)
        self.d.append(self.depth[u])

        shuffle(list(self.graph.adj(u)))

        for v in list(self.graph.adj(u)):
            if not self.visited[v]:
                self.visited[v] = True 
                self.depth[v]   = self.depth[u] + 1
                self.dfs_visit(v)

    def get_npe(self):
        return self.n, self.d