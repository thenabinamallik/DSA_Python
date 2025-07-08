 #Agenda
'''
1 -  What is a list ?
    :- List is linear collection of data items also known as List Item.
     
2 - What is a Node ?
3 - defining a Node ?
4 - Singly Linked List
    :- SLL is a linear data structure
    :- It can grow and shrink

5 - Elementary Operations
    :- Insertion
    :- Deletion
    :- Traverse
    :- is_Empty
'''

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next
    
class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_Empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        node =  Node(data,self.start)
        self.start = node

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

    def insert_after(self,target, data):
        if target is not None:
            temp = self.search(target)
            node = Node(data,temp.next)
            temp.next = node

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def insert_at_last(self, data):
        node = Node(data)
        if not self.is_Empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.start = node

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            
            temp = temp.next
        return None
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

    def __iter__(self):
        return SLLIterator(self.start)
    
class SLLIterator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

myList = SLL()

myList.insert_at_start(20)
myList.insert_at_start(220)
myList.insert_at_start(230)
myList.insert_after(220,30)
myList.insert_at_start(250)
myList.insert_at_last(555)

myList.delete_first()
myList.delete_last()
myList.delete_item(220)

myList.print_list()
print()
for x in myList:
    print(x, end=' ')