"""
====================================================
🧩 AlgoForge Module: Divide and Conquer
====================================================
Implements classic divide-and-conquer algorithms:
- Merge Sort
- Quick Sort
- Binary Search
- Count Inversions
- Closest Pair of Points
- Strassen’s Matrix Multiplication

Divide & Conquer strategy:
Break → Solve → Combine → Efficient O(n log n) solutions.
====================================================
"""

import random
import math
from typing import List, Tuple


# -----------------------------------------------------------
# 🔹 MERGE SORT
# -----------------------------------------------------------

def merge_sort(arr: List[int]) -> List[int]:
    """Merge Sort (O(n log n))"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -----------------------------------------------------------
# 🔹 QUICK SORT
# -----------------------------------------------------------

def quick_sort(arr: List[int]) -> List[int]:
    """Quick Sort (O(n log n) avg, O(n²) worst)"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# -----------------------------------------------------------
# 🔹 BINARY SEARCH
# -----------------------------------------------------------

def binary_search(arr: List[int], target: int) -> int:
    """Binary Search (O(log n)) — works on sorted arrays"""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# -----------------------------------------------------------
# 🔹 COUNT INVERSIONS
# -----------------------------------------------------------

def count_inversions(arr: List[int]) -> int:
    """Counts number of inversions in the array."""

    def merge_and_count(left, right):
        i = j = 0
        merged = []
        inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv_count += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    if len(arr) <= 1:
        return 0

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_inv = count_inversions(left)
    right_inv = count_inversions(right)

    merged, split_inv = merge_and_count(left, right)

    for i in range(len(arr)):
        arr[i] = merged[i]

    return left_inv + right_inv + split_inv


# -----------------------------------------------------------
# 🔹 CLOSEST PAIR OF POINTS (2D)
# -----------------------------------------------------------

def closest_pair(points: List[Tuple[int, int]]) -> float:
    """Smallest distance between any two points — O(n log n)."""

    def distance(p1, p2):
        return math.dist(p1, p2)

    def brute_force(pts):
        min_dist = float("inf")
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                min_dist = min(min_dist, distance(pts[i], pts[j]))
        return min_dist

    def divide(px, py):
        n = len(px)

        if n <= 3:
            return brute_force(px)

        mid = n // 2
        mid_x = px[mid][0]

        left_x = px[:mid]
        right_x = px[mid:]

        left_y = list(filter(lambda p: p[0] <= mid_x, py))
        right_y = list(filter(lambda p: p[0] > mid_x, py))

        d_left = divide(left_x, left_y)
        d_right = divide(right_x, right_y)

        d = min(d_left, d_right)

        strip = [p for p in py if abs(p[0] - mid_x) < d]

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d = min(d, distance(strip[i], strip[j]))

        return d

    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])

    return divide(px, py)


# -----------------------------------------------------------
# 🔹 STRASSEN'S MATRIX MULTIPLICATION
# -----------------------------------------------------------

def _next_power_of_two(n: int) -> int:
    p = 1
    while p < n:
        p <<= 1
    return p


def _pad_matrix(A: List[List[float]], size: int) -> List[List[float]]:
    padded = [[0.0] * size for _ in range(size)]
    for i in range(len(A)):
        for j in range(len(A[i])):
            padded[i][j] = A[i][j]
    return padded


def _unpad_matrix(A: List[List[float]], rows: int, cols: int) -> List[List[float]]:
    return [row[:cols] for row in A[:rows]]


def _add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def _sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def _naive_multiply(A, B):
    rA, cA = len(A), len(A[0])
    rB, cB = len(B), len(B[0])

    C = [[0.0] * cB for _ in range(rA)]

    for i in range(rA):
        for k in range(cA):
            for j in range(cB):
                C[i][j] += A[i][k] * B[k][j]

    return C


def _strassen_recursive(A, B, cutoff):
    n = len(A)

    if n <= cutoff:
        return _naive_multiply(A, B)

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = _strassen_recursive(_add(A11, A22), _add(B11, B22), cutoff)
    M2 = _strassen_recursive(_add(A21, A22), B11, cutoff)
    M3 = _strassen_recursive(A11, _sub(B12, B22), cutoff)
    M4 = _strassen_recursive(A22, _sub(B21, B11), cutoff)
    M5 = _strassen_recursive(_add(A11, A12), B22, cutoff)
    M6 = _strassen_recursive(_sub(A21, A11), _add(B11, B12), cutoff)
    M7 = _strassen_recursive(_sub(A12, A22), _add(B21, B22), cutoff)

    C11 = _add(_sub(_add(M1, M4), M5), M7)
    C12 = _add(M3, M5)
    C21 = _add(M2, M4)
    C22 = _add(_sub(_add(M1, M3), M2), M6)

    new = [[0.0] * n for _ in range(n)]

    for i in range(mid):
        new[i][:mid] = C11[i]
        new[i][mid:] = C12[i]
    for i in range(mid):
        new[mid + i][:mid] = C21[i]
        new[mid + i][mid:] = C22[i]

    return new


def strassen_multiply(A: List[List[float]], B: List[List[float]], cutoff: int = 64) -> List[List[float]]:
    """Matrix multiplication using Strassen’s Method."""
    if not A or not B:
        return []

    rowsA, colsA = len(A), len(A[0])
    rowsB, colsB = len(B), len(B[0])

    if colsA != rowsB:
        raise ValueError("Matrix dimensions incompatible for multiplication")

    n = max(rowsA, colsA, rowsB, colsB)
    m = _next_power_of_two(n)

    A_pad = _pad_matrix(A, m)
    B_pad = _pad_matrix(B, m)

    C_pad = _strassen_recursive(A_pad, B_pad, cutoff)

    return _unpad_matrix(C_pad, rowsA, colsB)


# -----------------------------------------------------------
# 🧪 BENCHMARK WORKLOAD
# -----------------------------------------------------------

def run_divide_conquer_operations(n: int = 10000):
    """Runs standard workload for AlgoForge benchmarking."""
    arr = [random.randint(0, 100000) for _ in range(n)]

    sorted_arr = merge_sort(arr)
    quick_sort(arr.copy())
    binary_search(sorted_arr, sorted_arr[len(sorted_arr) // 2])
    count_inversions(arr.copy())

    points = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(500)]
    closest_pair(points)

    # small matrix test for Strassen
    A = [[random.randint(0, 10) for _ in range(4)] for _ in range(4)]
    B = [[random.randint(0, 10) for _ in range(4)] for _ in range(4)]
    strassen_multiply(A, B)

    return len(sorted_arr)


# -----------------------------------------------------------
# Standalone Test Runner
# -----------------------------------------------------------

if __name__ == "__main__":
    print("Running Divide and Conquer module test...")
    print("Workload Output:", run_divide_conquer_operations(2000))