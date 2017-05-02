from ListNode import ListNode


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = ListNode(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = ListNode(data)

    def remove(self, d):
        if self.head is not None:
            if self.head.data == d:
                self.head = self.head.next
            else:
                temp = self.head
                while temp.next is not None:
                    if temp.next.data == d:
                        temp.next = temp.next.next
                        break
                    else:
                        temp = temp.next

    def remove_all(self, d):
        # Removes leading d's by moving self.head
        while self.head is not None and self.head.data == d:
            self.head = self.head.next

        # Removes following d's by traversing the LinkedList
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == d:
                    temp.next = temp.next.next
                else:
                    temp = temp.next

    def contains(self, d):
        temp = self.head
        while temp is not None:
            if temp.data == d:
                return True
            else:
                temp = temp.next

        return False

    def size(self):
        count = 0

        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next

        return count

    def is_empty(self):
        return self.head is None

    def to_list(self):
        result = []

        temp = self.head
        while temp is not None:
            result.append(temp.data)
            temp = temp.next

        return result

    def __str__(self):
        result = ""

        temp = self.head
        while temp is not None:
            result += str(temp.data) + " -> "
            temp = temp.next

        return result[0:-4]