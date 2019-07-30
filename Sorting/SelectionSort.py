# time complexity is O(n^2)


def selectionSort(A):
    for i in range(len(A)-1):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]
    return print(A)


selectionSort([4, 5, 6, 1, 2, 7, 8, 3])