from LinkedList import LinkedList

ll = LinkedList()
print("LinkedList:", ll)
print("LL:", ll)
print("size: %d, is_empty: %r, contains 1: %r\n" % (ll.size(), ll.is_empty(), ll.contains(1)))

ll.insert(1)
print("LL:", ll)
print("size: %d, is_empty: %r, contains 1: %r\n" % (ll.size(), ll.is_empty(), ll.contains(1)))

ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
print("LL:", ll)
print("size: %d, is_empty: %r, contains 1: %r\n" % (ll.size(), ll.is_empty(), ll.contains(1)))

ll.remove_all(1)
print("LL:", ll)
print("size: %d, is_empty: %r, contains 1: %r\n" % (ll.size(), ll.is_empty(), ll.contains(1)))