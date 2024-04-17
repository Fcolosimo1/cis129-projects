#Auther Fedele Coloismo
#Module 8 lab

def is_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()
    
    # Remove spaces and punctuation
    s = ''.join(char for char in s if char.isalnum())
    
    # Initialize a stack to store characters
    stack = []
    
    # Push each character of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack and compare them with characters from the string
    while len(stack) > 1:
        # Pop the first character from the stack
        first_char = stack.pop(0)
        
        # Pop the last character from the stack
        last_char = stack.pop()
        
        # If the characters don't match, return False (not a palindrome)
        if first_char != last_char:
            return False
    
    # If all characters match, return True (palindrome)
    return True

# Test the function
print(is_palindrome("radar"))  # True
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("hello"))  # False
