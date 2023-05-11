def bubble(arr):
   n = len(arr)
   for i in range(n):
       for j in range(0, n-i-1):
           if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
   return arr

def find_pivot_index(A: list, start: int, end: int) -> int:
    """
    Selects the last element as the pivot element and partitions the input array into two
    subarrays: one containing elements less than the pivot element, and another containing
    elements greater than the pivot element.

    Args:
    - A (list): The input array to be sorted.
    - start (int): The starting index of the subarray to be sorted.
    - end (int): The ending index of the subarray to be sorted.

    Returns:
    - p_index (int): The index of the pivot element in the sorted array.
    """
    pivot = A[end]
    p_index = start
    for iter in range(start, end):
        if A[iter] <= pivot:
            A[p_index], A[iter] = A[iter], A[p_index]
            p_index += 1
    A[p_index], A[end] = pivot, A[p_index]
    return p_index


def quicksort(A,start,end):
    if start < end:
        pivot_index=find_pivot_index(A,start,end)
        print("--------------",A)
        quicksort(A,start,pivot_index-1)
        quicksort(A,pivot_index+1,end)