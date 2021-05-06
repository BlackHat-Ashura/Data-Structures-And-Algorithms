from collections import defaultdict


class Graph:
    def __init__(self, numberOfVertices):
        self.gdict = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def topologicalSortUtil(self, vertex, visited, stack):
        visited.append(vertex)

        for i in self.gdict[vertex]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, vertex)

    def TopologicalSort(self):
        visited = []
        stack = []

        for k in list(self.gdict):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        print(stack)


graph = Graph(8)
graph.addEdge("A", "C")
graph.addEdge("B", "C")
graph.addEdge("B", "D")
graph.addEdge("C", "E")
graph.addEdge("E", "H")
graph.addEdge("E", "F")
graph.addEdge("D", "F")
graph.addEdge("F", "G")
graph.TopologicalSort()

r'''
           A   B
            \ / \ 
             C   D
            /   / 
           E   / 
          / \ /
         H   F---G
'''
