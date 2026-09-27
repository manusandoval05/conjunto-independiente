from graphs import Graph

def read_graph_from_file(file_path: str) -> Graph | None:
    graph: Graph = Graph()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines: list[str] = [line.strip() for line in f if line.strip()]
            
            if not lines:
                print("Error: The file is empty.")
                return None

            vertex_names: list[str] = lines[0].split(',')
            for name in vertex_names:
                graph.add_vertex(name.strip())

            for line in lines[1:]:
                origin, destination = line.split(',')
                graph.add_edge(origin.strip(), destination.strip())
                
        return graph

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except ValueError:
        print("Error: Incorrect format. Make sure to separate values by commas.")
        return None