import math


def InsertionSort(ar):
    length = len(ar)
    for i in range(1, length):
        first = ar[i]
        j = i - 1
        while j >= 0 and first < ar[j]:
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = first


def BucketSort(ar):
    length = len(ar)
    buckets = round(math.sqrt(length))
    maxValue = max(ar)
    arr = []
    for i in range(buckets):
        arr.append([])

    for element in ar:
        index = math.ceil(element * buckets / maxValue)
        arr[index - 1].append(element)

    for i in range(buckets):
        InsertionSort(arr[i])

    k = 0
    for i in range(buckets):
        for j in range(len(arr[i])):
            ar[k] = arr[i][j]
            k += 1


ar = [3, 2, 1, 4, 5, 9, 8, 7, 6]
BucketSort(ar)
print(ar)
