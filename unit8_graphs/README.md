# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

## Implementation Summary

For this assignment, I implemented Breadth-First Search in Python using an adjacency list and a queue. I created a graph that represented a streaming recommendation network where each movie was a node and the connections between movies represented similar content.

The BFS function used a queue to visit nodes level by level and a visited set to prevent the same node from being processed more than once. I tested the traversal starting from Movie A and then added Movie G to demonstrate how the traversal changed after the graph was updated.

I also tested several edge cases. A missing starting node returned an empty list, a single-node graph returned only that node, and I tested BFS starting from a different node.

BFS is useful when nearby connections should be explored before deeper ones. In a recommendation system, this could help find content that is closely related to a user's current interests before exploring more distant connections.

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   