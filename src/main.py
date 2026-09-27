import sys
from graphs import Graph
from graph_file_reader import read_graph_from_file
from theorems import get_independent_set

def main() -> None:
    if len(sys.argv) < 2:
        print("Error: Missing input file.")
        print("Usage: python main.py file.txt")
        return

    graph: Graph | None = read_graph_from_file(sys.argv[1])
    
    if graph is None:
        return

    print("======================================================")
    print(" STARTING ALGORITHM: INDEPENDENT SET (Theorem 3.6)")
    print("======================================================\n")
    
    solution: set[str] = get_independent_set(graph, graph)
    
    print("\n======================================================")
    print(" FINAL RESULT")
    print("======================================================")
    print(f"The independent set S(G) found is: {solution}\n")

if __name__ == '__main__':
    main()