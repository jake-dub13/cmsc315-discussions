"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # Create a copy so the original list is not changed.
    sorted_list = lst.copy()

    # Repeat passes through the list.
    for i in range(len(sorted_list) - 1):
        swapped = False

        # Compare neighboring values.
        for j in range(len(sorted_list) - 1 - i):
            if sorted_list[j] > sorted_list[j + 1]:

                # Swap values if they are out of order.
                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )

                swapped = True

        # Stop early if no swaps occurred during the pass.
        if not swapped:
            break

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.
    """

    # A list with zero or one element is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Divide the list into two halves.
    middle = len(lst) // 2
    left_half = lst[:middle]
    right_half = lst[middle:]

    # Recursively sort both halves.
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves.
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """

    result = []
    left_index = 0
    right_index = 0

    # Compare values from both lists and add the smaller one.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values from either list.
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    dataset1 = [42, 19, 88, 7, 31, 64, 12]

    print("Original:", dataset1)
    print("Bubble Sort:", bubble_sort(dataset1))
    print("Merge Sort:", merge_sort(dataset1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")

    dataset2 = [55, 23, 91, 4, 68, 37, 76, 15]

    print("Original:", dataset2)
    print("Bubble Sort:", bubble_sort(dataset2))
    print("Merge Sort:", merge_sort(dataset2))
    print("Both algorithms produced the same sorted result:",
          bubble_sort(dataset2) == merge_sort(dataset2))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    empty_list = []
    sorted_list = [1, 2, 3, 4, 5]
    duplicate_list = [8, 3, 8, 1, 3]

    print("Empty list with Bubble Sort:", bubble_sort(empty_list))
    print("Empty list with Merge Sort:", merge_sort(empty_list))

    print("Already sorted list with Bubble Sort:", bubble_sort(sorted_list))
    print("Already sorted list with Merge Sort:", merge_sort(sorted_list))

    print("Duplicate values with Bubble Sort:", bubble_sort(duplicate_list))
    print("Duplicate values with Merge Sort:", merge_sort(duplicate_list))

    # ===============================
    # REAL-WORLD SORTING EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD EXAMPLE ===")

    # Example: sorting movie popularity scores for a streaming platform.
    popularity_scores = [72, 95, 61, 88, 79, 95, 54]

    print("Original popularity scores:", popularity_scores)
    print("Sorted popularity scores:", merge_sort(popularity_scores))


if __name__ == "__main__":
    main()