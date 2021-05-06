def HouseRobberTopDown(houses, currentHouse=0, memo={}):
    if currentHouse >= len(houses):
        return 0
    if currentHouse not in memo:
        stealHouse = houses[currentHouse] + HouseRobberTopDown(houses, currentHouse+2, memo)
        skipHouse = HouseRobberTopDown(houses, currentHouse+1, memo)
        memo[currentHouse] = max(stealHouse, skipHouse)
    return memo[currentHouse]


def HouseRobberBottomUp(houses):
    table = [0] * (len(houses) + 2)
    for i in range(len(houses)-1, -1, -1):
        table[i] = max(houses[i] + table[i+2], table[i+1])
    return table[0]


houses = [6, 7, 1, 30, 8, 2, 4]
print(HouseRobberTopDown(houses))
print(HouseRobberBottomUp(houses))
