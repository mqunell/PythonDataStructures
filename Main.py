from LinkedList import LinkedList

ll = LinkedList()
ll.insert(1)
ll.insert(2)
print("LinkedList after inserts:", ll)
ll.remove(1)
ll.remove(2)
ll.remove(5)
ll.remove(1)
print("LinkedList after removes:", ll)