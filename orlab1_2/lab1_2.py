import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nodes = [1, 2, 3, 4, 5]
# edges_with_weight = [(1, 2, 10), (1, 4, 5), (2, 3, 3), (2, 4, 9), (2, 5, 11), (2, 6, 5), (3, 6, 10), (4, 5, 6),
# (4, 7, 15),(4, 8, 13), (5, 6, 10), (5, 8, 5), (6, 8, 7), (6, 9, 8),(7, 8, 4), (8, 9, 8)]
edges_with_weight = [(1, 2, 1), (1, 3, 3), (2, 3, 4), (2, 4, 6), (2, 5, 7), (3, 4, 5), (4, 5, 2)]

G = nx.Graph()
G1 = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges_with_weight)
G1 = G.copy()
edges_with_weight1 = edges_with_weight.copy()

layout = nx.spring_layout(G1)
nx.draw(G1, layout, with_labels=True, node_color='b')
labels = nx.get_edge_attributes(G1, "weight")
nx.draw_networkx_edge_labels(G1, pos=layout, edge_labels=labels)
plt.show()

Skeleton = nx.Graph()
edges_with_weight2 = []

for i in range(0, G1.number_of_nodes() - 1):
    if i == 0:
        min_edge = -1
        min_edge_weight = 100

        for n in range(0, G1.number_of_edges()):
            if min_edge_weight > edges_with_weight1[n][2]:
                min_edge = n
                min_edge_weight = edges_with_weight1[n][2]

        print("Edge with min weight: " + str(edges_with_weight1[min_edge]))
        edges_with_weight2.append(edges_with_weight1[min_edge])
        Skeleton.add_node(edges_with_weight1[min_edge][0])
        Skeleton.add_node(edges_with_weight1[min_edge][1])
        print("Add nodes: " + str(edges_with_weight1[min_edge][0]) + " , " + str(edges_with_weight1[min_edge][1]))
        G1.remove_edge(edges_with_weight1[min_edge][0], edges_with_weight1[min_edge][1])
        edges_with_weight1.remove(edges_with_weight2[0])

    else:
        min_edge = -1
        min_edge_weight = 100
        flag1 = False
        flag2 = False

        for t in range(0, G1.number_of_edges()):
            flag1 = Skeleton.has_node(edges_with_weight1[t][0])
            flag2 = Skeleton.has_node(edges_with_weight1[t][1])
            if ((flag1 == True and flag2 == False) or (flag1 == False and flag2 == True) or (
                    flag1 == False and flag2 == False)):
                if min_edge_weight > edges_with_weight1[t][2]:
                    min_edge = t
                    min_edge_weight = edges_with_weight1[t][2]

        print("Edge with min weight: " + str(edges_with_weight1[min_edge]))
        edges_with_weight2.append(edges_with_weight1[min_edge])

        flag3 = Skeleton.has_node(edges_with_weight1[min_edge][0])
        flag4 = Skeleton.has_node(edges_with_weight1[min_edge][1])
        if (flag3 == False) and (flag4 == False):
            Skeleton.add_node(edges_with_weight1[min_edge][0])
            Skeleton.add_node(edges_with_weight1[min_edge][1])
            print("Add nodes: " + str(edges_with_weight1[min_edge][0]) + " , " + str(edges_with_weight1[min_edge][1]))

        elif (flag3 == True) and (flag4 == True):
            print("Dont't add node")

        elif flag3 == True:
            Skeleton.add_node(edges_with_weight1[min_edge][1])
            print('Add node ' + str(edges_with_weight1[min_edge][1]))

        elif flag4 == True:
            Skeleton.add_node(edges_with_weight1[min_edge][0])
            print('Add node ' + str(edges_with_weight1[min_edge][0]))

        G1.remove_edge(edges_with_weight1[min_edge][0], edges_with_weight1[min_edge][1])
        edges_with_weight1.remove(edges_with_weight2[len(edges_with_weight2) - 1])

    Skeleton.add_weighted_edges_from(edges_with_weight2)
    layout1 = nx.spring_layout(Skeleton)
    nx.draw(Skeleton, layout1, with_labels=True, node_color='b')
    labels1 = nx.get_edge_attributes(Skeleton, "weight")
    nx.draw_networkx_edge_labels(Skeleton, pos=layout1, edge_labels=labels1)
    plt.show()
    Skeleton.remove_edges_from(edges_with_weight2)

print(edges_with_weight2)
print(Skeleton.nodes)

Skeleton.add_weighted_edges_from(edges_with_weight2)

sumweight = 0
for x in range(0, len(edges_with_weight2)):
    sumweight += edges_with_weight2[x][2]
print("Skeleton min weight sum: " + str(sumweight))

layout2 = nx.spring_layout(Skeleton)
nx.draw(Skeleton, layout2, with_labels=True, node_color='b')
labels2 = nx.get_edge_attributes(Skeleton, "weight")
nx.draw_networkx_edge_labels(Skeleton, pos=layout2, edge_labels=labels2)
plt.show()
