# this is a else if statement after nested if.
# simple concept of ELIF statement: if cond:
# statemtn: else: if ,cond, stat, else, if,
x = 10
y = 25
z = 43
a = 56
b = 96
if x > y and x > z:
    print("x is greater among them")
else:
    if y > z and y > a:
        print("y is greater among them")
    else:
        if z > a and z > b:
            print("z is greater among them")
        elif a>b and a>x:
                print("a is greater among them")
        else:
                print("b is greater among them")
