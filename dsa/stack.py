class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    
mystack=Stack()

mystack.push(3)
mystack.push(2)
mystack.push(7)
mystack.push(9)
mystack.push(6)
print(mystack.stack)
print(mystack.pop())
print(mystack.peek())
print(mystack.isEmpty())
print(mystack.size())

    