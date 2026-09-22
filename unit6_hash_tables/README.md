# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

## Implementation Summary

For this assignment, I created a Python dictionary to demonstrate how dictionaries can be used like hash tables. I added multiple SKU and quantity key-value pairs and demonstrated insert, lookup, update, and delete operations.

I tested successful lookups using existing keys and showed how assigning a new value to an existing key updates the stored value. I also removed an existing key-value pair and displayed the dictionary before and after the deletion.

For edge cases, I tested looking up a missing key using get(), which safely returned None, and I checked whether a missing key existed before attempting to delete it. This prevented the program from causing an error.

For the real-world scenario, I used an inventory system where product SKU numbers were used as keys and inventory quantities were stored as values. This demonstrated how hash tables can provide fast access to stored information.