from Stack import Stack

s = Stack()

print("Pushing 1 onto the stack.")
s.push(1)

print("Popping %s off of the stack." % str(s.pop()))
print("Attempting to pop again: %s" % str(s.pop()))