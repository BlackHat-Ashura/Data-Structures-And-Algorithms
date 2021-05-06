"""
Given a directed graph and two nodes,
design an algorithm to find out whether there is a route from Start to End.
"""


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    '''
    # This returns Shortest Path
    
    def checkRoute(self, startNode, endNode):
        visited = [startNode]
        queue = [[startNode]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == endNode:
                return path
            for adjacent in self.gdict[node]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)
        return False
    '''

    def checkRoute(self, startNode, endNode):
        visited = [startNode]
        queue = [startNode]
        while queue:
            node = queue.pop(0)
            if node == endNode:
                return True
            for adjacent in self.gdict[node]:
                if adjacent not in visited:
                    visited.append(adjacent)
                    queue.append(adjacent)
        return False
