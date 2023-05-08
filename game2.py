import random
x=random.randrange(1,10)
guess=int(input("Enter any numbers from 1 to 8: "))
while guess!=x:
    print("sorry!!you guessed the wrong number. Try again please")
    guess=int(input("Enter any numbers from 1 to 8: "))
print("Congratulations!!you have guessed the number correctly.")