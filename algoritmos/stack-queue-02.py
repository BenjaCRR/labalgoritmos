stack=[]
#push
stack.append("Tung")
stack.append("Tung")
stack.append("Tung")
stack.append("Sahur")
print(stack)
#Size
size=len(stack)
print("size: ",size)
#Pop
stack.pop()
stack.pop()
print("pop: ",stack)

#enqueue
stack.append("Tung")
stack.append("Tung")
stack.append("Tung")
stack.append("Sahur")
print("enuqeue: ", stack)
#dequeue
stack.pop(0)
stack.pop(0)
print("final: ",stack)


#punto 2-b


class Stack:
    stack=[]
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

myStack = Stack()

myStack.push('Horacio')
myStack.push('el')
myStack.push('Brawler')
print("Stack: ", myStack.stack)

print("Pop: ", myStack.pop())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.isEmpty())

print("Size: ", myStack.size())

print("Stack: ", myStack.stack)
class Queue:
    stack=[]
    def enqueue(self, element):
        self.stack.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
myStack = Queue()

myStack.enqueue('Horacio')
myStack.enqueue('el')
myStack.enqueue('Brawler')
print("Stack: ", myStack.stack)

print("Pop: ", myStack.dequeue())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.isEmpty())

print("Size: ", myStack.size())

print("Stack: ", myStack.stack)