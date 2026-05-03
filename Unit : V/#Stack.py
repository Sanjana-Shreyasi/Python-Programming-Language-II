#Stack
#Creata a program that implements a stack using a list. Add a method, safe_pop(), which safely removes the top element from the stack. If 
# the stack is empty, the method should handle this condition by : 
#1) Printing a message as "Stack is empty, nothing to pop."
#2) Returning None.

class stack:
    def __init__(self):
        self.stack=[]

    #Push element onto stack
    def Push(self,Item):
        self.stack.append(Item)
        print(f"{Item} pushed to stack")

    #Safe pop method
    def Safe_pop(self):
        if len(self.stack)==0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.stack.pop()
        
    #Display Stack
    def Display (self):
        print("Stack:",self.stack)

#Example usage
S=stack()
S.Push(10)
S.Push(20)
S.Push(30)
S.Display()
print("Popped:",S.Safe_pop())
print("Popped:",S.Safe_pop())
print("Popped:",S.Safe_pop())

#Trying to pop from empty stack
print("Popped:",S.Safe_pop())
