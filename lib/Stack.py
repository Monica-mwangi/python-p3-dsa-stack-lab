class Stack:
    """
    A basic stack implementation with limited size and search functionality.
    """

    def __init__(self, items=None, limit=100):
        """
        Initializes a stack with optional initial items and a size limit.

        Args:
            items (list, optional): A list of items to populate the stack. Defaults to None.
            limit (int, optional): The maximum number of elements allowed in the stack. Defaults to 100.
        """
        if items is None:
            self.items = []
        else:
            self.items = items
        self.limit = limit

    def isEmpty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Pushes an item onto the stack if there's space.

        Args:
            item: The item to be added to the stack.

        Returns:
            bool: True if successful, False if stack is full.
        """
        if len(self.items) < self.limit:
            self.items.append(item)
            return True
        else:
            return False

    def pop(self):
        """
        Removes and returns the top element from the stack if not empty.

        Returns:
            mixed: The top element or None if empty.
        """
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        """
        Returns the top element of the stack without removing it.

        Returns:
            mixed: The top element or None if empty.
        """
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        """
        Returns the current number of elements in the stack.

        Returns:
            int: The stack size.
        """
        return len(self.items)

    def full(self):
        """
        Checks if the stack has reached its maximum capacity.

        Returns:
            bool: True if full, False otherwise.
        """
        return len(self.items) == self.limit

    def search(self, target):
        """
        Searches for the target element in the stack and returns its distance
        from the top (index position).

        Returns:
            int: The distance from the top of the stack if found, -1 otherwise.
        """
        try:
            index = self.items.index(target)  # Find the index of the target
            return len(self.items) - index - 1  # Calculate distance from top
        except ValueError:
            return -1  # Target not found
