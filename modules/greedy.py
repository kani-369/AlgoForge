"""


 Dijkstra's Algorithm  
 Kruskal's Algorithm (Union-Find)  
 Prim's Algorithm (Min-Heap)  
 Huffman Coding  
 Activity Selection (Interval Scheduling)  
 Fractional Knapsack  


"""
from typing import Dict, List, Tuple, Any
import heapq
import random
import math
from collections import defaultdict, Counter


# 
#  DIJKSTRA'S ALGORITHM
# ==============================================================

def dijkstra(adj: Dict[int, List[Tuple[int, float]]], source: int) -> Dict[int, float]:
    """
    adj: adjacency list {u: [(v, weight), ...]}
    source: starting node
    Returns a dict of shortest distances from source.
    Complexity: O((V + E) log V)
    """
    dist = {node: math.inf for node in adj}
    dist[source] = 0.0

    visited = set()
    heap = [(0.0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, w in adj.get(u, []):
            nd = d + w
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist


# 
#  KRUSKAL'S ALGORITHM (UNION-FIND)
# ==============================================================

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

        return True


def kruskal(n_nodes: int, edges: List[Tuple[float, int, int]]) -> Tuple[float, List[Tuple[int, int, float]]]:
    """
    edges: list of (weight, u, v)
    Returns: (total_weight, mst_edges)
    Complexity: O(E log E)
    """
    uf = UnionFind(n_nodes)
    edges_sorted = sorted(edges, key=lambda x: x[0])

    mst = []
    total_weight = 0.0

    for w, u, v in edges_sorted:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
        if len(mst) == n_nodes - 1:
            break

    return total_weight, mst


# 
#  PRIM'S ALGORITHM (Min-Heap)
# ==============================================================

def prim(n_nodes: int, adj: Dict[int, List[Tuple[int, float]]], start: int = 0
         ) -> Tuple[float, List[Tuple[int, int, float]]]:
    """
    adj: adjacency list
    start: starting node
    Returns: (total_weight, mst_edges)
    Complexity: O((V + E) log V)
    """
    visited = [False] * n_nodes
    visited[start] = True

    heap = []
    for v, w in adj.get(start, []):
        heapq.heappush(heap, (w, start, v))

    mst = []
    total_weight = 0.0

    while heap and len(mst) < n_nodes - 1:
        w, u, v = heapq.heappop(heap)
        if visited[v]:
            continue

        visited[v] = True
        mst.append((u, v, w))
        total_weight += w

        for to, wt in adj.get(v, []):
            if not visited[to]:
                heapq.heappush(heap, (wt, v, to))

    return total_weight, mst


# 
#  HUFFMAN CODING
# ==============================================================

def huffman_coding(data: str) -> Tuple[Dict[str, str], float]:
    """
    Builds Huffman coding for the characters in data.
    Returns: (codes_dict, average_code_length_in_bits)
    Complexity: O(n log n)
    """

    if not data:
        return {}, 0.0

    freq = Counter(data)
    heap_nodes = [(freq[ch], ch) for ch in freq]
    heapq.heapify(heap_nodes)

    # Build tree
    while len(heap_nodes) > 1:
        f1, n1 = heapq.heappop(heap_nodes)
        f2, n2 = heapq.heappop(heap_nodes)
        combined = (n1, n2)
        heapq.heappush(heap_nodes, (f1 + f2, combined))

    _, root = heap_nodes[0]

    # Build codes
    codes: Dict[str, str] = {}

    def build(node, prefix):
        if isinstance(node, str):
            codes[node] = prefix or "0"
            return
        left, right = node
        build(left, prefix + "0")
        build(right, prefix + "1")

    build(root, "")

    # Average code length
    total_bits = sum(len(codes[ch]) * freq[ch] for ch in freq)
    avg_len = total_bits / sum(freq.values())

    return codes, avg_len


# 
#  ACTIVITY SELECTION
# ==============================================================

def activity_selection(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    intervals: list of (start, end)
    Returns a maximum-size set of non-overlapping intervals.
    Complexity: O(n log n)
    """
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    selected = []
    last_end = -math.inf

    for s, f in sorted_intervals:
        if s >= last_end:
            selected.append((s, f))
            last_end = f

    return selected


# 
#  FRACTIONAL KNAPSACK
# ==============================================================

def fractional_knapsack(items: List[Tuple[float, float]], capacity: float
                        ) -> Tuple[float, List[Tuple[float, float, float]]]:
    """
    items: list of (value, weight)
    capacity: float
    Returns: (max_value, [(value_taken, weight_taken, fraction)])
    Complexity: O(n log n)
    """

    items_with_ratio = [((v / w if w != 0 else float('inf')), v, w) for v, w in items]
    items_with_ratio.sort(key=lambda x: x[0], reverse=True)

    picked = []
    remaining = capacity
    total_value = 0.0

    for ratio, v, w in items_with_ratio:
        if remaining <= 0:
            break

        if w <= remaining:
            picked.append((v, w, 1.0))
            total_value += v
            remaining -= w
        else:
            fraction = remaining / w
            picked.append((v * fraction, w * fraction, fraction))
            total_value += v * fraction
            remaining = 0

    return total_value, picked


# 
#  Benchmark Helper — run_greedy_operations()
# ==============================================================

def run_greedy_operations(seed: int = 42) -> Dict[str, Any]:
    """
    Runs small workloads for each greedy algorithm for internal testing
    & benchmarking integration.
    """
    random.seed(seed)
    results = {}

    # ---- DIJKSTRA ----
    n = 100
    adj = {i: [] for i in range(n)}
    for _ in range(n * 3):
        u = random.randrange(n)
        v = random.randrange(n)
        if u == v:
            continue
        w = random.random() * 10
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = dijkstra(adj, 0)
    results["dijkstra_sample_dist_0"] = dist.get(0, None)

    # ---- KRUSKAL & PRIM ----
    edges = []
    seen = set()
    for u in adj:
        for v, w in adj[u]:
            if (v, u) not in seen:
                seen.add((u, v))
                edges.append((w, u, v))

    kruskal_weight, _ = kruskal(n, edges)
    prim_weight, _ = prim(n, adj, 0)

    results["kruskal_weight"] = kruskal_weight
    results["prim_weight"] = prim_weight

    # ---- HUFFMAN ----
    sample_text = "".join(random.choice("abcdabcdabcd") for _ in range(200))
    codes, avg_len = huffman_coding(sample_text)
    results["huffman_avg_len"] = avg_len
    results["huffman_unique_symbols"] = len(codes)

    # ---- ACTIVITY SELECTION ----
    intervals = []
    for _ in range(200):
        s = random.randint(0, 1000)
        f = s + random.randint(1, 50)
        intervals.append((s, f))

    results["activity_selected_count"] = len(activity_selection(intervals))

    # ---- FRACTIONAL KNAPSACK ----
    items = [(random.uniform(1, 100), random.uniform(1, 20)) for _ in range(100)]
    max_val, picked = fractional_knapsack(items, 200)
    results["fractional_value"] = max_val
    results["fractional_picked_count"] = len(picked)

    return results


# Debug run
if __name__ == "__main__":
    print("Running greedy module quick check...")
    out = run_greedy_operations()
    for k, v in out.items():
        print(f"{k}: {v}")
