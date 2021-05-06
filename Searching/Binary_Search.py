def BinarySearch(ar, value):
    length = len(ar)
    start = 0
    end = length - 1
    middle = (start + end) // 2

    while not (ar[middle] == value):
        if value < ar[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end) // 2
        if start > length - 1:
            return f"[-] {value} Not found.\n"

    return f"[+] {value} is at index {middle}"


ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(BinarySearch(ar, 7))
