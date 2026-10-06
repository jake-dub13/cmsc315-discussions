"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Return an empty list if the starting node does not exist.
    if start not in graph:
        return []

    visited = set()
    order = []

    # A queue processes nodes in first-in, first-out order,
    # which allows BFS to explore the graph level by level.
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        order.append(current)

        # Add unvisited neighbors so they can be explored later.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # BFS explores nearby nodes before going deeper.
    # DFS instead follows one path as deeply as possible first.
    return order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # This graph represents a streaming recommendation network.
    # Each node represents a movie, and each edge represents
    # a similarity or recommendation connection between movies.
    graph = {
        "Movie A": ["Movie B", "Movie C"],
        "Movie B": ["Movie A", "Movie D", "Movie E"],
        "Movie C": ["Movie A", "Movie F"],
        "Movie D": ["Movie B"],
        "Movie E": ["Movie B", "Movie F"],
        "Movie F": ["Movie C", "Movie E"]
    }

    print("\n=== GRAPH STRUCTURE ===")
    for node, neighbors in graph.items():
        print(node, "->", neighbors)

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    start = "Movie A"

    # BFS starts at Movie A and visits all directly connected
    # movies before moving farther through the graph.
    print("Starting node:", start)
    print("Traversal order:", bfs(graph, start))

    # Add another movie and connect it to Movie D.
    graph["Movie G"] = ["Movie D"]
    graph["Movie D"].append("Movie G")

    print("\nAfter adding Movie G:")
    print("Updated traversal:", bfs(graph, start))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: A missing starting node safely returns an empty list.
    print("Missing node:", bfs(graph, "Movie Z"))

    # Edge case 2: A graph with only one node visits that node once.
    single_node_graph = {
        "Movie X": []
    }

    print("Single-node graph:", bfs(single_node_graph, "Movie X"))

    # Edge case 3: Start BFS from a different node.
    print("Starting from Movie F:", bfs(graph, "Movie F"))


if __name__ == "__main__":
    main()