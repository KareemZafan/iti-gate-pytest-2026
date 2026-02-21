
class MyStack:
    def __init__(self): 
        self.items = []
    
    def is_stack_empty(self): 
        return len(self.items) == 0
    
    def push(self, item): 
        self.items.append(item)

    def pop(self):
        if self.is_stack_empty():
            raise ValueError("Stack is empty")
        return self.items.pop()
    
    def get_stack_peek(self):
        if self.is_stack_empty():
            raise ValueError("Stack is empty")
        return self.items[-1]
    
    def get_stack_size(self):
        return len(self.items)
    
    def get_stack_elements(self):
        return self.items