# Ask the user for a password
#Declare password
correct = "cheese"
#Declare number of attempts
tries = 0

keepGoing = True
while(keepGoing):
    #While loop to record the number of password attempts
    tries = tries + 1 
    print("try # ", tries) #Prints the amount of times a user has tried
    
    guess = input("What is the password? ") #Creates the variable to store a user guess
    if guess == correct: ## If statement to test if users guess was the correct password
        print("That's correct! Here's the treasure!")
        keepGoing = False
        
    elif tries >= 3:
        print("Too many wrong tries. Launching the missles")
        keepGoing = False