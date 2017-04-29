class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Empty stack; nothing to pop."

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return "Empty stack; nothing to peek at."

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def __str__(self):
        if self.isEmpty():
            return "Empty stack."
        else:
            result = ""
            for s in self.items:
                result += str(s) + ", "
            return "Bottom -> %s -> Top" % result[0:-2]