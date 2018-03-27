"You will have to import the Stack class to use it in your implementation"
from util import Stack

toEnqueue = [1,2,3,4,5]

class QueueTheStack:
    "A container with a first-in-first-out (FIFO) queuing policy."   
    def __init__(self):
        "add adequate number of stacks here"
        "*** WRITE CODE HERE ***"
        self.s1=Stack()
        self.s2=Stack()

    def push(self,item):
        "Enqueue the 'item' into the queue"
        "*** WRITE CODE HERE ***"
        self.s1.push(item)
        
    def pop(self):
        "dequeue the 'item' from the queue"
        "*** WRITE CODE HERE ***"
        if (self.s2.isEmpty()):
            while not (self.s1.isEmpty()):
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def isEmpty(self):
        "returns true if the queue is empty"
        "***WRITE CODE HERE***"
        if (self.s2.isEmpty()):
            return self.s1.isEmpty()
        else:
            return self.s2.isEmpty()



#MAIN Method
if __name__ == '__main__':

    myQueue = QueueTheStack()
    "This will enqueue the whole list."
    for i in toEnqueue:
        myQueue.push(i)

    "This should print the queue.. in order : 12345"
    for i in range(0,len(toEnqueue)):
        print myQueue.pop()
    


