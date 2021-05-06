def InsertionSort(ar):
    length = len(ar)
    for i in range(1, length):
        '''
        "first" is assigned the second element as the first element is already taken as sorted.
        '''
        first = ar[i]
        j = i-1
        '''
        "j" moves from last element of sorted values to first element of sorted values.
        
        Example:
        ar = [3, 2, 1, 4, 5, 9, 8, 7, 6]
        
        first = 2
        2 < 3 --> ar = [3, 3, 1, 4, 5, 9, 8, 7, 6] --> ar = [2, 3, 1, 4, 5, 9, 8, 7, 6]
        
        first = 1
        1 < 3 --> ar = [2, 3, 3, 4, 5, 9, 8, 7, 6]
        1 < 2 --> ar = [2, 2, 3, 4, 5, 9, 8, 7, 6] --> ar = [1, 2, 3, 4, 5, 9, 8, 7, 6]
        
        so on...
        
        '''
        while j >= 0 and first < ar[j]:
            ar[j+1] = ar[j]
            j -= 1
        ar[j+1] = first


ar = [3, 2, 1, 4, 5, 9, 8, 7, 6]
InsertionSort(ar)
print(ar)
