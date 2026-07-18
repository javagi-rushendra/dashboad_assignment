# Create a Python program that uses a While loop to print numbers from 1 to 10.
n=1
while n <= 10:
    print(n)
    n=n+1
# Modify the program to ask the user for a positive integer input and print numbers from 1 up to the input number using a While loop.
A=int(input("Please enter a positive integer: "))
while A <= 0:
    print("Invalid input. Please enter a positive integer.")
    A=int(input("Please enter a positive integer: "))
# Ensure your program includes input validation to handle cases where the user enters a non-positive integer or a non-integer value.
# Submit your Python code as a .py file along with a brief explanation of how your program works.