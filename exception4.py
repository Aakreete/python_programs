import math
num=int(input("enter a number please"))
try:
    result=math.factorial(num)
    print(result)
finally:
    print("goodnightt")

#what I understood from exception handling is on the function of factorial only
#the postive value gives the result and if it is negative number then it
#doesn't display the result. there is try, excpet and finally handling in excpetion
#which works like if else statement. #and exception works in order to handle the errors
#like valueerrors or nameerrors.