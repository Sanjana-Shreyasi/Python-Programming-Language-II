#Queue
#Develop a queue implementation using Python's deque from the collection's module. Add a method, safe_dequeue(),that removes the front
#element from the queue. If the queue is empty, the method should print a message as, "Queue is empty, cannot dequeue."

from collections import deque

class Queue:
    def __init__(self):
        self.queue=deque()

    #Enqueue (add element to rear)
    def enqueue(self,item):
        self.queue.append(item)
        print(f"{item} added to queue")

    # Safe dequeue (remove from front)
    def safe_dequeue(self):
        if len(self.queue)==0:
            print("Queue is empty, cannot dequeue.")
        else:
            return self.queue.popleft()
        
    #Display queue
    def display(self):
        print("Queue:",list(self.queue))

#Example usage
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print("Dequeued:",q.safe_dequeue())
print("Dequeued:",q.safe_dequeue())
print("Dequeued:",q.safe_dequeue())

