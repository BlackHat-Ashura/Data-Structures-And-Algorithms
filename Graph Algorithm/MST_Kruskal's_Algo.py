class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 1)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


class Graph:
    def __init__(self):
        self.graph = []
        self.nodes = []
        self.MST = []

    def addNode(self, value):
        self.nodes.append(value)

    def addEdge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def print_solution(self):
        print("[+] Edge : Weight")
        for source, destination, weight in self.MST:
            print(f"    {source} -> {destination} : {weight}")
        print("")

    def Kruskal(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        noOfVertices = len(self.nodes)

        while e < noOfVertices - 1:
            source, destination, weight = self.graph[i]
            i += 1
            x = ds.find(source)
            y = ds.find(destination)
            if x != y:
                e += 1
                self.MST.append([source, destination, weight])
                ds.union(x, y)
        self.print_solution()


graph = Graph()
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")

graph.addEdge("A", "B", 5)
graph.addEdge("A", "C", 13)
graph.addEdge("A", "E", 15)
graph.addEdge("B", "A", 5)
graph.addEdge("B", "C", 10)
graph.addEdge("B", "D", 8)
graph.addEdge("C", "A", 13)
graph.addEdge("C", "B", 10)
graph.addEdge("C", "D", 6)
graph.addEdge("C", "E", 20)
graph.addEdge("D", "B", 8)
graph.addEdge("D", "C", 6)
graph.addEdge("E", "A", 15)
graph.addEdge("E", "C", 20)

graph.Kruskal()
