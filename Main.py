from LinkedList import LinkedList

ll = LinkedList()
test_value = 2

print("LL:", ll)
print(str(ll.to_list()))
print("size: %d, is_empty: %r, contains %d: %r\n" % (ll.size(), ll.is_empty(), test_value, ll.contains(test_value)))

ll.insert(1)
print("LL:", ll)
print(str(ll.to_list()))
print("size: %d, is_empty: %r, contains %d: %r\n" % (ll.size(), ll.is_empty(), test_value, ll.contains(test_value)))

ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(1)
ll.remove(2)
ll.insert(2)
print("LL:", ll)
print(str(ll.to_list()))
print("size: %d, is_empty: %r, contains %d: %r\n" % (ll.size(), ll.is_empty(), test_value, ll.contains(test_value)))

ll.remove_all(1)
print("LL:", ll)
print(str(ll.to_list()))
print("size: %d, is_empty: %r, contains %d: %r\n" % (ll.size(), ll.is_empty(), test_value, ll.contains(test_value)))
