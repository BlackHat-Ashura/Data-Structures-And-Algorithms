from Singly_Linked_List import SinglyLL, Node


def remDup1(LL):
    """
    T - O(N)
    S - O(N)
    """
    if LL.head is None:
        print("[!] LL doesnt exist")
    else:
        tempNode = LL.head
        visited = [tempNode.value]
        while tempNode.next:
            if tempNode.next.value in visited:
                tempNode.next = tempNode.next.next
            else:
                visited.append(tempNode.next.value)
                tempNode = tempNode.next
        return f"[+] New LL = {LL.show()}"

# SLL = SinglyLL()
# SLL.insertNode(1)
# SLL.insertNode(1, 0)
# SLL.insertNode(2, 1)
# SLL.insertNode(3, 2)
# SLL.insertNode(4, 0)
# SLL.insertNode(5, 0)
# SLL.insertNode(6, 3)
# SLL.insertNode(7, 0)
# SLL.insertNode(8, 5)
# SLL.show()
# remDup1(SLL)
# SLL.show()

def remDup2(LL):
    """
    T - O(N^2)
    S - O(1)
    """
    if LL.head is None:
        print("[!] LL doesnt exist")
    else:
        tempNode = LL.head
        while tempNode:
            currentNode = tempNode
            while currentNode.next:
                if currentNode.next.value == tempNode.value:
                    currentNode.next = currentNode.next.next
                else:
                    currentNode = currentNode.next
            tempNode = tempNode.next
        return f"[+] New LL = {LL.show()}"

# SLL = SinglyLL()
# SLL.insertNode(1)
# SLL.insertNode(1, 0)
# SLL.insertNode(2, 1)
# SLL.insertNode(3, 2)
# SLL.insertNode(4, 0)
# SLL.insertNode(5, 0)
# SLL.insertNode(6, 3)
# SLL.insertNode(7, 0)
# SLL.insertNode(8, 5)
# SLL.show()
# remDup2(SLL)
# SLL.show()

def nthToLast(LL, n):
    pointer1 = LL.head
    pointer2 = LL.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return f"[+] {n} value from last is {pointer1.value}."

# SLL = SinglyLL()
# SLL.insertNode(1)
# SLL.insertNode(1, 0)
# SLL.insertNode(2, 1)
# SLL.insertNode(3, 2)
# SLL.insertNode(4, 0)
# SLL.insertNode(5, 0)
# SLL.insertNode(6, 3)
# SLL.insertNode(7, 0)
# SLL.insertNode(8, 5)
# SLL.show()
# print(nthToLast(SLL))


def partition(LL, x):
    currentNode = LL.head
    LL.tail = LL.head
    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value < x:
            currentNode.next = LL.head
            """
            For the first node, firstNode.next is assigned to itself.
            firstNode.next = firstNode
            """
            LL.head = currentNode
        else:
            LL.tail.next = currentNode
            LL.tail = currentNode
        currentNode = nextNode

    """
    If x > all values in LL, then no value gets added at the end.
    Then the firstNode becomes the tailNode and points to itself.
    tail.next != None
    Then this is no longer a Singly Linked List, so program cannot exit.
    """
    LL.tail.next = None

# SLL = SinglyLL()
# SLL.insertNode(1)
# SLL.insertNode(1, 0)
# SLL.insertNode(2, 1)
# SLL.insertNode(3, 2)
# SLL.insertNode(4, 0)
# SLL.insertNode(5, 0)
# SLL.insertNode(6, 3)
# SLL.insertNode(7, 0)
# SLL.insertNode(8, 5)
# SLL.show()
# partition(SLL, 5)
# SLL.show()


def sumLL(LL1, LL2):
    n1 = LL1.head
    n2 = LL2.head
    result = 0
    LL = SinglyLL()
    while n1 or n2:
        result = result//10
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        LL.insertNode(result%10, 1)
    return LL

# SLL1 = SinglyLL()
# SLL1.insertNode(7, 1)
# SLL1.insertNode(1, 1)
# SLL1.insertNode(6, 1)
# SLL2 = SinglyLL()
# SLL2.insertNode(5, 1)
# SLL2.insertNode(9, 1)
# SLL2.insertNode(2, 1)
# SLL1.show()
# SLL2.show()
# sumLL(SLL1, SLL2).show()


def addSameNode(LL1, LL2, value):
    tempNode = Node(value=value)
    LL1.tail.next = tempNode
    LL1.tail = tempNode
    LL2.tail.next = tempNode
    LL2.tail = tempNode

def intersection(LL1, LL2):
    if LL1.tail is not LL2.tail:
        return False
    len1 = len(LL1)
    len2 = len(LL2)
    shorter = LL1 if len1 < len2 else LL2
    longer = LL2 if len1 < len2 else LL1
    diff = len(longer) - len(shorter)
    shorterLL = shorter.head
    longerLL = longer.head
    for i in range(diff):
        longerLL = longerLL.next
    while shorterLL is not longerLL:
        shorterLL = shorterLL.next
        longerLL = longerLL.next
    return shorterLL.value

# SLL1 = SinglyLL()
# SLL1.insertNode(7, 1)
# SLL1.insertNode(1, 1)
# SLL1.insertNode(90, 1)
# SLL2 = SinglyLL()
# SLL2.insertNode(5, 1)
# SLL2.insertNode(9, 1)
# SLL2.insertNode(90, 1)
# SLL1.show()
# SLL2.show()
# addSameNode(SLL1, SLL2, 100)
# addSameNode(SLL1, SLL2, 150)
# addSameNode(SLL1, SLL2, 200)
# SLL1.show()
# SLL2.show()
# print(intersection(SLL1, SLL2))
