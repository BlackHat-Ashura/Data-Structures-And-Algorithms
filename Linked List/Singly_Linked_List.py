class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        This method Iterates through the Linked List and returns values to show().
        """
        tempNode = self.head
        while tempNode:
            yield tempNode.value
            tempNode = tempNode.next

    def show(self):
        """
        This method Prints elements of Linked List.
        """
        if self.head == None:
            print("[!] Linked List doesnt exist.\n")
        else:
            print([node for node in self], "\n")

    def insertNode(self, value, location=None):
        """
        This method Inserts a node with a specified value at the specified location in the Linked List.
        Location 0 for start of Linked List.
        Location 1 for end of Linked List.
        Rest are Location 2, 3, 4,... for subsequent positions of Linked List.
        """
        newNode = Node(value)
        if location == None:
            print("[!] No location mentioned.")
            print(f"[-] Failed to add {value}.\n")
        elif self.head is None:
            print("[!] Linked List doesnt exist so new one will be created.")
            self.head = newNode
            self.tail = newNode
            newNode.next = None
            print(f"[+] Linked List created successfully with a single node holding a value = {newNode.value} !\n")
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 1
                while index < location - 1:
                    if tempNode.next == None:
                        break
                    tempNode = tempNode.next
                    index += 1
                if tempNode.next != None:
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.next = nextNode
                else:
                    print(f"[!] Location {location} exceeds nodes in linked list.")
                    print(f"[-] Failed to insert {value} to linked list.\n")

    def search(self, nodeValue):
        """
        This method Searches for the specified node value.
        Location 0 for start of Linked List.
        Location 1 for end of Linked List.
        Rest are Location 2, 3, 4,... for subsequent positions of Linked List.
        """
        if self.head is None:
            print("[!] Linked List doesnt exist.\n")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    print(f"[+] {nodeValue} exists in Linked List.\n")
                    break
                tempNode = tempNode.next
            if not tempNode:
                print(f"[-] {nodeValue} doesnt exist in Linked List.\n")

    def remove(self, location=None):
        """
        This method Removes value from a specified location.
        Location 0 for start of Linked List.
        Location 1 for end of Linked List.
        Rest are Location 2, 3, 4,... for subsequent positions of Linked List.
        """
        if location == None:
            print("[-] No location mentioned!\n")
        elif self.head is None:
            print("[!] Linked List doesnt exist.\n")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            if location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode.next != self.tail:
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 1
                while index < location - 1:
                    if tempNode.next == None:
                        break
                    tempNode = tempNode.next
                    index +=1
                if tempNode.next != None:
                    nextNode = tempNode.next
                    tempNode.next = nextNode.next
                    if tempNode.next == None:
                        self.tail = tempNode
                else:
                    print(f"[!] Location {location} exceeds nodes in linked list.\n")

    def deleteLL(self):
        """
        This method Deletes the Linked List.
        """
        if self.head is None:
            print("[!] Linked List doesnt exist.\n")
        else:
            self.head = None
            self.tail = None
            print("[+] Successfully deleted Linked List!\n")

    def __len__(self):
        """
        This method returns length of Linked List.
        """
        tempNode = self.head
        i = 0
        while tempNode:
            i += 1
            tempNode = tempNode.next
        return i


# SLL = SinglyLL()
#
# SLL.insertNode(1, 0)
# SLL.insertNode(6, 1)
# SLL.insertNode(6, 1)
# SLL.insertNode(6, 2)
# SLL.insertNode(4, 100)
# SLL.insertNode(5, 3)
# SLL.search(2)
# SLL.show()
# SLL.remove(8)
# SLL.show()
