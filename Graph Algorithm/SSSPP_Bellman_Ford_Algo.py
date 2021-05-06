class Graph:
    def __init__(self):
        self.graph = []
        self.nodes = []

    def addNode(self, value):
        self.nodes.append(value)

    def addEdge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def print_solution(self, dist, src):
        print(f"[+] Vertex Distances from Source {src}")
        for key, value in dist.items():
            print(" ", key, " : ", value)

    def BellmanFord(self, input_source):
        Distances = {i: float("inf") for i in self.nodes}
        Distances[input_source] = 0
        noOfVertices = len(self.nodes)

        for _ in range(noOfVertices - 1):
            for source, destination, weight in self.graph:
                if Distances[source] != float("inf") and Distances[source] + weight < Distances[destination]:
                    Distances[destination] = Distances[source] + weight

        for source, destination, weight in self.graph:
            if Distances[source] != float("inf") and Distances[source] + weight < Distances[destination]:
                print("[-] Graph contains negative cycle.\n")
                return

        self.print_solution(Distances, input_source)


graph = Graph()
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addNode("E")

graph.addEdge("A", "C", 6)
graph.addEdge("A", "D", 6)
graph.addEdge("B", "A", 3)
graph.addEdge("C", "D", 1)
graph.addEdge("D", "C", 2)
graph.addEdge("D", "B", 1)
graph.addEdge("E", "B", 4)
graph.addEdge("E", "D", 2)

graph.BellmanFord("E")
