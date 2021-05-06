class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def FractionalKnapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        else:
            unusedCapacity = capacity - usedCapacity
            value = i.ratio * unusedCapacity
            usedCapacity += unusedCapacity
            totalValue += value

        if usedCapacity == capacity:
            break

    print(f"[+] Total value = {totalValue}.")


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
items = [item1, item2, item3]

FractionalKnapsack(items, 50)
