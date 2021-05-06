class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def BFS(self, vertex):
        visited = [vertex]
        queue = [vertex]
        print("[+] BFS = ", end="")
        while queue:
            deVertex = queue.pop(0)
            print(deVertex, end=" ")
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
        print("\n")

    def DFS(self, vertex):
        visited = [vertex]
        stack = [vertex]
        print("[+] DFS = ", end="")
        while stack:
            popVertex = stack.pop()
            print(popVertex, end=" ")
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)
        print("\n")


dict_ = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"]
}

graph = Graph(dict_)
graph.BFS("a")
graph.DFS("a")
