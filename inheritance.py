#this is a multilevel inheritance 
#multilevel inheritance has base class(feature1), 
#derivedclass1(featureofbaseclass+feature2) and
#derivedclass2 has (featured of base class+deriveclass1+feature3)
#example to make you understand easilty grandfather, father and a child

#baseclass
class person:
    def display(self):
        print("heello, this is a base class")

#derivedclass1
class employee(person):
    def printing(self):
        print("helloo, This is a derived class 1.")

#derivedclass2
class officer(employee):
    def show(self):
        print("Helloo, this is a derived class2.")
        print("thank you, byee")

p=officer()
p.display()
p.printing()
p.show()
