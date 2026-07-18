# Write a Python program that uses a for loop to iterate over a list of numbers and calculate the sum of the squares of each number.
list_num=int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(list_num):
    number = int(input("Enter a number: "))
    numbers.append(number)
sum_of_squares = 0
for n in numbers:
    sum_of_squares += n ** 2
print("Sum of squares:", sum_of_squares)



def print_characters(input_string):
    for char in input_string:
        print(char)



numbers = [10, 20, 5, 30, 15]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum number:", maximum)



fib_sequence = [0, 1]
for i in range(2, 10):
    next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
    fib_sequence.append(next_fib)
print("Fibonacci sequence:", fib_sequence)



dictionary = {'a': 1, 'b': 2, 'c': 3}
for key, value in dictionary.items():
    print(f"Key: {key}, Value: {value}")