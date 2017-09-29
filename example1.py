class employee:
    empcount=0;
    def __init__(self,name,salary):#constructor
        self.name=name;
        self.salary=salary;
        employee.empcount+=1;
    def display(self):
        print("Total = ",self.empcount)
    def displaye(self):
        print("name = ",self.name,"salary = ",self.salary);

emp1=employee("python",5200);#objext creation
emp1.display()
emp1.displaye()
emp1.age=10;#declaring variable outside class
print(emp1.age);
