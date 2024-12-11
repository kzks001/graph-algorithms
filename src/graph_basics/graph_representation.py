import numpy as np
from loguru import logger


######################
## Adjacency Matrix ##
######################


class AdjMat:
    """A class to represent a graph using an adjacency matrix.

    Attributes:
        num_nodes (int): The number of nodes in the graph.
        is_undirected (bool): Whether the graph is undirected.
        matrix (np.ndarray): The adjacency matrix.
    """

    def __init__(self, num_nodes: int, is_undirected: bool = True):
        """Initialise the adjacency matrix.

        Args:
            num_nodes (int): The number of nodes in the graph.
            is_undirected (bool): Whether the graph is undirected or not.
                Defaults to True.
        """
        self.num_nodes = num_nodes
        self.is_undirected = is_undirected
        self.matrix = np.zeros((num_nodes, num_nodes), dtype=int)

    def add_edge(self, u: int, v: int, weight: int | float = 1):
        """Adds an edge from node `u` to node `v`. If undirected, adds edges
        in both directions. Handles invalid inputs gracefully.

        Args:
            u (int): Source node.
            v (int): Destination node.
            weight (int | float, optional): Edge weight. Defaults to 1.

        Logs:
            Warnings if the inputs are invalid but does not raise exceptions.
        """
        try:
            if not isinstance(u, int) or not isinstance(v, int):
                logger.warning(
                    f"Warning: Nodes u ({u}) and v ({v}) must be integers. Skipping."
                )
                return

            if not (0 <= u < self.num_nodes) or not (0 <= v < self.num_nodes):
                logger.warning(
                    f"Warning: Nodes u ({u}) and v ({v}) must be in the range "
                    f"[0, {self.num_nodes - 1}]. Skipping."
                )
                return

            self.matrix[u][v] = weight
            if self.is_undirected:
                self.matrix[v][u] = weight
            logger.info(f"Edge added: {u} -> {v} with weight {weight}.")
        except Exception as e:
            logger.error(f"Unexpected error while adding edge ({u} -> {v}): {e}")

    def remove_edge(self, u: int, v: int):
        """Removes an edge from node `u` to node `v`.

        Args:
            u (int): Source node.
            v (int): Destination node.
        """
        self.matrix[u][v] = 0
        if self.is_undirected:
            self.matrix[v][u] = 0

    def has_edge(self, u: int, v: int) -> bool:
        """Check if there is an edge from node `u` to node `v`.

        Args:
            u (int): Source node.
            v (int): Destination node.

        Returns:
            bool: True if the edge exists, False otherwise.
        """
        return self.matrix[u][v] != 0

    def display(self):
        """logger.info the adjacency matrix in a readable format."""
        logger.info(f"\n{self.matrix}")


####################
## Adjacency list ##
####################


class AdjList:
    """A class to represent a graph using an adjacency list.

    Attributes:
        num_nodes (int): The number of nodes in the graph.
        is_undirected (bool): Whether the graph is undirected.
        adj_list (list): The adjacency list.
    """

    def __init__(self, num_nodes: int, is_undirected: bool = True):
        """Initialize the adjacency list.

        Args:
            num_nodes (int): The number of nodes in the graph.
            is_undirected (bool): Whether the graph is undirected. Defaults to
                True.
        """
        self.num_nodes = num_nodes
        self.is_undirected = is_undirected
        self.adj_list = [[] for _ in range(num_nodes)]

    def add_edge(self, u: int, v: int, weight: int | float = 1):
        """Adds an edge from node `u` to node `v`. If undirected, adds edges
        in both directions. Handles invalid inputs gracefully.

        Args:
            u (int): Source node.
            v (int): Destination node.
            weight (int | float, optional): Edge weight. Defaults to 1.

        Logs:
            Warnings if the inputs are invalid but does not raise exceptions.
        """
        try:
            if not isinstance(u, int) or not isinstance(v, int):
                logger.warning(
                    f"Warning: Nodes u ({u}) and v ({v}) must be integers. Skipping."
                )
                return

            if not (0 <= u < self.num_nodes) or not (0 <= v < self.num_nodes):
                logger.warning(
                    f"Warning: Nodes u ({u}) and v ({v}) must be in the range "
                    f"[0, {self.num_nodes - 1}]. Skipping."
                )
                return

            if any(neighbour == v for neighbour, _ in self.adj_list[u]):
                logger.warning(f"Edge {u} -> {v} already exists. Skipping.")
                return

            self.adj_list[u].append((v, weight))
            if self.is_undirected:
                self.adj_list[v].append((u, weight))
            logger.info(f"Edge added: {u} -> {v} with weight {weight}.")

        except Exception as e:
            logger.error(f"Unexpected error while adding edge ({u} -> {v}): {e}")

    def remove_edge(self, u: int, v: int):
        """Removes an edge from node `u` to node `v`.

        Args:
            u (int): Source node.
            v (int): Destination node.
        """
        self.adj_list[u] = [
            (node, weight) for node, weight in self.adj_list[u] if node != v
        ]
        if self.is_undirected:
            self.adj_list[v] = [
                (node, weight) for node, weight in self.adj_list[v] if node != u
            ]
        logger.info(f"Edge removed: {u} -> {v}.")

    def has_edge(self, u: int, v: int) -> bool:
        """Check if there is an edge from node `u` to node `v`.

        Args:
            u (int): Source node.
            v (int): Destination node.

        Returns:
            bool: True if the edge exists, False otherwise.
        """
        return any(node == v for node, _ in self.adj_list[u])

    def display(self):
        """Logs the adjacency list in a readable format."""
        for i, neighbours in enumerate(self.adj_list):
            logger.info(f"Node {i}: {neighbours}")
