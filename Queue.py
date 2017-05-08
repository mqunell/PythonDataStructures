class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        if self.is_empty():
            self.items.append(item)
        else:
            # Append the last item to the end
            self.items.append(self.items[-1])

            # Shift the items right
            for i in range(len(self.items) - 2, 0, -1):
                self.items[i] = self.items[i-1]

            # Put the new item in index 0
            self.items[0] = item

    def remove(self):
        if self.is_empty():
            return "Empty queue; nothing to remove."
        else:
            temp = self.items[-1]
            self.items = self.items[0:-1]
            return temp

    def element(self):
        if self.is_empty():
            return "Empty queue; nothing to element."
        else:
            return self.items[-1]

    def contains(self, d):
        return self.items.__contains__(d)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def __str__(self):
        if self.is_empty():
            return "Empty queue."
        else:
            result = ""
            for i in self.items:
                result += str(i) + ", "
            return "Back -> %s -> Front" % result[0:-2]