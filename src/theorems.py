from graphs import Graph

def get_independent_set(current_graph: Graph, original_graph: Graph, level: int = 0) -> set[str]:
    indent: str = "   " * level
    
    # Base Case: Induced subgraph is empty
    if not current_graph.vertices:
        print(f"{indent}Reached an empty graph. Returning an empty set.")
        return set()

    # Inductive Step
    v: str | None = current_graph.get_arbitrary_vertex()
    if v is None:
        return set()
        
    print(f"{indent}[Step {level + 1}] Selected vertex: '{v}'")

    neighborhood: set[str] = current_graph.get_neighborhood(v)
    print(f"{indent}The neighborhood N({v}) is: {neighborhood}")

    h_graph: Graph = current_graph.get_reduced_graph(neighborhood)
    print(f"{indent}The reduced subgraph H keeps vertices: {list(h_graph.vertices.keys())}")
    print(f"{indent}Recursive call to H")

    s_h: set[str] = get_independent_set(h_graph, original_graph, level + 1)

    possible_solution: set[str] = s_h.union({v})
    
    print(f"{indent}Returning to level {level + 1}. S(H) returned was: {s_h}")
    print(f"{indent}Evaluating if joining S(H) with '{v}' {possible_solution} is_independent function")
    
    # Check independence against the original graph to find potential conflicts
    if original_graph.is_independent_set(possible_solution):
        print(f"{indent}Yes, it is (Case 1). Keeping '{v}'.")
        return possible_solution
    else:
        print(f"{indent}No, it is not (Case 2). Conflict exists, discarding '{v}'.")
        return s_h