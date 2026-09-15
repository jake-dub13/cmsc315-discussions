"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Linear search checks each value from beginning to end.
    # In the worst case, every element must be checked,
    # which gives linear search O(n) time complexity.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = (low + high) // 2

        # Check the middle value first.
        if lst[middle] == target:
            return middle

        # If the target is smaller, discard the right half.
        elif target < lst[middle]:
            high = middle - 1

        # If the target is larger, discard the left half.
        else:
            low = middle + 1

        # Each iteration removes about half of the remaining
        # search space, giving binary search O(log n) performance.

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    small_data = [10, 20, 30, 40, 50, 60, 70]
    existing_value = 50
    missing_value = 35

    print("Small dataset:", small_data)

    # Both searches should find 50 at index 4.
    print("Linear search for 50:",
          linear_search(small_data, existing_value))
    print("Binary search for 50:",
          binary_search(small_data, existing_value))

    # Both searches should return -1 because 35 is not present.
    print("Linear search for 35:",
          linear_search(small_data, missing_value))
    print("Binary search for 35:",
          binary_search(small_data, missing_value))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    large_data = list(range(1, 10001))
    large_target = 9999

    print("Large dataset size:", len(large_data))

    print("Linear search for 9999:",
          linear_search(large_data, large_target))
    print("Binary search for 9999:",
          binary_search(large_data, large_target))

    # Both algorithms return the same index, but linear search may
    # need to examine thousands of values. Binary search repeatedly
    # cuts the remaining search area in half, making it much more
    # efficient as the dataset becomes larger.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: An empty list contains no values,
    # so both searches should return -1.
    empty_list = []

    print("Linear search on empty list:",
          linear_search(empty_list, 10))
    print("Binary search on empty list:",
          binary_search(empty_list, 10))

    # Edge case 2: A single-element list should return index 0
    # when the target matches the only value.
    single_item = [25]

    print("Linear search on single-element list:",
          linear_search(single_item, 25))
    print("Binary search on single-element list:",
          binary_search(single_item, 25))

    # ===============================
    # REAL-WORLD SEARCH SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SEARCH SCENARIO ===")

    # A store could search a sorted list of product ID numbers.
    # Binary search is useful when the list is large and sorted.
    # Linear search can still be useful for small or unsorted lists.

    product_ids = [1001, 1005, 1010, 1015, 1020, 1025, 1030]
    product_to_find = 1025

    print("Product IDs:", product_ids)
    print("Linear search result:",
          linear_search(product_ids, product_to_find))
    print("Binary search result:",
          binary_search(product_ids, product_to_find))


if __name__ == "__main__":
    main()