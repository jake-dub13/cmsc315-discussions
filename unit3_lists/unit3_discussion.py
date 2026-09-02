"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Inserting into the beginning or middle shifts later elements to the right.
    # Inserting near the end usually requires less shifting and is more efficient.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Validate the index before removing an item to avoid an IndexError.
    # Safe deletion prevents the program from crashing when an invalid index is used.
    if index < 0 or index >= len(lst):
        return None

    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because each element is checked in order.
    # The search continues sequentially until the value is found or the list ends.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    games = ["Halo", "Minecraft", "Skyrim", "Fallout"]
    print("Original list:", games)

    # Insert a value at the beginning of the list.
    insert_at(games, 0, "DOOM")
    print("After inserting at the beginning:", games)

    # Insert a value near the middle of the list.
    insert_at(games, 2, "Cyberpunk 2077")
    print("After inserting in the middle:", games)

    # Insert a value at the end of the list.
    insert_at(games, len(games), "Red Dead Redemption 2")
    print("After inserting at the end:", games)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Delete the first item.
    removed = delete_at(games, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", games)

    # Delete an item from the middle.
    middle_index = len(games) // 2
    removed = delete_at(games, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", games)

    # Delete the final item.
    removed = delete_at(games, len(games) - 1)
    print("Removed from end:", removed)
    print("Updated list:", games)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a value that is currently in the list.
    search_item = "Minecraft"
    result = search_value(games, search_item)
    print(f"{search_item} was found at index:", result)

    # Search for a value that is not in the list.
    search_item = "Elden Ring"
    result = search_value(games, search_item)
    print(f"{search_item} search result:", result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Attempt to delete using an invalid index.
    invalid_delete = delete_at(games, 100)
    print("Deleting with invalid index:", invalid_delete)

    # Edge case 2: Insert into an empty list.
    empty_list = []
    insert_at(empty_list, 0, "First Item")
    print("Insert into empty list:", empty_list)

    # Edge case 3: Attempt to delete from an empty list.
    empty_list = []
    empty_delete = delete_at(empty_list, 0)
    print("Deleting from empty list:", empty_delete)


if __name__ == "__main__":
    main()