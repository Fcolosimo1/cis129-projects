# Author: Fedele Colosimo
# Module 3 coffee shop program
#The program calculates the income from ticket sales in a theater with three sections (A, B, and C) charging $20, $15, and $10 per ticket, respectively. 
      #After validating the input for each section against its capacity, it displays the subtotal for each section and the total income generated.

# Constants
SECTION_NAMES = ["A", "B", "C"]
SEAT_PRICES = {"A": 20, "B": 15, "C": 10}
SEAT_CAPACITIES = {"A": 300, "B": 500, "C": 200}

# Function to display welcome message
def display_welcome():
    print("Welcome to the Theater Ticket Sales Program!")
    print("Section Names:", SECTION_NAMES)
    print("Seat Prices:", SEAT_PRICES)
    print("Seat Capacities:", SEAT_CAPACITIES)
    print()

# Function to get number of tickets sold for a section
def get_tickets_sold(section):
    while True:
        try:
            tickets_sold = int(input(f"Enter the number of tickets sold for section {section}: "))
            if tickets_sold < 0:
                raise ValueError("Number of tickets sold cannot be negative.")
            if tickets_sold > SEAT_CAPACITIES[section]:
                raise ValueError(f"Number of tickets sold exceeds section {section} capacity.")
            return tickets_sold
        except ValueError as e:
            print("Error:", e)

# Function to calculate subtotal for a section
def calculate_subtotal(section, tickets_sold):
    return tickets_sold * SEAT_PRICES[section]

# Main function
def main():
    display_welcome()
    
    total_income = 0
    section_totals = {}

    # Get ticket sales for each section
    for section in SECTION_NAMES:
        tickets_sold = get_tickets_sold(section)
        subtotal = calculate_subtotal(section, tickets_sold)
        total_income += subtotal
        section_totals[section] = subtotal

        print(f"Subtotal for section {section}: ${subtotal}")
        print(f"Overall total so far: ${total_income}\n")

    # Display overall total and section totals
    print("Overall Total Income:", total_income)
    print("Section Totals:")
    for section, subtotal in section_totals.items():
        print(f"Section {section}: ${subtotal}")

# Call the main function
main()
