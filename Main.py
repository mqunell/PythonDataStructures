from LinkedList import LinkedList

ll = LinkedList()
ll.insert(1)
ll.insert(1)
ll.insert(1)
ll.insert(1)
ll.insert(0)
print("LinkedList after inserts:", ll)
ll.remove_all(1)
print("LinkedList after removes:", ll)