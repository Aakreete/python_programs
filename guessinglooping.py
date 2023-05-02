# this is a guessing game using a loop function
#run this program
 
print("Welcome to this programming section")
answer = "yes"
while answer == "yes":
    g = input("Guess the number: ")
    guess = int(g)
    if guess == 5:
        print("correct")
    else:
        if guess > 5:
            print("This number is very high")
        else:
            print("This is very low!!")
    answer = input("wanna play game again?yes/no")    
print("finish looping")
print("game over guys !!")
