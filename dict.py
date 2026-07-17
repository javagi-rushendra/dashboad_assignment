# Create a Python program that initializes an empty dictionary to store user profiles, with keys representing user IDs and values representing user names.
# Implement a function to add a new user profile to the dictionary, taking user ID and name as input parameters.
# Implement a function to retrieve a user's name by their ID, handling cases where the ID is not found in the dictionary.
# Implement a function to update an existing user's name, given their ID and new name.
# Implement a function to remove a user profile by their ID, handling cases where the ID is not found in the dictionary.
# Test each function with sample data to demonstrate their correctness, printing the resulting dictionary after each operation.
dictionary = {}
def add_user(user_id, name):
    dictionary[user_id] = name
    print(f"User {name} added with ID {user_id}.")
    print("Current dictionary:", dictionary)
def get_user(user_id):
    if user_id in dictionary:
        print(f"User ID {user_id} corresponds to name: {dictionary[user_id]}")
    else:
        print(f"User ID {user_id} not found.")

def update_user(user_id, new_name):
    if user_id in dictionary:
        dictionary[user_id] = new_name
        print(f"User ID {user_id} updated to name: {new_name}")
    else:
        print(f"User ID {user_id} not found.")
    print("Current dictionary:", dictionary)

def remove_user(user_id):
    if user_id in dictionary:
        del dictionary[user_id]
        print(f"User ID {user_id} removed.")
    else:
        print(f"User ID {user_id} not found.")
    print("Current dictionary:", dictionary)

# Test the functions
add_user(1, "Alice")
add_user(2, "Bob")
get_user(1)
get_user(3)
update_user(1, "Charlie")
remove_user(2)
remove_user(3)