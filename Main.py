from Stack import Stack
from Queue import Queue

s = Stack()
s.push(1)
s.push(2)
s.push(3)

q = Queue()
q.add(1)
q.add(2)
q.add(3)

print("Stack 'contains' tests: %r, %r, %r, %r" % (s.contains(0), s.contains(1), s.contains(2), s.contains(3)))
print("Queue 'contains' tests: %r, %r, %r, %r" % (q.contains(0), q.contains(1), q.contains(2), q.contains(3)))

s.pop()
s.pop()
s.pop()
print("Empty stack 'contains' test: %r" % s.contains(4))

q.remove()
q.remove()
q.remove()
print("Empty queue 'contains' test: %r" % q.contains(4))
