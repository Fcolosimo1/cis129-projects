import math

# Function to get the total number of hot dogs needed
def get_total_hotdogs():
    # Get the number of people attending the cookout
    people = int(input("Enter the number of people attending the cookout: "))
    # Get the number of hot dogs for each person
    hotdogs_per_person = int(input("Enter the number of hot dogs for each person: "))
    # Calculate the total number of hot dogs needed
    total_hotdogs = people * hotdogs_per_person
    return total_hotdogs

# Function to display the results
def show_results(dogs_left, min_dogs, buns_left, min_buns):
    # Display the minimum packages of hot dogs needed
    print("Minimum packages of hot dogs needed:", min_dogs)
    # Display the minimum packages of buns needed
    print("Minimum packages of hot dog buns needed:", min_buns)
    # Display the number of hot dogs left over
    print("Hot dogs left over:", dogs_left)
    # Display the number of hot dog buns left over
    print("Hot dog buns left over:", buns_left)

# Main module
def main():
    # Get the total number of hot dogs needed
    total = get_total_hotdogs()
    
    # Named constants for the package sizes
    DOGS = 10   # Hot dogs in a package
    BUNS = 8    # Hot dog buns in a package

    # Calculate the number of left over hot dogs
    dogs_left = (DOGS - total % DOGS) % DOGS

    # Calculate the minimum number of packages of hot dogs
    min_dogs = math.ceil(total / DOGS)

    # Calculate the number of left over hot dog buns
    buns_left = (BUNS - total % BUNS) % BUNS

    # Calculate the minimum number of packages of hot dogs buns
    min_buns = math.ceil(total / BUNS)

    # Display the results
    show_results(dogs_left, min_dogs, buns_left, min_buns)

# Call the main function
main()
