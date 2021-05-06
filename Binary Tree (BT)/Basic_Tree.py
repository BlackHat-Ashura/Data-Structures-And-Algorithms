class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        tree = " " * level + str(self.data) + "\n"
        for child in self.children:
            tree += child.__str__(level + 1)
        return tree

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


menu = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
menu.addChild(cold)
menu.addChild(hot)
cola = TreeNode("Cola", [])
pepsi = TreeNode("Pepsi", [])
fanta = TreeNode("Fanta", [])
cold.addChild(cola)
cold.addChild(pepsi)
cold.addChild(fanta)
coffee = TreeNode("Coffee", [])
tea = TreeNode("Tea", [])
hot.addChild(coffee)
hot.addChild(tea)
print(menu)
