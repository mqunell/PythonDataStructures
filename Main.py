'''from Stack import Stack

s = Stack()

print("Pushing 1 and 2 onto the stack.")
s.push(1)
s.push(2)

print("Peeking at the stack: %s" % str(s.peek()))
print("Popping %s off of the stack." % str(s.pop()))
print("Peeking at the stack: %s" % str(s.peek()))
print("Popping %s off of the stack." % str(s.pop()))
print("Attempting to peek again: %s" % str(s.peek()))'''

from Queue import Queue

q = Queue()

q.add("first")
q.add("second")
print(q)
q.remove()
print(q)
q.remove()
print(q)