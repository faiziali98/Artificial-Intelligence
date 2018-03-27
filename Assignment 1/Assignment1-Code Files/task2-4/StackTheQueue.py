
"You will have to import the Queue class to use it in your implementation"
from util import Queue

toStack = [1,2,3,4,5]

class StackTheQueue:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        "Add Adequate queues!"
        "*** WRTIE CODE HERE ***"
        self.q1=Queue()
        self.q2=Queue()

    def push(self,item):
        "Push 'item' onto the stack"
        "*** WRTIE CODE HERE ***"
        if (self.q1.isEmpty()):
            self.q1.push(item)
            while not (self.q2.isEmpty()):
                self.q1.push(self.q2.pop())
        else:
            self.q2.push(item)
            while not (self.q1.isEmpty()):
                self.q2.push(self.q1.pop())

    def pop(self):
        "Pop the most recently pushed item from the stack"
        "*** WRTIE CODE HERE ***"
        if (self.q1.isEmpty()):
            return self.q2.pop()
        else:
            return self.q1.pop()
        
    def isEmpty(self):
        "Returns true if the queue is empty"
        "*** WRTIE CODE HERE ***"
        return self.q1.isEmpty() and self.q2.isEmpty()
                

if __name__ == '__main__':

    myStack = StackTheQueue()

    #Push all values onto the stack
    for i in toStack:
        myStack.push(i)

    #Pop all the entered values...
    #This should print values in toStack in descending order: 54321!
    for i in range(0,len(toStack)):
        print myStack.pop()
