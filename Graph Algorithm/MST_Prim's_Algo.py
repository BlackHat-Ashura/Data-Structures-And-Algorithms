class Graph:
    def __init__(self, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.MST = []

    def print_solution(self):
        print("[+] Edge : Weight")
        for source, destination, weight in self.MST:
            print(f"    {source} -> {destination} : {weight}")
        print("")

    def Prim(self):
        noOfVertices = len(self.nodes)
        visited = [0] * noOfVertices
        edgeNum = 0
        visited[0] = True
        source = 0
        destination = 0

        while edgeNum < noOfVertices - 1:
            min = float("inf")
            for i in range(noOfVertices):
                if visited[i]:
                    for j in range(noOfVertices):
                        if not visited[j] and self.edges[i][j]:
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                source = i
                                destination = j
            self.MST.append([self.nodes[source], self.nodes[destination], self.edges[source][destination]])
            visited[destination] = True
            edgeNum += 1

        self.print_solution()


edges = [[0, 10, 20, 0, 0],
         [10, 0, 30, 5, 0],
         [20, 30, 0, 15, 6],
         [0, 5, 15, 0, 8],
         [0, 0, 6, 8, 0]]
nodes = ["A", "B", "C", "D", "E"]

g = Graph(edges, nodes)
g.Prim()
