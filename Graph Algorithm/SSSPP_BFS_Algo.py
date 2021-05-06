class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def BFS(self, start, end):
        visited = [start]
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict[node]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)


dict_ = {
    "a": ["b", "c"],
    "b": ["g", "a", "d"],
    "c": ["a", "d", "e"],
    "d": ["b", "c", "f"],
    "e": ["c", "f"],
    "f": ["d", "e", "g"],
    "g": ["b", "f"]
}

graph = Graph(dict_)
print(graph.BFS("g", "e"))
print(graph.BFS("a", "f"))
