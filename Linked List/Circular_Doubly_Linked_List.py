class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLL:
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
            if tempNode.next == self.head:
                break
            tempNode = tempNode.next

    def show(self):
        """
        This method Prints elements of Linked List.
        """
        if self.head is None:
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
            newNode.prev = newNode
            newNode.next = newNode
            print(f"[+] Linked List created successfully with a single node holding a value = {value} !\n")
        else:
            if location == 0:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                self.head.prev = newNode
            else:
                tempNode = self.head
                index = 1
                while index < location - 1:
                    if tempNode.next == self.head:
                        break
                    tempNode = tempNode.next
                    index += 1
                if tempNode.next != self.head:
                    nextNode = tempNode.next
                    tempNode.next = newNode
                    newNode.prev = tempNode
                    newNode.next = nextNode
                    nextNode.prev = newNode
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
            forwardNode = self.head
            backwardNode = self.tail
            while forwardNode and backwardNode:
                if forwardNode.value == nodeValue:
                    print(f"[+] {nodeValue} exists in Linked List.\n")
                    break
                if backwardNode.value == nodeValue:
                    print(f"[+] {nodeValue} exists in Linked List.\n")
                    break
                if forwardNode.next == backwardNode:
                    """For even length."""
                    print(f"[-] {nodeValue} doesnt exist in Linked List.\n")
                    break
                if forwardNode.next == backwardNode.prev:
                    """For odd length."""
                    print(f"[-] {nodeValue} doesnt exist in Linked List.\n")
                    break
                forwardNode = forwardNode.next
                backwardNode = backwardNode.prev

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
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            if location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 1
                while index < location - 1:
                    if tempNode.next == self.head:
                        break
                    tempNode = tempNode.next
                    index +=1
                if tempNode.next != self.head:
                    nextNode = tempNode.next
                    tempNode.next = nextNode.next
                    if tempNode.next == self.head:
                        self.tail = tempNode
                        self.head.prev = self.tail
                    else:
                        tempNode.next.prev = tempNode
                else:
                    print(f"[!] Location {location} exceeds nodes in linked list.\n")

    def deleteLL(self):
        """
        This method Deletes the Linked List.
        """
        if self.head is None:
            print("[!] Linked List doesnt exist.\n")
        else:
            delNode = self.head
            self.tail.next = None
            while delNode:
                delNode.prev = None
                delNode = delNode.next
            self.head = None
            self.tail = None
            print("[+] Successfully deleted Linked List!\n")


# CDLL = CircularDoublyLL()
#
# CDLL.insertNode(1, 0)
# CDLL.insertNode(6, 1)
# CDLL.insertNode(2, 2)
# CDLL.insertNode(3, 3)
# CDLL.insertNode(4, 40)
# CDLL.insertNode(5, 4)
#
# CDLL.show()
# CDLL.deleteLL()
# CDLL.show()
