def WaysToReachLastCell(path, cost, row=0, column=0):
    if cost < 0:
        return 0
    elif row == len(path)-1 and column == len(path[0])-1:
        if path[row][column] - cost == 0:
            return 1
        else:
            return 0
    elif row == len(path)-1:
        return WaysToReachLastCell(path, cost - path[row][column], row, column+1)
    elif column == len(path[0])-1:
        return WaysToReachLastCell(path, cost - path[row][column], row+1, column)
    else:
        route1 = WaysToReachLastCell(path, cost - path[row][column], row+1, column)
        route2 = WaysToReachLastCell(path, cost - path[row][column], row, column+1)
        return route1 + route2


path = [[4, 7, 1, 6],
        [5, 7, 3, 9],
        [3, 2, 1, 2],
        [7, 1, 6, 3]]

print(WaysToReachLastCell(path, 30))
