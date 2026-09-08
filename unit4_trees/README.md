# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Implementation Summary

I implemented a Binary Search Tree in Python using recursive insertion, searching, and in-order traversal. The tree stored smaller values in the left subtree and larger values in the right subtree, which allowed the program to reduce the search space after each comparison.

I inserted seven values into the tree and created both left and right subtrees. I then performed an in-order traversal, which returned the values in sorted order because the traversal visits the left subtree, the current node, and then the right subtree.

For searching, I tested two values that were present in the tree and two values that were missing. The recursive search followed only the subtree where the target value could exist instead of checking every value sequentially.

I also tested several edge cases. Searching an empty tree returned False, traversing an empty tree returned an empty list, and duplicate values were ignored. These tests showed how the BST handled unusual conditions without causing errors.