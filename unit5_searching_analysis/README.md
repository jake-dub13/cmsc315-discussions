# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

## Implementation Summary

I implemented both linear search and binary search in Python and tested them using small and large sorted datasets. The linear search checked each value from the beginning of the list until the target was found or the end of the list was reached. The binary search repeatedly checked the middle value and eliminated half of the remaining search area after each comparison.

I tested both algorithms on a small dataset by searching for a value that existed and a value that was missing. Both searches returned the correct index when the value was found and returned -1 when the value was not present.

I also tested both algorithms on a dataset containing 10,000 values. Both returned the same correct result, but binary search was more efficient because it reduced the remaining search space by half during each step instead of checking values one at a time.

For edge cases, I tested an empty list and a single-element list. Both search methods returned -1 for the empty list and correctly returned index 0 when the single value was found.

The real-world example used a sorted list of product ID numbers. Both linear and binary search successfully located the requested product ID. This demonstrated that linear search can still be useful for small or unsorted datasets, while binary search is better suited for large sorted datasets.