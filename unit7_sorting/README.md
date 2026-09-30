# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

## Implementation Summary

For this assignment, I implemented Bubble Sort and Merge Sort in Python and tested both algorithms using multiple datasets. Bubble Sort compared neighboring values and swapped them when they were out of order. Merge Sort used recursion to divide the list into smaller sections and then merged the sorted sections back together.

I tested both algorithms on two different unsorted datasets and confirmed that they produced the same sorted results. I also tested edge cases including an empty list, an already sorted list, and a list containing duplicate values.

For the real-world example, I used movie popularity scores from a streaming platform. Merge Sort was used to organize the scores in ascending order.

Merge Sort is generally more efficient for large datasets because its typical time complexity is O(n log n), while Bubble Sort is generally O(n²). Bubble Sort can still be useful for small or nearly sorted datasets because it is simple and can stop early when no swaps are needed.