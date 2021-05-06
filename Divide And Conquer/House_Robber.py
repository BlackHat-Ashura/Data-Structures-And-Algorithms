def HouseRobber(houses, currentHouse=0):
    if currentHouse >= len(houses):
        return 0
    else:
        stealHouse = houses[currentHouse] + HouseRobber(houses, currentHouse + 2)
        skipHouse = HouseRobber(houses, currentHouse + 1)
        return max(stealHouse, skipHouse)


houses = [6, 7, 1, 1, 30, 8, 2, 4]
print(HouseRobber(houses))
