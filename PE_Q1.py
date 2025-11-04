class Model:
    def __init__(self,n,m,y):
        self.year = y
        self.month = m
        self.name = n
    def display(self):
        print(f"{self.name} - {self.month} - {self.year}")
class Node:
    def __init__(self,model):
        self.data = model
        self.next = None

class LLMLinkedListManager:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def add_to_tail(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode
    def delete_by_name(self,name):
        if self.isEmpty():
            print("list is empty")
            return
        if self.head.data.name == name:
            if self.head == self.tail:
                self.head = self.tail = None
                return
            current = self.head
            del self.head
            self.head = current.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data.name == name:
                current.next = current.next.next
                break
            current = current.next
        if current.next == self.tail:
            self.tail == current.next
    def sort_by_year(self):
        n1 = self.head
        while n1 != self.tail:
            n2 = n1.next
            while n2 != None:
                if n1.data.year > n2.data.year:
                    n1.data, n2.data = n2.data, n1.data
                n2 = n2.next
            n1 = n1.next
    def display(self):
        if self.isEmpty():
            print("list is empty")
            return
        current = self.head
        while current is not None:
            current.data.display()
            current = current.next

if __name__ == "__main__":
    sList = LLMLinkedListManager()
    sList.add_to_tail(Model("FlAN", 9, 2021))
    sList.add_to_tail(Model("BERT", 10, 2018))
    sList.add_to_tail(Model("Trans", 6, 2017))
    sList.add_to_tail(Model("Chatgpt", 11, 2022))
    sList.add_to_tail(Model("GPT-3", 5, 2020))
    sList.add_to_tail(Model("DeepSeek", 1, 2024))
    sList.display()
    sList.sort_by_year()
    print("After sort: ")
    sList.display()