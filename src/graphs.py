class Vertex:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.neighbors: list['Vertex'] = []

    def add_neighbor(self, neighbor: 'Vertex') -> None:
        self.neighbors.append(neighbor)

class Edge:
    def __init__(self, origin: Vertex, destination: Vertex) -> None:
        self.origin: Vertex = origin
        self.destination: Vertex = destination

class Graph:
    def __init__(self) -> None:
        self.vertices: dict[str, Vertex] = {}
        self.edges: list[Edge] = []

    def add_vertex(self, name: str) -> None:
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)

    def add_edge(self, origin: str, destination: str) -> None:
        if origin in self.vertices and destination in self.vertices:
            edge = Edge(self.vertices[origin], self.vertices[destination])
            self.edges.append(edge)
            self.vertices[origin].add_neighbor(self.vertices[destination])

    def get_neighborhood(self, vertex_name: str) -> set[str]:
        neighborhood = {vertex_name}
        if vertex_name in self.vertices:
            for neighbor in self.vertices[vertex_name].neighbors:
                neighborhood.add(neighbor.name)
        return neighborhood

    def get_reduced_graph(self, neighborhood: set[str]) -> 'Graph':
        reduced_graph = Graph()
        
        for vertex_name in self.vertices:
            if vertex_name not in neighborhood:
                reduced_graph.add_vertex(vertex_name)
                
        
        for edge in self.edges:
            if edge.origin.name not in neighborhood and edge.destination.name not in neighborhood:
                reduced_graph.add_edge(edge.origin.name, edge.destination.name)
                
        return reduced_graph

    def is_independent_set(self, vertex_names: set[str]) -> bool:
        for edge in self.edges:
            if edge.origin.name in vertex_names and edge.destination.name in vertex_names:
                return False
        return True

    def get_arbitrary_vertex(self) -> str | None:
        if not self.vertices:
            return None
        return list(self.vertices.keys())[0]