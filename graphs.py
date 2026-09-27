class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

class Edge:
    
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

class Graph:

    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, value):
        if value not in self.vertices:
            vertex = Vertex(value)
            self.vertices[value] = vertex

    def add_edge(self, origin, destination):
        edge = Edge(origin, destination)
        self.edges.append(edge)
        origin.add_neighbor(destination)

    def get_neighborhood(self, vertex_name):
        neighborhood = {vertex_name}
        if vertex_name in self.vertices:
            for neighbor in self.vertices[vertex_name].neighbors:
                neighborhood.add(neighbor.value)
        return neighborhood

    def get_reduced_graph(self, neighborhood):
        reduced_graph = Graph()
        for vertex_name in neighborhood:
            reduced_graph.add_vertex(vertex_name)
        for edge in self.edges:
            if edge.origin.value in neighborhood and edge.destination.value in neighborhood:
                reduced_graph.add_edge(edge.origin, edge.destination)
        return reduced_graph

    def is_independent_set(self, vertices): 
        for edge in self.edges:
            if edge.origin.value in vertices and edge.destination.value in vertices:
                return False
        return True

    def get_arbitrary_vertex(self):
        if not self.vertices:
            return None
        return list(self.vertices.values())[0]  