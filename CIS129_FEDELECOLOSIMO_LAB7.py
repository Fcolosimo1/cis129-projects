# Author: Fedele Colosimo
# Module 7 Dice Game Lab

# Lab 7.1 - Functions and Pseudocode
#Step 1
def addTen(number):
    print("Enter a number:")
    number = int(input())
    number += 10
    return number
#Step 2
number = addTen()

#Writing Your Own Function that Returns a Boolean Value
#Step 1
def gender():
    answer = False
    type = input("Enter your gender (male or female): ")
    if type == "male":
        answer = False
    else:
        answer = True
    return answer
#Step 2
answer = gender()

#Using Mathematical Library Function: sqrt
#Step 1
# Declare a variable named myNumber
myNumber = 0

# Declare a variable named squareRoot of the data type Real
squareRoot = 0.0

# Ask the user to enter a number and store it in myNumber
myNumber = float(input("Enter a number: "))

# Call the sqrt function to determine the square root of myNumber
squareRoot = math.sqrt(myNumber)

# Display the square root to the screen
print("The square root is", squareRoot)

#Using formatting Functions
#Step 1
Declare Real subtotal
Declare Constant Real tax = 0.06
Declare Real total

Display "Enter the subtotal:"
Input subtotal

Set total = subtotal + subtotal * tax

Display "The total is $", currencyFormat(total)

#Lab 7.2 – Python Code and Random
import random  

# the main function
def main():
    print()

    # initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'
    winnersName = 'NO NAME'
    p1number = 0
    p2number = 0

    # call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # while loop to run program again
    while endProgram == 'no':

        # call to rollDice
        winnersName = rollDice(p1number, p2number, playerOne, playerTwo, winnersName)

        # call to displayInfo
        displayInfo(winnersName)

        endProgram = input('Do you want to end program? (yes/no): ')

# this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input("Enter Player One's name: ")
    playerTwo = input("Enter Player Two's name: ")
    return playerOne, playerTwo

# this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnersName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    if p1number > p2number:
        winnersName = playerOne
    elif p2number > p1number:
        winnersName = playerTwo
    else:
        winnersName = "TIE"
    return winnersName

# this function displays the winner
def displayInfo(winnerName):
    print("The winner is:", winnerName)

# calls main
main()

