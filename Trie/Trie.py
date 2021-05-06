class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, string):
        current = self.root
        for char in string:
            node = current.children.get(char)
            if node is None:
                node = TrieNode()
                current.children.update({char: node})
            current = node
        current.endOfString = True
        print(f"Successfully inserted {string} in Trie.\n")

    def searchString(self, string):
        current = self.root
        isPresent = True
        for char in string:
            node = current.children.get(char)
            if node is None:
                isPresent = False
                break
            current = node
        if current.endOfString == True and isPresent == True:
            print(f"[+] {string} exists in Trie.\n")
        else:
            print(f"[-] {string} doesn't exist in Trie.\n")

    def delString(self, string, root=None, index=0):
        if index == 0:
            root = self.root
        char = string[index]
        node = root.children.get(char)

        if node is None:
            return False
        else:
            if index == len(string) - 1:
                if len(node.children) >= 1:
                    node.endOfString = False
                    return False
                else:
                    root.children.pop(char)
                    return True

            delete = self.delString(string, node, index + 1)

        if delete == True:
            if len(node.children) >= 1:
                return False
            else:
                if node.endOfString == True:
                    return False
                root.children.pop(char)
                return True
        else:
            return False


# tr = Trie()
# tr.insertString("Api")
# tr.insertString("Apple")
# tr.insertString("App")
# tr.delString("Boi")
# tr.searchString("Apple")
# tr.searchString("App")
# tr.searchString("Api")
# tr.searchString("Apples")
