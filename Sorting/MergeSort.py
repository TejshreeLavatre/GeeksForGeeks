# time complexity is O(n log n)

# import sys
#
#
# def mergeSort(A):
#     mergeSort2(A, 0, len(A)-1)
#
#
# def mergeSort2(A, first, last):
#         if first < last:
#             middle = (first+last) // 2
#             mergeSort2(A, first, middle)
#             mergeSort2(A, middle+1, last)
#             merge(A, first, middle, last)
#
#
# def merge(A, first, middle, last):
#     L = A[first:middle+1]
#     R = A[middle+1:last+1]
#     L.append(sys.maxsize)
#     R.append(sys.maxsize)
#     i = j = 0
#
#     for k in range(first, last+1):
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i += 1
#         else:
#             A[k] = R[j]
#             j += 1

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


arr = [3, 5, 6, 2, 1, 4, 9, 8, 7]
print(mergesort(arr))
