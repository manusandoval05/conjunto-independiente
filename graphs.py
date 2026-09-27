class Vertex:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.neighbors: list['Vertex'] = []

    def add_neighbor(self, neighbor: 'Vertex') -> None:
        self.neighbors.append(neighbor)

class Edge:
    
    def __init__(self, origin: Vertex, destination: Vertex):
        self.origin: Vertex = origin
        self.destination: Vertex = destination

class Graph:

    def __init__(self):
        self.vertices: dict[str, Vertex] = {}
        self.edges: list[Edge] = []

    def add_vertex(self, name: str) -> None:
        if name not in self.vertices:
            vertex = Vertex(name)
            self.vertices[name] = vertex

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

    def get_reduced_graph(self, neighborhood):
        reduced_graph = Graph()
        for vertex_name in neighborhood:
            reduced_graph.add_vertex(vertex_name)
        for edge in self.edges:
            if edge.origin.name in neighborhood and edge.destination.name in neighborhood:
                reduced_graph.add_edge(edge.origin, edge.destination)
        return reduced_graph

    def is_independent_set(self, vertices: set[str]) -> bool:
        for edge in self.edges:
            if edge.origin.name in vertices and edge.destination.name in vertices:
                return False
        return True

    def get_arbitrary_vertex(self) -> str | None:
        if not self.vertices:
            return None
        return list(self.vertices.values())[0]  