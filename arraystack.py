from arraystructure import *
class ArrayStack(ArrayStructure):
    def __init__(self):
        super().__init__(1)
    def push(self,x):
        self.insertLast(x)
    def pop(self,x):
        self.removeLast()
    def top(self):
        if self.isEmpty():
            print("empty")
            return None
        return self.arrayNodes[self.length-1].data
astack = ArrayStack()
for i in range(10):
   astack.push(i)
astack.removeLast()
astack.display()
print(astack.top())