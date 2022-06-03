class Person:
  def __init__(self, name):
    self.name = name

  def GetName(self):
    print( self.name)
class Employee (Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

    def GetSalary(self):
        print( self.salary)

class Manager (Employee):
    def __init__(self, name,salary):
        super().__init__(name,salary)

class Worker (Employee,Manager):
    def __init__(self, name,salary,nameManager,salaryManager):
        Employee.__init__(name,salary)
        Manager.__init__(nameManager,salaryManager)

    def GetManager(self):
        Manager().GetName()

class Tester (Worker):
    def __init__(self, name,salary):
        Worker.__init__(name,salary)
    def Test(self):
        print( "Testing()")

class Programmer (Worker):
    def __init__(self, name,salary):
        Worker.__init__(name,salary)
    def Code(self):
        print( "code()")


p1 = Person("osoba")
p1.GetName()
p2= Employee("Employeetest",16)
p2.GetName()
p2.GetSalary()
p3=Manager("Managertest",22)
p3.GetName()
p3.GetSalary()
p4=Worker("Workertest",22)
p4.GetManager()
programing= Programmer(p4)
programing.Code()
testing=Tester(p4)
testing.Test()
