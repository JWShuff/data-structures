class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
    def __init__(self, stack = [], total = None):
        self.stack = stack
        if len(self.stack) > 0:
            self.total = len(self.stack)
        self.total = total

    def push(self, data):
        # write your code to add data following LIFO and return the Stack
        self.stack.push(data)
        self.total = len(self.stack)
        return self.stack
    
    def pop(self, data):
        # write your code to removes the data following LIFO and return the Stack
        self.stack.pop(0)
        self.total = len(self.stack)
        return self.stack

    def size(self):
        # write your code that returns the size of the Stack
        return len(self.stack)
