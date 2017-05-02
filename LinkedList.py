from ListNode import ListNode


class LinkedList:
    def __init__(self):
        """
        Initializes the "head" of the LinkedList.
        """

        self.head = None

    def insert(self, data):
        """
        Inserts <data> at the end of the LinkedList.
        
        :param data: The value being added
        """

        if self.head is None:
            self.head = ListNode(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = ListNode(data)

    def remove(self, d):
        """
        Removes the first ListNode containing <d>.
        
        :param d: The value being removed
        """

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
        """
        Removes all ListNodes containing <d>.
        
        :param d: The value being removed
        """

        # Removes leading <d>'s by moving self.head
        while self.head is not None and self.head.data == d:
            self.head = self.head.next

        # Removes following <d>'s by traversing the LinkedList
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == d:
                    temp.next = temp.next.next
                else:
                    temp = temp.next

    def contains(self, d):
        """
        Checks if the LinkedList contains <d>.
        
        :param d: The value being searched for
        :return: True if found, False if not (boolean)
        """

        temp = self.head
        while temp is not None:
            if temp.data == d:
                return True
            else:
                temp = temp.next

        return False

    def size(self):
        """
        Counts the size of the LinkedList.
        
        :return: The size of the LinkedList (int)
        """

        count = 0

        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next

        return count

    def is_empty(self):
        """
        Checks if the LinkedList is empty.
        
        :return: True if empty, False if not (boolean)
        """

        return self.head is None

    def to_list(self):
        """
        Creates a list version of the LinkedList.
        
        :return: A list of the values (list)
        """

        result = []

        temp = self.head
        while temp is not None:
            result.append(temp.data)
            temp = temp.next

        return result

    def __str__(self):
        """
        Formatted string representation of the LinkedList.
        
        :return: Each value with ASCII arrows between them (string)
        """

        result = ""

        temp = self.head
        while temp is not None:
            result += str(temp.data) + " -> "
            temp = temp.next

        return result[0:-4]