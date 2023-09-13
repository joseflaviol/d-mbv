class Graph:

    def __init__(self, number_of_vertices: int, oriented: bool = False):
        self.number_of_vertices = number_of_vertices
        self.oriented           = oriented
        self.adj_list           = []

        for _ in range(self.number_of_vertices):
            self.adj_list.append({})
    
    def add_edge(self, u: int, v: int, w: float = 0):
        if not (0 <= u < self.number_of_vertices) or not (0 <= v < self.number_of_vertices):
            return 

        self.adj_list[u][v] = w 

        if not self.oriented:
            self.adj_list[v][u] = w 
    
    def adj(self, u: int):
        try:
            return self.adj_list[u].keys()
        except IndexError:
            return []

    def weight(self, u: int, v: int):
        try:
            return self.adj_list[u][v]
        except IndexError:
            return None
        except KeyError:
            return None