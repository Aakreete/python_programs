#This is a object oriented programming language.
#there are 3types of different types of object oriented language
#1. Inheritance 2. Encapsulation 3. Polymorphism
#1. Inheritance: to inherits the property from the other class.
#The newely created class is called derived class or child and it has 3featured
#and already existed class is called Base class or parent class but it has 2features
#2features from parent class and one new feature in child class
class animal:
    def eating(self):
        print("eating")
class dog:
    def eating(self):
        print("he is a good boy")
    def bark(self):
            print("she is a good girl")
e=dog()
e.eating()
e.bark()