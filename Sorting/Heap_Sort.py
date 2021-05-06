def HeapifyTree(ar, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and ar[left] < ar[smallest]:
        smallest = left

    if right < n and ar[right] < ar[smallest]:
        smallest = right

    if smallest != i:
        ar[i], ar[smallest] = ar[smallest], ar[i]
        HeapifyTree(ar, n, smallest)


def HeapSort(ar):
    n = len(ar)
    for i in range(int(n/2) - 1, -1, -1):
        HeapifyTree(ar, n, i)

    for i in range(n-1, 0, -1):
        ar[i], ar[0] = ar[0], ar[i]
        HeapifyTree(ar, i, 0)

    ar.reverse()


ar = [3, 2, 1, 4, 5, 9, 8, 7, 6]
HeapSort(ar)
print(ar)
