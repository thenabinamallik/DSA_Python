# 1 - Class and Objects <hr>
### Create a class Employee with attributes empid, name, salary and also define methods to ccess properties of Employee.
```Python

class Employee:
    def __init__(self,empid=None, name=None, salary=None):
        self.empid = empid
        self.name = name
        self.salary = salary

    def setEmpid(self, empid):
        self.empid = empid
    def setName(self, name):
        self.name = name
    def setSalary(self, salary):
        self.salary = salary

    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    

e1 = Employee()
e2 = Employee(2,"Mallik",150000)
e1.setEmpid(1)
e1.setName("Nabina")
e1.setSalary(200000)

print(e1.getEmpid(), e1.getName(), e1.getSalary())
print(e2.getEmpid(), e2.getName(), e2.getSalary())
```
#### Output
```
1 Nabina 200000
2 Mallik 150000
```

<br>

# 2 - Singly Linked List <hr>
### Create a Singly Linked List and perform insert_at_start(), insert_at_last(), insert_after() and Print_list() function along with deletes
```python

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
```
#### Output
```
230 30 20 
230 30 20 
```
