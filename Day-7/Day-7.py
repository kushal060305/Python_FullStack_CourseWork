#Generate a code for all the dictionary with their openrations like add , delete, update and search# Create an empty dictionary
my_dict = {}

# Add an item to the dictionary
my_dict["key1"] = "value1"
my_dict["key2"] = "value2"

# Update an item in the dictionary
my_dict["key1"] = "new_value1"

# Delete an item from the dictionary
del my_dict["key2"]

# Search for an item in the dictionary
if "key1" in my_dict:
    print("Key found!")
    print(my_dict["key1"])