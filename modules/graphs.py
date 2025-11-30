"""

 BFS (Breadth-First Search)
 DFS (Depth-First Search)
 Dijkstra's Algorithm (weighted shortest path)
 Topological Sort (for DAGs)
 Cycle Detection (DFS-based)
 Connected Components (undirected)
 Unweighted Shortest Path (BFS)
 run_graph_operations() — benchmark workload


==============================================================
"""

from __future__ import annotations
from typing import List, Dict, Set, Tuple, Optional
from collections import deque
import heapq
import random


# 
# Graph creation (adjacency list)
# ==============================================================

def create_graph(n: int, edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    """Creates an adjacency list for an unweighted graph."""
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected
    return graph


# 
#  BFS (Breadth-First Search)
# ==============================================================

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    q = deque([start])
    order = []

    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)

    return order


# 
#  DFS (Depth-First Search)
# ==============================================================

def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    order = []

    def _dfs(node):
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            _dfs(neighbor)

    _dfs(start)
    return order


# 
#  Dijkstra (Weighted Shortest Path)
# ==============================================================

def dijkstra_weighted(adj: Dict[int, List[Tuple[int, float]]], start: int) -> Dict[int, float]:
    """Returns shortest distances from start node using Dijkstra."""
    dist = {node: float("inf") for node in adj}
    dist[start] = 0.0

    heap = [(0.0, start)]
    visited = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist


# 
#  Topological Sort (Kahn’s Algorithm)
# ==============================================================

def topological_sort(n: int, edges: List[Tuple[int, int]]) -> List[int]:
    """Topological ordering for a directed acyclic graph (DAG)."""
    indegree = [0] * n
    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return order  # May be incomplete if cycle exists


# 
#  Cycle Detection (DFS)
# ==============================================================

def has_cycle(graph: Dict[int, List[int]]) -> bool:
    visited = set()
    parent = {}

    def _dfs(u, p):
        visited.add(u)
        parent[u] = p
        for v in graph[u]:
            if v not in visited:
                if _dfs(v, u):
                    return True
            elif v != p:
                return True
        return False

    for node in graph:
        if node not in visited and _dfs(node, -1):
            return True
    return False


# 
# Connected Components
# ==============================================================

def connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    visited = set()
    comps = []

    for node in graph:
        if node not in visited:
            comp = []
            q = deque([node])
            while q:
                u = q.popleft()
                if u in visited:
                    continue
                visited.add(u)
                comp.append(u)
                for v in graph[u]:
                    if v not in visited:
                        q.append(v)
            comps.append(comp)

    return comps


# 
#  Unweighted Shortest Path (BFS)
# ==============================================================

def shortest_path_unweighted(graph: Dict[int, List[int]], start: int, end: int) -> int:
    """Returns the number of edges in the shortest path."""
    q = deque([(start, 0)])
    visited = set()

    while q:
        node, dist = q.popleft()
        if node == end:
            return dist

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append((neighbor, dist + 1))

    return -1  # unreachable


# 
#  Benchmark Helper — run_graph_operations()
# ==============================================================

def run_graph_operations(n: int = 500) -> Dict[str, int]:
    """
    Creates a random graph and runs all graph algorithms.
    Returns summary metrics for benchmarking.
    """
    # Random edges
    edges = [(random.randint(0, n - 1), random.randint(0, n - 1)) for _ in range(n * 2)]
    graph = create_graph(n, edges)

    # Weighted version for Dijkstra
    weighted_adj = {
        i: [(random.randint(0, n - 1), random.random() * 10) for _ in range(3)]
        for i in range(n)
    }

    bfs_res = bfs(graph, 0)
    dfs_res = dfs(graph, 0)
    topo_res = topological_sort(n, edges)
    cc_res = connected_components(graph)
    dij_res = dijkstra_weighted(weighted_adj, 0)

    return {
        "bfs_len": len(bfs_res),
        "dfs_len": len(dfs_res),
        "components": len(cc_res),
        "topo_len": len(topo_res),
        "dijkstra_reachable": sum(1 for d in dij_res.values() if d < float("inf")),
    }


if __name__ == "__main__":
    print("Running Graph module quick check...")
    out = run_graph_operations(200)
    print(out)
