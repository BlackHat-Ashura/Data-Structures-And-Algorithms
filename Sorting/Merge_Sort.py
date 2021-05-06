def merge(ar, l_index, m_index, r_index):
    n1 = m_index - l_index + 1
    n2 = r_index - m_index

    Left = [0] * n1
    Right = [0] * n2

    for i in range(n1):
        Left[i] = ar[l_index + i]

    for j in range(n2):
        Right[j] = ar[m_index + 1 + j]

    i = 0
    j = 0
    k = l_index

    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            ar[k] = Left[i]
            i += 1
        else:
            ar[k] = Right[j]
            j += 1
        k += 1

    while i < n1:
        ar[k] = Left[i]
        i += 1
        k += 1

    while j < n2:
        ar[k] = Right[j]
        j += 1
        k += 1


def MergeSort(ar, l_index, r_index):
    if l_index < r_index:
        m_index = (l_index + r_index)//2
        MergeSort(ar, l_index, m_index)
        MergeSort(ar, m_index + 1, r_index)
        merge(ar, l_index, m_index, r_index)


ar = [3, 2, 1, 4, 5, 9, 8, 7, 6]
MergeSort(ar, 0, 8)
print(ar)
