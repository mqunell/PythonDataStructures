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
        if self.head is None:
            " do nothing "
        elif self.head.data == d:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == d:
                    temp.next = temp.next.next
                    break
                temp = temp.next

    def __str__(self):
        result = ""

        temp = self.head
        while temp is not None:
            result += str(temp.data) + " -> "
            temp = temp.next

        return result[0:-4]