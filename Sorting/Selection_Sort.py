def SelectionSort(ar):
    length = len(ar)
    for i in range(length-1):
        '''
        length - 1 considers till last but one index.
        This is because when we reach the last element, the array is already sorted.
        '''
        min = i
        for j in range(i+1, length):
            '''
            "j" starts from "i+1" as unsorted elements begin from "i".
            '''
            if ar[min] > ar[j]:
                min = j
        ar[i], ar[min] = ar[min], ar[i]


ar = [3, 2, 1, 4, 5, 9, 8, 7, 6]
SelectionSort(ar)
print(ar)
