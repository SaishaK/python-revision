class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, elements):
        self.elements.append(elements)
    
    def pop(self):
        if len(self.elements) == 0:
            return ("Underflow")
        return self.elements.pop(-1)
    
    def display(self):
        print(self.elements)

stack1 = Stack()

stack1.push(5)
stack1.push(14)
stack1.push(20)
stack1.display()

stack1.pop()
stack1.display()