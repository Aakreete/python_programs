#Ghost Game
from random import randint;
import time;

feeling_brave = True
score = 0

print('Ghost Game')

while feeling_brave:
  ghost_door = randint(1,3)
  
  print ('Three doors ahead ...')
  print('A ghost behind one.')
  print('which door do you open?')
  
  selection = False
  while selection == False:
    door = input('1,2, or 3?')
    
    try:
      
      if int(door)<= 3 and int(door)>= 1:
        door_num = int(door)
        selection = True
      else:
        print("That's not a valid door number!")
    except ValueError:
      
      print("That's not even valid input!")  
  
  time.sleep(1)
  if door_num == ghost_door:
    print("GHOST")
    feeling_brave = False
  else:
    print('No Ghost!')
    print('You enter the next room.')
    score = score + 1

print('run away!')
print('Game over! you scored ', score)