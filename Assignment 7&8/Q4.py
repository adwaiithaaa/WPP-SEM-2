class Employee:
    def __init__(self, name, sal):
        self.name = name 
        self.sal = sal  

    def __add__(self, other):
        return self.sal + other.sal 

    def __sub__(self, other):
        return self.sal - other.sal 

    def __lt__(self, other):
        return self.sal < other.sal  

    def __gt__(self, other):
        return self.sal > other.sal  

    def __eq__(self, other):
        return self.sal == other.sal  

e1 = Employee("Tina", 12000)
e2 = Employee("Sruthi", 10000)
print("Total Sal:", e1 + e2)
print("Sal Diff:", e1 - e2)
print("Tina < Sruthi:", e1 < e2)
print("Tina > Sruthi:", e1 > e2)
print("Tina == Sruthi:", e1 == e2)
