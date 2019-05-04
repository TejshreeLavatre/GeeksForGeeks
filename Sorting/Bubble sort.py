
def bubbleSort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return print(A)


bubbleSort(['b', 'c', 'a', 'f', 'e', 'd'])


# def optimizedBubble(arr, i, n):
#     for i in range(n):
#         swapped = False
#         for j in range(n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if swapped == False:   # if no two elements were swapped by inner loop, then break.
#             break              # It is the case when the array is already sorted)
#     return print(arr)

