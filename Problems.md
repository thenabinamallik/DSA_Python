# Class and Objects <br>
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