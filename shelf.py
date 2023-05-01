#this is shelf one in python, there is one way to which you can ignore this shelf
#from writing in the programming
class person:
    def display(shelf): #we use shelf as a parameter here to pass the arguments.
                        #if you don't write anything on that shelf then it shows typeerror on the code
                        #in output. this is because there is nothing to pass in the parameter.
                        #you can anything instead of shelf as well like name or anything u want.
        print("hello")

p=person()
p.display()
#instead of shelf there is next option to use if you don't wanna write shelf
class lotus:
    @staticmethod
    def display():
        print("what's up guys")
l=lotus()
l.display()