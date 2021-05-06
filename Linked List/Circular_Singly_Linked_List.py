class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLL:
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
        if self.head == None:
            print("[!] Linked List doesnt exist.\n")
        else:
            print([node for node in self], "\n")

    def insertNode(self, value, location):
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
            newNode.next = newNode
            print(f"[+] Linked List created successfully with a single node holding a value = {newNode.value} !\n")
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
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
                if tempNode.next == self.head:
                    break
                tempNode = tempNode.next
            if tempNode.next == self.head:
                print(f"[-] {nodeValue} doesnt exist in Linked List.\n")

    def remove(self, location=None):
        """
        This method Removes value from a specified location.
        Location 0 for start of Linked List.
        Location 1 for end of Linked List.
        Rest are Location 2, 3, 4,... for subsequent positions of Linked List.
        """
        if self.head is None:
            print("[!] Linked List doesnt exist.\n")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            if location == 1:
                if self.head == self.tail:
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode.next != self.tail:
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
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
            self.tail.next = None
            self.tail = None
            print("[+] Successfully deleted Linked List!\n")


# CSLL = CircularSinglyLL()
#
# CSLL.insertNode(1, 0)
# CSLL.insertNode(6, 1)
# CSLL.insertNode(6, 1)
# CSLL.insertNode(6, 2)
# CSLL.insertNode(4, 100)
# CSLL.insertNode(5, 3)
# CSLL.search(2)
# CSLL.show()
# CSLL.remove(8)
# CSLL.show()
