#Author: Fedele Colosimo
#Module 5 Lab:  Repetition Structures

keepGoing = "y"

# Declare local variables
monthlySales = 0
storeAmount = 0
empAmount = 0
salesIncrease = 0

# Function calls
while keepGoing() == "y":
# Include code to get the monthly Sales
# Include code to get the Increase in Sales
# Include code to Calculate the Store Bonus
# Include code to Calculate the Employee Bonus
# Include code to print out all the results
    
print("Do you want to run the program again? (Enter y for yes).")
keepGoing = input()

keepGoing = "y"

# Declare local variables
monthlySales = 0.0
storeAmount = 0.0
empAmount = 0.0
salesIncrease = 0.0

# Do-While Loop
while True:
# include code to get the monthly Sales
# include code to get the Increase in Sales
# include code to Calculate the Store Bonus
# include code to Calculate the Employee Bonus
# include code to print out all the results
    
    print("Do you want to run the program again? (Enter y for yes).")
    keepGoing = input()
    if keepGoing.lower() != "y":
        break


#Module 5 Lab Part 2 –Repetition Structures Pseudocode: Count Controlled Loops
 // Step 1: Declare variables below 
   totalBottles = 0
   counter = 1
   todayBottles = 0
   totalPayout = 0
   keepGoing = "y"
	
   // Step 3: Loop to run program again
   While keepGoing.lower() == "y"
      // Step 2: Code to set value of variables
      # code to set value of variable totalBottles 
      # code to set value of variable totalPayout
      # code to print the number of total bottles and total payout
		
      Display "Do you want to enter another week’s worth of data?"
      Display "(Enter y or n)"
      Input keepGoing
   End While	

// getBottles code
    NBR_OF_DAYS = 7
    // Declare and initialize totalBottles, todayBottles, counter to 0
totalBottles = 0
todayBottles = 0
counter = 1

    While counter <= NBR_OF_DAYS
             Display "Enter number of bottles returned for day #", counter, ":"
             Input todayBottles
             totalBottles = totalBottles + todayBottles
             counter = counter + 1
	End While
	

// calcPayout code
     PAYOUT_PER_BOTTLE = .10
     totalPayout = totalBottles * PAYOUT_PER_BOTTLE

// printInfo code
a.  Display "Total number of bottles collected for the week:", totalBottles
b.  Display "Total payout for the week:", totalPayout

# Lab 5 The Bottle Return Program

# Step 1: Declare variables below 
totalBottles = 0
todayBottles = 0
counter = 1
totalPayout = 0
keepGoing = "y"

# Step 2: Loop to run program again
while keepGoing.lower() == "y":
    # Step 3: Code to set value of variables
    totalBottles = 0  # reset totalBottles for each week
    for counter in range(1, 8):
        print("Enter number of bottles for day #" + str(counter) + ":")
        todayBottles = float(input())
        totalBottles += todayBottles
    
    # Step 4: Calculate totalPayout
    PAYOUT_PER_BOTTLE = 0.10
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE
    
    # Step 5: Print the number of total bottles and total payout
    print("The total number of bottles collected is", totalBottles)
    print("The total paid out is $", totalPayout)
    
    # Step 6: Ask if the user wants to enter another week’s worth of data
    print("Do you want to enter another week’s worth of data? (Enter y or n):")
    keepGoing = input()
