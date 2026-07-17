# Create a new list containing the names of 5 different cities
# Use indexing to access and print the name of the city at the middle index of the list
# Use slicing to extract a subset of cities from the list (e.g., the first 3 cities) and print the result
# Sort the list of cities in ascending order and print the result
# Append a new city to the end of the list and print the updated list
# Remove the first city from the list and print the updated list
# Write a function that takes a list of cities as input and returns the length of the list
# Test the function with the list of cities created in the first task and print the result
n= 5
cities = []
for i in range(n):
    city = input("Enter a city name: ")
    cities.append(city)
    
print("Cities:", cities)

# Access the city at the middle index
middle_index = len(cities) // 2
print("City at middle index:", cities[middle_index])

# Extract a subset of cities using slicing
subset = cities[:3]
print("First 3 cities:", subset)

# Sort the list in ascending order
cities.sort()
print("Sorted cities:", cities)

# Append a new city to the end of the list
new_city = input("Enter a new city name to append: ")
cities.append(new_city)
print("Updated list after appending:", cities)

# Remove the first city from the list
cities.pop(0)
print("Updated list after removing first city:", cities)

# Function to return the length of the list
def get_city_count(city_list):
    return len(city_list)

# Test the function
count = get_city_count(cities)
print("Number of cities in the list:", count)