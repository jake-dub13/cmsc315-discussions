"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Start recursive insertion at the root.
        # Smaller values move left and larger values move right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # An empty position means the new node belongs here.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored in this implementation.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # A BST can eliminate an entire subtree after each comparison
        # because values smaller than a node are on the left and
        # larger values are on the right.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # Reaching an empty location means the value was not found.
        if node is None:
            return False

        # The value has been found.
        if value == node.value:
            return True

        # Search only the side where the value could exist.
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node is not None:
            # In-order traversal visits left, node, then right.
            # Since smaller values are on the left and larger values
            # are on the right, the result is sorted.
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== EMPLOYEE ID TREE CONSTRUCTION ===")

    employee_tree = BST()

    employee_ids = [1050, 1025, 1075, 1010, 1040, 1060, 1090]

    # These employee IDs create both left and right subtrees.
    # Each comparison determines whether the ID could be found
    # in the left or right subtree, reducing the search space.
    for employee_id in employee_ids:
        employee_tree.insert(employee_id)

    print("Employee IDs inserted:", employee_ids)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits the left subtree first,
    # then the current node, and finally the right subtree.
    # This produces the employee IDs in sorted order.
    traversal = employee_tree.inorder()

    print("Employee IDs in sorted order:", traversal)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== EMPLOYEE ID SEARCH TESTS ===")

    # Existing employee IDs should return True.
    print("Search for employee ID 1040:", employee_tree.search(1040))
    print("Search for employee ID 1060:", employee_tree.search(1060))

    # Missing employee IDs should return False.
    print("Search for employee ID 1030:", employee_tree.search(1030))
    print("Search for employee ID 1100:", employee_tree.search(1100))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Searching an empty employee tree should return False.
    empty_tree = BST()
    print("Search empty tree for employee ID 1050:",
          empty_tree.search(1050))

    # Edge case 2: Traversing an empty tree should return an empty list.
    print("In-order traversal of empty tree:",
          empty_tree.inorder())

    # Edge case 3: Duplicate employee IDs are ignored in this BST.
    employee_tree.insert(1050)
    print(
        "After attempting to insert duplicate employee ID 1050:",
        employee_tree.inorder()
    )


if __name__ == "__main__":
    main()