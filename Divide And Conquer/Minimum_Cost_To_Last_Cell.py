def MinCostToLastCell(path, row=0, column=0):
    if row >= len(path) or column >= len(path[0]):
        return float("inf")
    if row == len(path)-1 and column == len(path[0])-1:
        return path[row][column]
    else:
        goDown = path[row][column] + MinCostToLastCell(path, row+1, column)
        goRight = path[row][column] + MinCostToLastCell(path, row, column+1)
        return min(goDown, goRight)


path = [[4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]]

print(MinCostToLastCell(path))


# def MaxCostToLastCell(path, row=0, column=0):
#     if row >= len(path) or column >= len(path[0]):
#         return 0
#     if row == len(path)-1 and column == len(path[0])-1:
#         return path[row][column]
#     else:
#         goDown = path[row][column] + MaxCostToLastCell(path, row+1, column)
#         goRight = path[row][column] + MaxCostToLastCell(path, row, column+1)
#         return max(goDown, goRight)
#
#
# path = [[4, 7, 8, 6, 4],
#         [6, 7, 3, 9, 2],
#         [3, 8, 1, 2, 4],
#         [7, 1, 7, 3, 7],
#         [2, 9, 8, 9, 3]]
#
# print(MaxCostToLastCell(path))
