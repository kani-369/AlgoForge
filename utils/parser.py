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

MODULE_PRIORITY = [
    "graphs",
    "dynamic_programming",
    "greedy",
    "divide_conquer",
    "sorting",
    "hashing",
    "trees",
    "linked_list",
    "stacks_queues",
    "arrays"
]

import difflib

def fuzzy_match(word: str, text: str, threshold: float = 0.75) -> bool:
    """
    Returns True if 'word' is similar to any substring in 'text'
    using fuzzy matching.
    """
    words = text.split()
    for w in words:
        similarity = difflib.SequenceMatcher(None, word, w).ratio()
        if similarity >= threshold:
            return True
    return False


def detect_module_from_input(user_input: str) -> str:
    """
    Detect module using:
    1. Priority list
    2. Exact keyword match
    3. Fuzzy match for typos
    """

    text = user_input.lower()

    for module in MODULE_PRIORITY:
        for kw in MODULE_KEYWORDS[module]:
            # First try exact match
            if kw in text:
                return module

            # Then try fuzzy match for misspellings
            if fuzzy_match(kw, text):
                return module

    return None

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
    # This searches for the keyword inside the chosen modu
    # le
    user_text = user_input.lower()
    # STEP 2 — detect operation keyword (exact OR fuzzy)
    for keyword in MODULE_KEYWORDS[module]:
    # Exact match first
        if keyword in user_text:
            result["operation"] = keyword
            break

    # Fuzzy match as backup
        if fuzzy_match(keyword, user_text):
            result["operation"] = keyword
            break






    return result

if __name__ == "__main__":
    #test Queries 
    tests = [

        "Sort 1000 numbers fast", 
        "Find the shortespath in this graph", 
        "Use knapsacs to solve this problem",
        "Schedule maximum tasks",
        "Insert into linked list",
        "Find subset exists"
        "search using the hash map",
        "Push in a stack"
        "Binary search example",
        "Closest pair of points"

    ] 

    for t in tests:
        print(t, "->", parse_input(t))