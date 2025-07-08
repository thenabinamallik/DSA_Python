class Node: #Node to store the item and next node's reference
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start=start

    def show(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
   
    def isEmpty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        node = Node(data,self.start)
        self.start=node

    def inser_after(self, target, data):
        if target is not None:
            temp = self.search(target)
            node = Node(data, temp.next)
            temp.next = node
        
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item is data:
                return temp
            temp = temp.next
        return None

    def insert_at_last(self, data):
        node = Node(data)
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = node
    
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    
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

    def delete_item(self, target):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item is target:
                self.start = None
        else:
            temp = self.start
            while temp is not None:
                if temp.next.item is target:
                    temp.next = temp.next.next
                    break
                temp = temp.next





myList = SLL()
myList.insert_at_start(20)
myList.insert_at_start(30)
myList.insert_at_start(40)
myList.insert_at_last(50)
myList.inser_after(40, 80)
print(myList.search(20))

myList.delete_first()
myList.delete_last()
myList.delete_item(30)

myList.show()