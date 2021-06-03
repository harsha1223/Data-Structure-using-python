def add_node(v):
    if (v in graph):
        print("Given node is already present in the graph")
    else:
        graph [v] = []

# for undirected and unweighted graph
def add_edge(v1,v2):
    if(v1 not in graph):
        print(v1,"is not present in the graph")
    elif(v2 not in graph):
        print(v2,"is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

# for undirected and weighted graph
def add_edge_cost(v1,v2,cost):
    if(v1 not in graph):
        print(v1,"is not present in the graph")
    elif(v2 not in graph):
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

graph = {}
add_node("A")
add_node("B")
add_node("C")
add_edge_cost("A","B",10)
print(graph)