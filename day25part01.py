from sys import stdin
from networkx import Graph, minimum_edge_cut, connected_components
lines = []
with open('input/25.txt') as myFile:
    for line in myFile:
        lines.append(line)
graph = Graph()
for line in lines:
    left, right = line.rstrip().split(":")
    for x in right.strip().split():
        graph.add_edge(left, x)
graph.remove_edges_from(minimum_edge_cut(graph))
group1, group2 = connected_components(graph)
print(len(group1)*len(group2))
