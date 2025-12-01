# parser.py

MODULE_KEYWORDS = {
    "arrays": [
        "array", "index", "append", "insert", "delete", "update",
        "search", "find", "position"
    ],

    "linked_list": [
        "linked list", "node", "insert", "delete", "traverse", "pointer"
    ],

    "stacks_queues": [
        "stack", "queue", "push", "pop", "enqueue", "dequeue",
        "fifo", "lifo"
    ],

    "hashing": [
        "hash", "hashmap", "dictionary", "lookup", "fast search", "collision"
    ],

    "trees": [
        "tree", "bst", "binary tree", "traversal",
        "height", "depth", "balanced"
    ],

    "graphs": [
        "graph", "edge", "node", "vertex", "route",
        "shortest path", "distance", "mst",
        "minimum spanning tree", "dijkstra", "kruskal", "prim"
    ],

    "sorting": [
        "sort", "order", "arrange", "ascending", "descending"
    ],

    "divide_conquer": [
        "divide", "conquer", "merge sort", "quick sort",
        "binary search", "closest pair", "inversion"
    ],

    "dynamic_programming": [
        "dp", "fibonacci", "knapsack", "subset", "lcs",
        "coin change", "matrix chain", "optimal"
    ],

    "greedy": [
        "greedy", "activity", "schedule", "compression",
        "huffman", "fractional knapsack"
    ]
}






def detect_module_from_input(user_input: str) -> str:
    """
    Detect which DSA module should handle the user query,
    based on keyword matching.
    Returns the module name (string) or None if no match.
    """

    text = user_input.lower()  # convert to lowercase for matching

    for module, keywords in MODULE_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return module  # first match found

    return None  # no module matched


def parse_input(user_input: str) -> dict:
    """
    Main parser function that:
    1. Detects which module the user needs
    2. Identifies the operation keyword
    3. Returns a clean structured dictionary
    """

    result = {
        "raw_input": user_input,
        "module": None,
        "operation": None,
    }

    # STEP 1 — detect module
    module = detect_module_from_input(user_input)
    result["module"] = module

    if module is None:
        # No module matched
        result["operation"] = None
        return result

    # STEP 2 — detect the exact operation keyword
    # This searches for the keyword inside the chosen module
    user_text = user_input.lower()
    for keyword in MODULE_KEYWORDS[module]:
        if keyword in user_text:
            result["operation"] = keyword
            break

    return result