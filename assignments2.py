# #Create a Python script that generates a tuple containing the names of 5 different cities.
# Write a function that takes a tuple as an argument and returns the first and last elements of the tuple.
# Create a tuple of tuples, where each inner tuple contains a student's name and their corresponding grade (e.g., ( ("John", 85), ("Alice", 92) )).
# Implement a function that takes the tuple of tuples from the previous task and returns a new tuple with the students' names sorted in alphabetical order.
# Practice tuple unpacking by writing a function that takes a tuple of 3 elements and assigns each element to a separate variable, then prints out the values of these variables.





# Step 1: Generate a tuple containing the names of 5 different cities
cities = ("annathapur", "mudigubba", "satyasai", "dharmavaram", "hindupur")
def get_first_and_last_elements(city_tuple):
    # Step 2: Function to return the first and last elements of the tuple
    return city_tuple[0], city_tuple[-1] 
#step 3: Create a tuple of tuples with students' names and their corresponding grades 
tuple_of_tuples = (("John", 85), ("Alice", 92), ("Bob", 78), ("Eve", 88), ("Charlie", 95))
#Implement a function that takes the tuple of tuples from the previous task and returns a new tuple with the students' names sorted in alphabetical order.
# def sort_student_names(student_tuple):
#     # Step 4: Function to return a new tuple with students' names sorted in alphabetical order
#     sorted_names = tuple(sorted(student[0] for student in student_tuple))
#     return sorted_names

def sort_student_names(student_tuple):
    # Step 4: Function to return a new tuple with students' names sorted in alphabetical order
    sorted_names = tuple(sorted(student[0] for student in student_tuple))
    return sorted_names

# Step 5: Function to demonstrate tuple unpacking
def demonstrate_tuple_unpacking(my_tuple):
    a, b, c = my_tuple
    print(f"Variable a: {a}")
    print(f"Variable b: {b}")
    print(f"Variable c: {c}")
