class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        if self.isEmpty():
            self.items.append(item)
        else:
            # Append the last item to the end
            self.items.append(self.items[-1])

            # Shift the items right
            for i in range(len(self.items) - 2, 0, -1):
                self.items[i] = self.items[i-1]

            # Put the new item in index 0
            self.items[0] = item

    def isEmpty(self):
        return self.items == []

    def __str__(self):
        return str(self.items)

# add(item)
# remove
# element
# size
# isEmpty
# __str__