class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        return self.items == []

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of the Queue"

    def peek(self):
        if self.isEmpty():
            return "There are no elements in the Queue"
        else:
            return self.items[0]

    def delete(self):
        self.items = []


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()
print(customQueue.peek())