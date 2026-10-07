# Ghost Game
from random import randint
print("Ghost Game")
feeling_brave = True # loop on/off switch
score = 0 # Initalizing a Variable 

while feeling_brave:
    ghost_door = randint(1, 3) # computer pick
    print("there are 3 doors to choose from")
    print("there is a ghost behind one of them ")
    print("which doors will you open?")
    door = input("1, 2, or 3? ") # data type inherited string 
    door_num = int(door) # change data type to int

    # write an if else statement of door selection

    if ghost_door == door_num: # two equal signs to compare variable
        print("Ghost is here!") # TRUE
        feeling_brave = False # Break the loop
    else:
        print("No Ghost here!")
        print("Try again")
        score = score + 1 # increment by 1 track tries 

# concatenate a winners statement telling the user how many tries it 
print("You Found the Ghost. It took", score, "tries.")
print("Gamee Over") 