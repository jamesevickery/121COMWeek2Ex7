def game(): # This is the main method for the game
    print("----------121COM Week 2 Lab Exercise 7----------")
    print("----------------<InsertTitleHere>---------------")
    print("---------------<InsertAuthorsHere>--------------")
    print("\n")
    
    print("You awake in a dark room.  Do you:")
    print("a) Scream for help.")
    print("b) Press the light switch")
    x = input("Enter a or b: ")
    if x == "a":
        print("Someone hears your screams...")
        # Contine adventure Here
    elif x == "b":
        print("The light comes on.")
        print("You do not recognise the room but you have a really bad feeling...")
        # Contine adventure Here
    else:
        raise ValueError("That was not an option. Game Over.")


try:
    game()
except ValueError as e:
    print("\nThat was not an option.\nYou fool.\nYou were given simple instructions but you're never happy, are you.\nWell, I hope you're proud of yourself.")

print("\nEnd of game.")