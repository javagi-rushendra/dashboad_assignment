# Create a new list containing the names of 5 different cities
# Use indexing to access and print the name of the city at the middle index of the list
# Use slicing to extract a subset of cities from the list (e.g., the first 3 cities) and print the result
# Sort the list of cities in ascending order and print the result
# Append a new city to the end of the list and print the updated list
# Remove the first city from the list and print the updated list
# Write a function that takes a list of cities as input and returns the length of the list
# Test the function with the list of cities created in the first task and print the result

n= 5
cities =[]
for i in range(n):
    city=input("enter a city name: ")
    cities.append(city)

print("cities:",cities)


# access the city at the middle Index
middile_Index = len(city) // 2
print("city at middle index: ",cities[middile_Index])

# extract a the subset of cities using slicing
submit=cities[:3]
print("first 3 cities:", subset)

# sort  the list in ascending order
cities.sort()
print("sorted cities:",cities)

# Append a new city to the end of the list
new_city = input("enter a name to append:")
cities.append(new_city)
print("update list after appending:",cities)

# Remove the first city from list
cities.pop(0)
print("update list after removing first city:",cities)

# function to return the length of the list
def get_city_count(city_list):
    return len(city_list)

# test the function
count = get_city_count(cities)
print("number of cities in the list:",count)







