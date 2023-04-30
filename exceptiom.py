import math
num=int(input('please enter the factorial of :'))
try:
    result=math.factorial(num)
    print(result)
except:
    print("can't compute the factorial of negative numbers cause of some reason")
