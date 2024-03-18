class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        
        self.s1.append(x)

    def dequeue(self):
        
        if len(self.s2) > 0:
           
            return self.s2.pop()

       
        else:
           
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())

            
            return self.s2.pop()



q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  
print(q.dequeue())  
print(q.dequeue())  

