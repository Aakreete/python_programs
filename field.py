#fields are the data which belongs to the class.
#there are 2types of fields in class of python.
#1. instance variable and class variable.
#the variable belongs to the object or instance is called a instance variable.
#the variable which belongs to the class is called class variable.
#that means a single variable belongs to all the object in the class.
class student:
    college='cityofwolverhampton'#class variable cause the all students belongs to this collgege

    def __init__(self, rollno, name):
        self.rollno=rollno
        self.name=name

    def display(self):
        print("student name:", self.name)
        print("student roll no.", self.rollno)
        print("college:", student.college)
student1=student('02', 'aakriti')
student1.display()
student2=student('03', 'arya')
student2.display()