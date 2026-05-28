stack = []

print("Stack: ", stack)

stack.append(5)
stack.append(3)

print("Stack: ", stack)
element = stack.pop()
print("Pop: ", element)
print("stack: ", stack)

stack.append(2)
stack.append(8)

print("stack: ", stack)

element = stack.pop()
print("Pop: ", element)
element = stack.pop()
print("Pop: ", element)

print("stack: ", stack)

stack.append(9)
stack.append(1)

print("stack: ", stack)

element = stack.pop()
print("Pop: ", element)


stack.append(7)
stack.append(6)

print("stack: ", stack)

element = stack.pop()
print("Pop: ", element)
element = stack.pop()
print("Pop: ", element)

print("stack: ", stack)

stack.append(4)

print("stack: ", stack)

element = stack.pop()
print("Pop: ", element)
element = stack.pop()
print("Pop: ", element)

print("stack final: ", stack)
size = len(stack)
print("Size: ", size)
