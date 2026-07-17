# 01.Implement a Python function print_numbers(n) that uses a while loop to print numbers from 1 to n (inclusive), where n is a positive integer provided as input to the function.
from random import random


n=1
while n<=10:
    print(n)
    n=n+1
# Write a Python program that simulates a simple bank account system. The system should use a while loop to continuously prompt the user for actions (deposit, withdraw, check balance) until the user decides to exit. The initial balance should be $1000.
amount = 1000
while amount>=0:
    action=input("enter (deposit, withdraw, check balance, exit): ").lower()
    if action=="deposit":
        deposit_amount=float(input("Enter deposit amount: "))
        amount=amount+deposit_amount
        print(f' deposited amount: {deposit_amount}, new balance: {amount}')
    elif action=="withdraw":
        withdraw_amount=float(input("enter withdraw amount: "))
        amount=amount-withdraw_amount
        print(f'withdraw amount: {withdraw_amount}, new balance: {amount}')
    elif action=="checkbalance":
        print(f'balance: {amount}')
    elif action=="exit":
        print("exiting the bank account system: ")
        break
    else:
        print("invalid action, please try again.")
# Create a function find_factorial(n) that calculates the factorial of a given number n using a while loop. The function should handle cases where n is less than 0 by raising a ValueError.
n=int(input("Enter a number to find its factorial: "))
while n<0: 
    raise ValueError("Factorial is not defined for negative numbers.")
factorial=1
while n>0:
    factorial=factorial*n
    n=n-1
print(f'The factorial of the given number is: {factorial}')

# Develop a simple number guessing game where the computer thinks of a number between 1 and 100, and the user has to guess it. After each guess, the computer should give a hint (higher or lower) using a while loop to repeatedly ask for guesses until the correct number is guessed.


number_to_guess = random.randint(1, 100)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print("Higher!")
    elif guess > number_to_guess:
        print("Lower!")
    else:
        print("Congratulations! You guessed the number.")