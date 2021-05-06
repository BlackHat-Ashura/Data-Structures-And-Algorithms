def print_solution(noOfVertices, distances):
    for i in range(noOfVertices):
        for j in range(noOfVertices):
            if distances[i][j] == inf:
                print("inf", end=" ")
            else:
                print(distances[i][j], end=" ")
        print("")


def FloydWarshall(Graph):
    noOfVertices = len(Graph)
    distances = [[Graph[i][j] for j in range(noOfVertices)] for i in range(noOfVertices)]
    for k in range(noOfVertices):
        for i in range(noOfVertices):
            for j in range(noOfVertices):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    print_solution(noOfVertices, distances)


inf = 9999
G = [[0, 8, inf, 1, inf],
     [inf, 0, 1, inf, 2],
     [4, inf, 0, inf, inf],
     [inf, 2, 9, 0, inf],
     [inf, inf, 3, inf, 0]]

FloydWarshall(G)
