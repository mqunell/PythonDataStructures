class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Empty stack; nothing to pop."
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Empty stack; nothing to peek at."
        else:
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def __str__(self):
        if self.is_empty():
            return "Empty stack."
        else:
            result = ""
            for s in self.items:
                result += str(s) + ", "
            return "Bottom -> %s -> Top" % result[0:-2]