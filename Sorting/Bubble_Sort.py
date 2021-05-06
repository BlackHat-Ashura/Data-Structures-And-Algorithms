def BubbleSort(ar):
    length = len(ar)
    for i in range(length-1):
        '''
        length - 1 considers till last but one index.
        This is because last but one element is compared with its next element.
        If we go till last element, then the next element will be out of bounds.
        '''
        sorted = True
        for j in range(length-1 - i):
            '''
            length - 1 --> To go to last but one index,
            "-i" is because for each sorting action the last element is not considered as it is already sorted.
            '''
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
                sorted = False
        if sorted == True:
            break


ar = [3, 2, 1, 4, 5, 9, 8, 7, 6]
BubbleSort(ar)
print(ar)
