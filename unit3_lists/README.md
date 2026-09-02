# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Implementation Summary

I implemented list insertion, deletion, and searching operations in Python. The program tested insertion at the beginning, middle, and end of a list and displayed how the list changed after each operation. I also tested deletion from the beginning, middle, and end while returning the removed value.

For searching, I used a linear search that checked each element in sequence until the value was found. The search returned the matching index when successful and returned -1 when the value was missing.

I also tested several edge cases, including deleting with an invalid index, inserting into an empty list, and deleting from an empty list. Invalid deletions returned None instead of causing an error.

The program used a video game list as a real-world example. This demonstrated how list operations can be used to add, remove, and locate items while also showing how insertion and deletion may require elements to shift depending on where the operation occurs.