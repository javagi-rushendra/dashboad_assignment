# Create a Python program that asks the user for their age and then uses conditional statements to determine and print whether the user is eligible to vote (assuming the voting age is 18 years old).
# Write a Python function that takes a grade (as a percentage) as input and uses conditional statements to return the corresponding letter grade (A for 90-100%, B for 80-89%, C for 70-79%, D for 60-69%, and F for below 60%).
# Develop a simple calculator program in Python that uses conditional statements to perform different mathematical operations (addition, subtraction, multiplication, division) based on the user's choice.
# Implement a Python program that generates a random number between 1 and 100 and uses conditional statements to guess whether the number is odd or even, providing feedback to the user
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")



def letter_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'
    

num = float(input("Enter your grade percentage: "))
grade = letter_grade(num)
print("Your letter grade is:", grade)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Choose operation: 1. Addition 2. Subtraction 3. Multiplication 4. Division")
choice = int(input("Enter your choice (1-4): "))
if choice == 1:
    result = n1 + n2
    print("Result:", result)
elif choice == 2:
    result = n1 - n2
    print("Result:", result)
elif choice == 3:
    result = n1 * n2
    print("Result:", result)
elif choice == 4:
    if n2 != 0:
        result = n1 / n2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")


import random
random_number = random.randint(1, 100)
if random_number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")