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
    path from the root to a leaf node. It uses a stack to simulate the
    depth-first traversal of the tree.

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


###################################
## Example: Path Sum Binary Tree ##
###################################


def has_path_sum_recursive(root: TreeNode, target_sum: int) -> bool:
    """Check if the binary tree has a root-to-leaf path with the given sum.

    Args:
        root (TreeNode): The root of the binary tree.
        target_sum (int): The target sum to check.

    Returns:
        bool: True if a path exists, otherwise False.
    """
    if root is None:
        return False

    if root.left is None and root.right is None:
        return target_sum == root.val

    return has_path_sum_recursive(
        root.left, target_sum - root.val
    ) or has_path_sum_recursive(root.right, target_sum - root.val)


#################################
## Some Variations of Path Sum ##
#################################


def count_path_sum_recursive(root: TreeNode, target_sum: int) -> int:
    """Count the number of root-to-leaf paths with a given sum.

    Args:
        root (TreeNode): The root of the binary tree.
        target_sum (int): The target sum to check.

    Returns:
        int: The count of paths that meet the target sum.
    """
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1 if target_sum == root.val else 0

    left = count_path_sum_recursive(root.left, target_sum - root.val)
    right = count_path_sum_recursive(root.right, target_sum - root.val)

    return left + right


def find_path_with_sum(root: TreeNode, target_sum: int) -> list[int] | None:
    """Finds a path in a binary tree where the sum of the node values equals the
    target sum.

    Args:
        root (TreeNode): The root of the binary tree.
        target_sum (int): The target sum for the path.

    Returns:
        list[int] | None: A list representing the path with the target sum, or
            None if no such path exists.
    """
    if root is None:
        return None

    if root.left is None and root.right is None:
        if target_sum == root.val:
            return [root.val]

    left = find_path_with_sum(root.left, target_sum - root.val)
    if left is not None:
        return [root.val] + left

    right = find_path_with_sum(root.right, target_sum - root.val)
    if right is not None:
        return [root.val] + right

    return None


def find_paths_with_sum(root: TreeNode, target_sum: int) -> list[list[int]] | None:
    """Finds all paths in a binary tree where the sum of the node values equals
    the target sum.

    Args:
        root (TreeNode): The root of the binary tree.
        target_sum (int): The target sum for the paths.

    Returns:
        list[list[int]]: A list of lists, where each inner list represents a
        path with the target sum. Returns an empty list if no such path exists.
    """
    if root is None:
        return []

    if root.left is None and root.right is None:
        if target_sum == root.val:
            return [[root.val]]
        else:
            return []

    left = find_paths_with_sum(root.left, target_sum - root.val)
    right = find_paths_with_sum(root.right, target_sum - root.val)

    all_paths = []
    for path in left + right:
        all_paths.append([root.val] + path)

    return all_paths


###########################################
## Example: Count Good Nodes Binary Tree ##
###########################################


def count_good_nodes(root: TreeNode, max_val: int = float("-inf")) -> int:
    """
    Counts the number of "good" nodes in a binary tree. A node is considered
    "good" if its value is greater than or equal to the maximum value seen
    along the path from the root to that node.

    Args:
        root (TreeNode): The root of the binary tree.
        max_val (int, optional): The maximum value encountered along the
            path to the current node. Defaults to negative infinity.

    Returns:
        int: The count of "good" nodes in the binary tree.
    """
    if root is None:
        return 0

    is_good = root.val >= max_val
    max_val = max(root.val, max_val)

    return (
        (1 if is_good else 0)
        + count_good_nodes(root.left, max_val)
        + count_good_nodes(root.right, max_val)
    )
