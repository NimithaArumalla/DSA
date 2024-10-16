class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if self.isEmpty():
            return "empty"
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "empty"
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
    
myq=Queue()
myq.enqueue(20)
myq.enqueue(9)
myq.enqueue(93)
print(myq.dequeue())
print(myq.peek())
print(myq.isEmpty())
print(myq.size())