# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

* Stack (LIFO)
* Queue (FIFO)

## Learning Objectives

* Implement stack operations
* Implement queue operations
* Understand LIFO and FIFO behavior
* Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.



# Implementation Summary



I implemented a `Stack` class using a Python list and a `Queue` class using `collections.deque`. The stack included methods for pushing, popping, peeking, and checking whether the stack was empty. The queue included methods for enqueueing, dequeueing, viewing the front item, and checking whether the queue was empty.

I demonstrated LIFO behavior by adding four browser pages to the stack and removing them in reverse order. I demonstrated FIFO behavior by adding four customers to the queue and removing them in the same order they were added.

I also tested edge cases for both data structures. The program handled attempts to pop or peek from an empty stack and attempts to dequeue or view the front of an empty queue by returning None. I also tested single-item stacks and queues and verified that each became empty after its only item was removed.

Using deque for the queue provided efficient removal from the front, while the Python list worked well for stack operations at the end of the list.



