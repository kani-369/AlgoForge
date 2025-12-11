"""
Complete Sorting Algorithms Module for AlgoForge.
Includes:
- Merge Sort
- Quick Sort
- Heap Sort
- Insertion Sort
- Selection Sort
- Bubble Sort
"""

from typing import List


# -----------------------------------------------------
# MERGE SORT
# -----------------------------------------------------
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -----------------------------------------------------
# QUICK SORT
# -----------------------------------------------------
def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


# -----------------------------------------------------
# HEAP SORT
# -----------------------------------------------------
def heap_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)

    return arr

def _heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


# -----------------------------------------------------
# INSERTION SORT
# -----------------------------------------------------
def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr


# -----------------------------------------------------
# SELECTION SORT
# -----------------------------------------------------
def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


# -----------------------------------------------------
# BUBBLE SORT
# -----------------------------------------------------
def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


# -----------------------------------------------------
# PROVIDE ALL SORTING ALGORITHMS TO BENCHMARK ENGINE
# -----------------------------------------------------
def get_sorting_algorithms():
    return {
        "merge_sort": merge_sort,
        "quick_sort": quick_sort,
        "heap_sort": heap_sort,
        "insertion_sort": insertion_sort,
        "selection_sort": selection_sort,
        "bubble_sort": bubble_sort,
    }