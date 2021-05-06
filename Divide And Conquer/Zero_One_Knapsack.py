class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit


def ZeroOneKnapsack(items, capacity, currentIndex=0):
    if capacity <= 0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + ZeroOneKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = ZeroOneKnapsack(items, capacity, currentIndex+1)
        return max(profit1, profit2)
    else:
        return 0


apple = Item(1, 26)
mango = Item(3, 31)
orange = Item(2, 17)
banana = Item(5, 72)
items = [mango, apple, orange, banana]

print(ZeroOneKnapsack(items, 7))
