class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # não direcionado
    
    def hamiltonian_path_util(self, path, visited):
        if len(path) == self.V:
            return True
        
        last_vertex = path[-1]
        for neighbor in self.adj_list[last_vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                path.append(neighbor)
                if self.hamiltonian_path_util(path, visited):
                    return True
                path.pop()
                visited[neighbor] = False
        
        return False
    
    def find_hamiltonian_path(self):
        for start_vertex in range(self.V):
            visited = [False] * self.V
            path = [start_vertex]
            visited[start_vertex] = True
            if self.hamiltonian_path_util(path, visited):
                return path
        return None

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 0)
    
    path = g.find_hamiltonian_path()
    if path:
        print("Caminho Hamiltoniano encontrado:", path)
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")
