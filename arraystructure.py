class Node:
    def __init__(self,x):
        self.data = x
class ArrayStructure:
    def __init__(self,cap = 10):
        self.capacity = cap
        self.length = 0
        self.arrayNodes = [None]*cap
    def isfull(self):
        return self.capacity==self.length
    def isEmpty(self):
        return self.length==0
    def increaseCap(self):
        newCap = self.capacity*2
        newArray = [""]*newCap
        for i in range(self.length):
            newArray[i] = self.arrayNodes[i]
        self.arrayNodes = newArray
        self.capacity = newCap
    def insertLast(self,x):
        if self.isfull():
            self.increaseCap()
        self.arrayNodes[self.length]=Node(x)
        self.length+=1
    def insertFirst(self,x):
        if self.isfull():
            self.increaseCap()
        for i in range(self.length,0,-1):
            self.arrayNodes[i] = self.arrayNodes[i-1]
        self.arrayNodes[0] = Node(x)
        self.length+=1
    def removeLast(self):
        if self.isEmpty():
            print("empty")
            return
        self.arrayNodes[self.length-1] = Node("")
        self.length-=1
    def removeFirst(self):
        if self.isEmpty():
            print("empty")
            return
        for i in range(self.length-1):
            self.arrayNodes[i] = self.arrayNodes[i+1]
        self.arrayNodes[self.length-1] = None
        self.length-=1
    def removeAt(self, idx):
        for i in range(idx,self.length-1):
            self.arrayNodes[i] = self.arrayNodes[i+1]
        self.arrayNodes[self.length-1] = None
        self.length-=1
    def display(self):
        for i in range(self.length):
            print(self.arrayNodes[i].data, end=" ")
        print()
if __name__ == "__main__":
    aStruct = ArrayStructure(2)
    aStruct.insertLast(1000)
    aStruct.insertLast(4)
    aStruct.insertLast(4)
    aStruct.insertLast(5)
    aStruct.insertLast(10000)
    aStruct.removeLast()
    aStruct.removeFirst()
    aStruct.removeAt(1)
    aStruct.display()