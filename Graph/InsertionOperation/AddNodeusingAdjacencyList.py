def add_node(v):
    if (v in graph):
        print("Given node is already present in the graph")
    else:
        graph [v] = []

graph = {}
add_node("A")
add_node("B")
print(graph)