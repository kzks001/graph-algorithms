from structure import TreeNode

###########################################
## Example: Maximum Depth of Binary Tree ##
###########################################


def max_depth_recursive(root: TreeNode) -> int:
    """Calculates the maximum depth of a binary tree using recursion.

    This function computes the depth as the number of nodes along the longest
    path from the root node to a leaf node. It recursively traverses the left
    and right subtrees to determine their respective depths.

    Args:
        root (TreeNode): The root node of the binary tree to traverse.
            The `TreeNode` class should have `left` and `right` attributes for
            its child nodes.

    Returns:
        int: The maximum depth of the binary tree, measured as the number of
        nodes from the root to the furthest leaf.
    """
    if root is None:
        return 0

    left_depth = max_depth_recursive(root.left)
    right_depth = max_depth_recursive(root.right)

    return max(left_depth, right_depth) + 1


def max_depth_iterative(root: TreeNode) -> int:
    """Finds the maximum depth of a binary tree using an iterative approach.

    This function calculates the depth as the number of nodes along the longest
    path from the root to a leaf node. It uses a stack to simulate the depth-first
    traversal of the tree.

    Args:
        root (TreeNode): The root node of the binary tree to traverse.
            The `TreeNode` class should have `left` and `right` attributes for
            its child nodes.

    Returns:
        int: The maximum depth of the binary tree, measured as the number of
        nodes from the root to the furthest leaf.
    """

    if root is None:
        return 0

    stack = [(root, 1)]
    max_depth = 0

    while stack:
        node, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))

    return max_depth
