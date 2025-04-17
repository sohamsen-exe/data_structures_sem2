class Employee:
    def EmpData(self, n, a, id):
        self.name = n
        self.age = a
        self.id = id
    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("EmpID :", self.id)

e1 = Employee()
e1.EmpData("Soham", 10, 69420)
e1.display()