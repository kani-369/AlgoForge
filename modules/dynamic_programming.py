"""


 Fibonacci (Memoization + Tabulation)
 0/1 Knapsack Problem
 Longest Common Subsequence (LCS)
 Coin Change Problem
 Matrix Chain Multiplication
 Subset Sum Problem


==============================================================
"""

from functools import lru_cache
from typing import List
import math


# 
# Fibonacci — Memoization (Top-Down) and Tabulation (Bottom-Up)
# ==============================================================

@lru_cache(maxsize=None)
def fibonacci_memoized(n: int) -> int:
    """Top-down Fibonacci using memoization."""
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fibonacci_tabulated(n: int) -> int:
    """Bottom-up Fibonacci using tabulation."""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 
#  0/1 Knapsack Problem
# ==============================================================

def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Classic 0/1 Knapsack — maximize profit within weight limit.
    Uses bottom-up DP table.
    """
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# 
#  Longest Common Subsequence (LCS)
# ==============================================================

def longest_common_subsequence(X: str, Y: str) -> int:
    """
    Find the length of the longest common subsequence between X and Y.
    Example: X = "AGGTAB", Y = "GXTXAYB" → 4 (GTAB)
    """
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# 
#  Coin Change Problem
# ==============================================================

def coin_change(coins: List[int], amount: int) -> int:
    """
    Find the minimum number of coins to make the given amount.
    Returns -1 if not possible.
    """
    dp = [math.inf] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != math.inf else -1


# 
#  Matrix Chain Multiplication
# ==============================================================

def matrix_chain_order(p: List[int]) -> int:
    """
    Given a chain of matrices A1...An, find minimum cost to multiply them.
    p = [dim1, dim2, dim3, ..., dimN]
    Returns the minimum number of scalar multiplications needed.
    """
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]

    for chain_len in range(2, n + 1):
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = math.inf

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


#  Subset Sum Problem
# ==============================================================

def subset_sum(nums: List[int], target: int) -> bool:
    """
    Determines if there exists a subset with sum equal to target.
    """
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True  # base case: sum=0 always possible

    for i in range(1, n + 1):
        for j in range(1, target + 1):

            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]


# 
#  Test Harness (for development only)
# ==============================================================

def run_dynamic_programming_examples():
    """Simple correctness tests before benchmarking."""
    print("\n Running sample Dynamic Programming algorithms...\n")

    print("① Fibonacci:", fibonacci_tabulated(10))
    print("② Knapsack:", knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))
    print("③ LCS:", longest_common_subsequence("AGGTAB", "GXTXAYB"))
    print("④ Coin Change:", coin_change([1, 2, 5], 11))
    print("⑤ Matrix Chain Multiplication:", matrix_chain_order([40, 20, 30, 10, 30]))
    print("⑥ Subset Sum:", subset_sum([3, 34, 4, 12, 5, 2], 9))
    print("\nAll DP algorithm tests completed.\n")


if __name__ == "__main__":
    run_dynamic_programming_examples()