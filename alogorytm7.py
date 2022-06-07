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

class Worker (Employee):
    def __init__(self, name,salary,Manager):
        Employee.__init__(self,name,salary)
        self.Manager = Manager

    def GetManager(self):
        self.Manager.GetName()

class Tester (Worker):
    def __init__(self, name,salary,Manager):
        Worker.__init__(self, name,salary,Manager)
    def Test(self):
        print( "Testing()")

class Programmer (Worker):
    def __init__(self, name,salary,Manager):
        Worker.__init__(self, name,salary,Manager)
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
p4=Worker("Workertest",22,p3)
p4.GetManager()
programing= Programmer("Programmer",22,p3)
programing.Code()
testing=Tester("Tester",22,p3)
testing.Test()
testing.GetManager()
programing.GetManager()

import random


class Card:    
    def __init__(self, value, znak):
        self.value = value
        self.znak = znak
    def __str__(self):
        return f"{self.value}/{self.znak}"
class Deck:
    def __init__(self):
        self.cards = []
        liczby = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
        for i in liczby:
            for j in ["Serce", "Pik", "Diament", "Kluby"]:
                self.cards.append(Card(i, j))
        self.tasowanie()
    def __str__(self):
        temp=""
        for i in self.cards:
            temp+=f"{i.value}/{i.znak} "
        return f"{temp}"
    def tasowanie(self):
        random.shuffle(self.cards)
    def dobieranie(self):
        return self.cards.pop()

Deck1 = Deck()
print(Deck1.tasowanie())
print(Deck1)
print(Deck1.dobieranie())
print(Deck1.dobieranie())
print(Deck1.dobieranie())
print(Deck1)
