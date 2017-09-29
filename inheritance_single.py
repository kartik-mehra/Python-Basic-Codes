#class subclass(parent_class1,parent_class2,......,parent_classn)
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
class subclass(employee):
    a=0;
sub1=subclass("python",5200);#objext creation
sub1.display()
sub1.displaye()
sub1.age=10;#declaring variable outside class
print(sub1.age);
