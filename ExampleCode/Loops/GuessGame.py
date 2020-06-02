"""
   Simple guess game select a random int between 1->9 and will ask you got
   guesses in an infinite loop until you get it right.
   
   Be very careful that you follow the indentation here, 
"""


import random         # Add the randon module

def main():
    
    #     Use randint to get number between 1 -> 9 (inclusive)
    correct = random.randint(1,9)       
    
    
    print("\nWlecome: Guess the number between 1 and 9\n")

    number_of_tries = 0

    while True:               # Start of infinite loop
        guess = int(input("Have a guess (give an int) : "))
        number_of_tries += 1

        if guess == correct:  # Test if the guess is correct
            print("You guessed right the correct value was : "+ str(correct))
            break             # If correct break the loop
        else:
            print("You guessed wrong.... have another go")
        # End of loop


    #    This is after loop.
    print("You took " + str(number_of_tries) + " attempt to guess right")


main()
