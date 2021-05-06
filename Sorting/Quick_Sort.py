def partition(ar, low, high):
    pointer = low - 1
    pivot = ar[high]
    for j in range(low, high):
        if ar[j] <= pivot:
            pointer += 1
            ar[pointer], ar[j] = ar[j], ar[pointer]
    ar[pointer+1], ar[high] = ar[high], ar[pointer+1]
    return pointer + 1


def QuickSort(ar, low, high):
    if low < high:
        partition_index = partition(ar, low, high)
        QuickSort(ar, low, partition_index-1)
        QuickSort(ar, partition_index+1, high)


ar = [3, 2, 1, 4, 5, 9, 8, 7, 6]
QuickSort(ar, 0, 8)
print(ar)
