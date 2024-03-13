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
