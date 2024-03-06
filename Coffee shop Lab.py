# Author: Fedele Colosimo
# Module 3 coffee shop program
# Write a short program in Python that asks the user for the number of coffee and muffins they are purchasing.

def main():
num_coffee = int(input("Number of coffees: "))
Num_muffins = int(input("Number of muffins: "))

subtotal = num_coffee * 5 + num_muffins * 4
tax = subtotal * 0.06
total = subtotal + tax 

Print(f"Subtotal: ${subtotal:.2f}")
Print(f"Tax (6%): ${tax:.2f}")
Print(f"Total: ${total:.2f}")

if__name__ == "__main__"
main()
