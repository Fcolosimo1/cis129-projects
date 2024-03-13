#Author: Fedele Colosimo
#Module 4 Lab:  Decisions and Boolean Logic

⦁	myAge = 32
⦁	yourAge = 18
⦁	myNumber = 81
⦁	yourNumber = 17
⦁	votingAge = 18

If myAge == 31 AND yourAge < myAge Then
   Display "My age is 31 and your age is less than that"
End If
If myAge <= 35 AND myAge >= 32 Then
   Display "My age is between 32 and 35"
End If
If yourAge == votingAge OR yourAge > votingAge Then
    Display "You can vote"
End If
If myNumber == 83 OR yourNumber == 83 Then
    Display "One of our numbers is 83"
End If
If myAge == 31 AND yourAge < myAge Then
    Display "My age is 31 and your age is less than that"
Else
    Display "Our ages do not qualify"
End If
If myAge <= 35 AND myAge >= 32 Then
    Display "My age is between 32 and 35"
Else
    Display "My age is not within that range"
End If
If yourAge == votingAge OR yourAge > votingAge Then
    Display "You can vote"
Else 
    Display "You cannot vote"
End If
If myNumber == 83 OR yourNumber == 83 Then
    Display "One of our numbers is 83"
Else
    Display "83 is not our numbers"
End If

#Module 4 Lab Part 2 – Pseudocode:  Dual Alternative Decisions

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = "Enter the monthly sales amount: "  # prompt will be a string literal

# include code to get the monthly Sales
# include code to get the Increase in Sales
# include code to Calculate the Store Bonus
# include code to Calculate the Employee Bonus
# include code to print out all the results

# This code determines the storeAmount bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# This code gets the percent of increase in sales
salesIncrease = float(input("Enter the percent increase in sales (in decimal format): "))
salesIncrease = salesIncrease * 100  # Convert from decimal to percentage

# This code determines the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= 4:
    empAmount = 50
elif salesIncrease >= 3:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if storeAmount == 6000 or empAmount == 75:
    print('Congrats! You have reached the highest bonus amounts possible!')
