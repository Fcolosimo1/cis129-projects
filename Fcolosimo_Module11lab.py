#Author Fedele Colosimo
#Module 11: Lab 
#Part 9.1
# Open the file in write mode ('w')
with open('grades.txt', 'w') as file:
    # Initialize an empty list to store grades
    grades = []
    
    # Prompt the user to enter grades
    print("Enter grades (enter 'q' to quit):")
    
    # Continue prompting until the user enters 'q'
    while True:
        grade = input("Enter grade: ")
        
        # If the user enters 'q', break out of the loop
        if grade.lower() == 'q':
            break
        
        # Otherwise, add the grade to the list
        grades.append(grade)
    
    # Write the grades to the file, one grade per line
    for grade in grades:
        file.write(grade + '\n')

print("Grades have been written to grades.txt")

#Part 9.2
# Open the file in read mode ('r')
with open('grades.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
    
    # Strip newline characters and convert grades to integers
    grades = [int(line.strip()) for line in lines]
    
    # Display individual grades
    print("Individual Grades:")
    for grade in grades:
        print(grade)
    
    # Calculate total, count, and average
    total = sum(grades)
    count = len(grades)
    average = total / count
    
    # Display total, count, and average
    print("\nTotal:", total)
    print("Count:", count)
    print("Average:", average)

#Part 9.3
import csv

# Open the file in write mode ('w') with newline='' to avoid extra newline characters
with open('grades.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'])
    
    # Prompt the user to enter student records
    print("Enter student records (firstname, lastname, exam1grade, exam2grade, exam3grade):")
    
    # Continue prompting until the user enters 'q'
    while True:
        # Get input from the user
        record = input("Enter record (or 'q' to quit): ")
        
        # If the user enters 'q', break out of the loop
        if record.lower() == 'q':
            break
        
        # Split the input into parts (firstname, lastname, exam1grade, exam2grade, exam3grade)
        parts = record.split(',')
        
        # Write the record to the CSV file
        writer.writerow(parts)

print("Student records have been written to grades.csv")
