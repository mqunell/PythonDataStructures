from Stack import Stack

s = Stack()

print("Stack is empty?: %s" % str(s.isEmpty()))
print("Pushing 1, 2, and 3 onto the stack.")
s.push(1)
s.push(2)
s.push(3)
print("Stack is empty?: %s" % str(s.isEmpty()))

print(s)
print("Top of the stack: " + str(s.peek()))
print("Popping " + str(s.pop()) + " from the stack")
print("Popping %s from the stack." % str(s.pop()))
print(s)