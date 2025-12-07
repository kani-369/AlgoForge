"""


 Binary Tree (structure + traversals)
 Binary Search Tree (insert/search/delete)
 AVL Tree (self-balancing BST)
 Helper utilities (height, level order)
 run_tree_operations() — used by benchmark.py

Efficient + clean implementations for AlgoForge.
==============================================================
"""

from __future__ import annotations
from typing import Optional, List, Any
import random

# 
#  Basic Binary Tree Node
# ==============================================================

class TreeNode:
    def __init__(self, value: Any):
        self.val = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

# 
# Traversal Utilities
# --------------------------------------------------------------

def inorder(root: Optional[TreeNode]) -> List[Any]:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def preorder(root: Optional[TreeNode]) -> List[Any]:
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def postorder(root: Optional[TreeNode]) -> List[Any]:
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def level_order(root: Optional[TreeNode]) -> List[Any]:
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return result


# 
#  Binary Search Tree (BST)
# ==============================================================

class BST:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    # Insert value
    def insert(self, val: Any):
        def _insert(node, val):
            if node is None:
                return TreeNode(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node

        self.root = _insert(self.root, val)

    # Search value
    def search(self, val: Any) -> bool:
        node = self.root
        while node:
            if val == node.val:
                return True
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return False

    # Delete node
    def delete(self, val: Any):
        def _min_value_node(node):
            while node.left:
                node = node.left
            return node

        def _delete(node, val):
            if node is None:
                return None
            if val < node.val:
                node.left = _delete(node.left, val)
            elif val > node.val:
                node.right = _delete(node.right, val)
            else:
                # Single child or no child
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # Node with 2 children
                successor = _min_value_node(node.right)
                node.val = successor.val
                node.right = _delete(node.right, successor.val)
            return node

        self.root = _delete(self.root, val)


# 
#  AVL Tree (Self-Balancing BST)
# ==============================================================

class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None
        self.height = 1


def _height(node: Optional[AVLNode]) -> int:
    return node.height if node else 0


def _get_balance(node: Optional[AVLNode]):
    return _height(node.left) - _height(node.right) if node else 0


def _right_rotate(y: AVLNode) -> AVLNode:
    x = y.left
    T = x.right

    x.right = y
    y.left = T

    y.height = 1 + max(_height(y.left), _height(y.right))
    x.height = 1 + max(_height(x.left), _height(x.right))

    return x


def _left_rotate(x: AVLNode) -> AVLNode:
    y = x.right
    T = y.left

    y.left = x
    x.right = T

    x.height = 1 + max(_height(x.left), _height(x.right))
    y.height = 1 + max(_height(y.left), _height(y.right))

    return y


class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def insert(self, val):
        def _insert(node, val):
            if not node:
                return AVLNode(val)

            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)

            node.height = 1 + max(_height(node.left), _height(node.right))
            balance = _get_balance(node)

            # Left-Left
            if balance > 1 and val < node.left.val:
                return _right_rotate(node)

            # Right-Right
            if balance < -1 and val > node.right.val:
                return _left_rotate(node)

            # Left-Right
            if balance > 1 and val > node.left.val:
                node.left = _left_rotate(node.left)
                return _right_rotate(node)

            # Right-Left
            if balance < -1 and val < node.right.val:
                node.right = _right_rotate(node.right)
                return _left_rotate(node)

            return node

        self.root = _insert(self.root, val)


# 
#   Benchmark Helper — run_tree_operations()
# ==============================================================

def run_tree_operations(n: int = 1000):
    """
    Sample benchmark workload for trees.
    Inserts n random values into both BST and AVL Tree.
    Returns traversal lengths.
    """
    values = [random.randint(0, 50000) for _ in range(n)]

    # BST
    bst = BST()
    for v in values:
        bst.insert(v)

    # AVL
    avl = AVLTree()
    for v in values:
        avl.insert(v)

    # Return traversal lengths to confirm structure
    return {
        "bst_inorder_len": len(inorder(bst.root)),
        "avl_inorder_len": len(inorder(avl.root)),
    }


# Debug
if __name__ == "__main__":
    print("Running Trees module quick check...")
    out = run_tree_operations(200)
    print(out)
