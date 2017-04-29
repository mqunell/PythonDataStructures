class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

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