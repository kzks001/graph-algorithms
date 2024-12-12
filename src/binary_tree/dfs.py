"""This script demonstrates various Depth-First Search (DFS) traversal
techniques for binary trees.

Example Binary Tree:
        1
       / \
      2   3
     / \
    4   5

The tree structure is represented as:
- Node 1 is the root with left child 2 and right child 3.
- Node 2 has left child 4 and right child 5.
- Nodes 3, 4, and 5 are leaf nodes (i.e., they have no children).

Expected Traversal Outputs:
1. Basic DFS:
   Visits nodes in depth-first order without specific output.

2. Preorder Traversal:
   Visits the current node, then the left subtree, and finally the right subtree.
   Result: [1, 2, 4, 5, 3]

3. Inorder Traversal:
   Visits the left subtree, then the current node, and finally the right subtree.
   Result: [4, 2, 5, 1, 3]

4. Postorder Traversal:
   Visits the left subtree, then the right subtree, and finally the current node.
   Result: [4, 5, 2, 3, 1]
"""

from structure import TreeNode
from loguru import logger

#####################
## Basic Traversal ##
#####################


def dfs(node: TreeNode) -> None:
    """Performs a basic Depth-First Search (DFS) traversal on a binary tree.

    This traversal visits each node in a depth-first manner, processing the left
    subtree before the right subtree.

    Args:
        node (TreeNode): The root node of the binary tree to traverse.
            The `TreeNode` class should have `left` and `right` attributes for
            its child nodes.
    """
    if node is None:
        return

    dfs(node.left)
    dfs(node.right)


########################
## Preorder Traversal ##
########################


def preorder_dfs(node: TreeNode) -> None:
    """Performs a preorder Depth-First Search (DFS) traversal on a binary tree.

    In preorder traversal, the current node is processed before its child nodes.
    The traversal order is: current node -> left subtree -> right subtree.

    Args:
        node (TreeNode): The root node of the binary tree to traverse.
            The `TreeNode` class should have `left` and `right` attributes for
            its child nodes.
    """
    if node is None:
        return

    logger.info(node.val)
    preorder_dfs(node.left)
    preorder_dfs(node.right)


#######################
## Inorder Traversal ##
#######################


def inorder_dfs(node: TreeNode) -> None:
    """Performs an inorder Depth-First Search (DFS) traversal on a binary tree.

    In inorder traversal, the left subtree is processed first, followed by the
    current node, and then the right subtree. This traversal is often used to
    retrieve values from a binary search tree in sorted order.

    Args:
        node (TreeNode): The root node of the binary tree to traverse.
            The `TreeNode` class should have `left` and `right` attributes for
            its child nodes.
    """
    if node is None:
        return

    inorder_dfs(node.left)
    logger.info(node.val)
    inorder_dfs(node.right)


#########################
## Postorder Traversal ##
#########################


def postorder_dfs(node: TreeNode) -> None:
    """Performs a postorder Depth-First Search (DFS) traversal on a binary tree.

    In postorder traversal, the child nodes are processed first (left subtree,
    then right subtree), followed by the current node.

    Args:
        node (TreeNode): The root node of the binary tree to traverse.
            The `TreeNode` class should have `left` and `right` attributes for
            its child nodes.
    """
    if node is None:
        return

    postorder_dfs(node.left)
    postorder_dfs(node.right)
    logger.info(node.val)
