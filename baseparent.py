class animal:
 def __init__(self,name):
    self.name=name

class dog(animal):
 def display(self):
    print(self.name)

d= dog("little baby dog")
d.display()