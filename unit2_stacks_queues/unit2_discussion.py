"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New values are added to the end of the list, which becomes the top of the stack.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek returns the most recently added value without changing the stack.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values are added to the back so older values remain at the front.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front returns the oldest value without removing it from the queue.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding four browser pages to the stack:")
    stack.push("Home Page")
    stack.push("News Page")
    stack.push("Sports Page")
    stack.push("Weather Page")

    print("Current top value:", stack.peek())

    print("\nRemoving values to demonstrate LIFO behavior:")
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())
    print("Removed:", stack.pop())

    print("\nAttempting to pop from an empty stack:")
    print("Result:", stack.pop())

    print("Attempting to peek at an empty stack:")
    print("Result:", stack.peek())

    single_stack = Stack()
    single_stack.push("Only Item")
    print("\nSingle-item stack before removal is empty:", single_stack.is_empty())

    single_stack.pop()
    print("Single-item stack after removal is empty:", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding four customers to the queue:")
    queue.enqueue("Customer A")
    queue.enqueue("Customer B")
    queue.enqueue("Customer C")
    queue.enqueue("Customer D")

    print("Current front value:", queue.front())

    print("\nRemoving values to demonstrate FIFO behavior:")
    print("Removed:", queue.dequeue())
    print("Removed:", queue.dequeue())
    print("Removed:", queue.dequeue())
    print("Removed:", queue.dequeue())

    print("\nAttempting to dequeue from an empty queue:")
    print("Result:", queue.dequeue())

    print("Attempting to view the front of an empty queue:")
    print("Result:", queue.front())

    single_queue = Queue()
    single_queue.enqueue("Only Customer")
    print("\nSingle-item queue before removal is empty:", single_queue.is_empty())

    single_queue.dequeue()
    print("Single-item queue after removal is empty:", single_queue.is_empty())


if __name__ == "__main__":
    main()