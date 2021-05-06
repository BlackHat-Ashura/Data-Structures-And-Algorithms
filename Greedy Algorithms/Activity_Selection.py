def ActivitySelection(A):
    A.sort(key=lambda x: x[2])
    firstA = A[0][0]
    print(firstA)
    previous = 0
    for current in range(len(A)):
        if A[current][1] >= A[previous][2]:
            print(A[current][0])
            previous = current


A = [["A1", 0, 6],
     ["A2", 3, 4],
     ["A3", 1, 2],
     ["A4", 5, 8],
     ["A5", 5, 7],
     ["A6", 8, 9]]

ActivitySelection(A)
