def add_node(v):
    global node_count
    if (v in nodes):
        print("The node already present in the graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range (node_count):
            temp.append(0)
        graph.append(temp)

#for undirected and unweighted graph:
def add_edge(v1,v2):
    if(v1 not in nodes):
        print(v1,"is not present in the graph")
    elif(v2 not in nodes):
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph [index1][index2] = 1
        graph [index2][index1] = 1

#for undirected and/ weighted graph:
def add_edge_cost(v1,v2,cost):
    if(v1 not in nodes):
        print(v1,"is not present in the graph")
    elif(v2 not in nodes):
        print(v2,"is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph [index1][index2] = cost
        graph [index2][index1] = cost

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end=" ")
        print()
node_count = 0
nodes = [] 
graph = []

# print("Before adding nodes")
# print(nodes)
# print(graph)
# add_node("A")
# add_node("B")
# add_node("D")
# add_edge_cost("A" , "B" , 10)
# add_edge_cost("A" , "D" , 5)
# print("After adding nodes")
# print(nodes)
# print(graph)
# print_graph()