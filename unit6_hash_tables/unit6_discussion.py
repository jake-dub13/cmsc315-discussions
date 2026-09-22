"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # A Python dictionary behaves like a hash table by storing
    # key-value pairs and using the key to quickly locate its value.
    inventory = {}

    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"] = 22
    inventory["P400"] = 7
    inventory["P500"] = 30

    print("\n=== INSERT OPERATIONS ===")
    print("Inventory after adding items:")
    print(inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Dictionary values can be retrieved directly using their keys.
    print("P100 quantity:", inventory["P100"])
    print("P300 quantity:", inventory["P300"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:")
    print(inventory)

    # Assigning a new value to an existing key replaces its old value.
    inventory["P100"] = 20

    print("After updating P100:")
    print(inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:")
    print(inventory)

    # Removing a key also removes the value associated with that key.
    del inventory["P200"]

    print("After deleting P200:")
    print(inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: get() safely returns None if the key does not exist.
    missing_value = inventory.get("P999")
    print("Lookup for missing P999:", missing_value)

    # Edge case 2: check for a key before trying to delete it.
    if "P999" in inventory:
        del inventory["P999"]
    else:
        print("P999 could not be deleted because it does not exist.")

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD INVENTORY EXAMPLE ===")

    # An inventory system can use the SKU as the key and quantity as the value.
    sku = "P400"
    print("Quantity available for", sku, ":", inventory.get(sku))


if __name__ == "__main__":
    main()