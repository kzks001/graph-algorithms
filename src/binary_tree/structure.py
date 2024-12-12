class TreeNode:
    """Class representing a node in a binary tree.

    Attributes:
        value (int): The value of the node.
        left (TreeNode | None): The left child node.
        right (TreeNode | None): The right child node.

    Example:
        Creating a binary tree structure:

        >>> root = TreeNode(10)
        >>> root.left = TreeNode(5)
        >>> root.right = TreeNode(15)
        >>> root.left.left = TreeNode(3)
        >>> root.left.right = TreeNode(7)
        >>> print(root)
        TreeNode(
                value=10,
                left=TreeNode(
                            value=5,
                            left=TreeNode(value=3, left=None, right=None),
                            right=TreeNode(value=7, left=None, right=None)
                            ),
                right=TreeNode(
                            value=15,
                            left=None,
                            right=None
                            )
                )
    """

    def __init__(
        self, val: any, left: "TreeNode" | None = None, right: "TreeNode" | None = None
    ):
        """Initialise a TreeNode.

        Args:
            val (any): The value of the node.
            left (TreeNode&quot; | None, optional): The left child node.
                Defaults to None.
            right (TreeNode&quot; | None, optional): The right child node.
                Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """Return a string representation of the TreeNode.

        Returns:
            str: String representation of the node.
        """
        return f"TreeNode(value={self.value}, left={self.left}, right={self.right})"
