def LinearSearch(ar, value):
    length = len(ar)
    for i in range(length):
        if ar[i] == value:
            return f"[+] {value} is at index {i}.\n"
    return f"[-] {value} Not found.\n"


ar = [3, 2, 1, 4, 5, 9, 8, 7, 6]
print(LinearSearch(ar, 8))
