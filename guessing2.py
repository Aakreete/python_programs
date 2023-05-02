#This is simple and a normal guessing game

print("Welcome to this amazing game guys")
b=input("Guess the number")
guess=int(b)
if guess==7:
    print("Absolutely correct!!")
else:
    if guess>7:
        print("This is too high")
    else:
        if guess<7:
            print("This is too low.")
print("Game Over")