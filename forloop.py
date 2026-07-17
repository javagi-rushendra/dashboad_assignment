n=[1,2,3,4,5,6,7,8,9,10]
for i in n:
    print(f"Number: {i}, Square: {i**2}")


def print_characters_with_index(input_string):
    for index, character in enumerate(input_string):
        print(f"Index: {index}, Character: {character}")







n=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even = 0
for num in n:
    if num % 2 == 0:
        sum_even += num
print(f"Sum of even numbers: {sum_even}")





dict={"a": 1, "b": 2, "c": 3}
for key, value in dict.items():
    print(f"Key: {key}, Value: {value}")







for i in range(1, 101):
    for j in range(1, 101):
        if j % 3 == 0 or j % 5 == 0:
            print(j)

