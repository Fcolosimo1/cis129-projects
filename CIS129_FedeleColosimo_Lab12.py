#Author Fedele Colosimo
#Module 12 lab

class Pet:
    # Constructor
    def __init__(self, n, t, a):
        self.name = n
        self.type = t
        self.age = a

    # Mutators
    def set_name(self, n):
        self.name = n

    def set_type(self, t):
        self.type = t

    def set_age(self, a):
        self.age = a

    # Accessors
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age


# main module
def main():
    # Declare input variables
    input_name = input("Enter a pet name: ")
    input_type = input("Enter a pet type: ")
    input_age = int(input("Enter a pet age: "))

    # create a Pet object
    animal = Pet(input_name, input_type, input_age)

    # Show values for this pet
    print("The pet name is", animal.get_name())
    print("The pet type is", animal.get_type())
    print("The pet age is", animal.get_age())


# Call the main function to run the program
if __name__ == "__main__":
    main()
