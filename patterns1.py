# Write a Python program to print the following patterns using nested loops:
# A square pattern of a specified size filled with asterisks (*)
# A right-angled triangle pattern of a specified height filled with numbers starting from 1
# A pyramid pattern of a specified height filled with asterisks (*)
# Ensure your program is well-documented with comments explaining the purpose of each section of code
# Test your program with different input sizes to verify its correctness and robustness

for i in range(5):  # Loop for rows
    for j in range(5):  # Loop for columns
        print("*", end=" ")  # Print asterisk without newline
    print()  # Move to the next line after each row



for i in range(1, 6):  # Loop for rows (height of triangle)
    for j in range(1, i + 1):  # Loop for columns (numbers in each row)
        print(j, end=" ")  # Print number without newline
    print()  # Move to the next line after each row


for i in range(1, 6):  # Loop for rows (height of pyramid)
    for j in range(5 - i):  # Loop for spaces before the asterisks
        print(" ", end="")  # Print space without newline
    for k in range(2 * i - 1):  # Loop for asterisks in each row
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next line after each row

#test cases
# Test case 1: Square pattern of size 5
# Test case 2: Right-angled triangle pattern of height 5
# Test case 3: Pyramid pattern of height 5




