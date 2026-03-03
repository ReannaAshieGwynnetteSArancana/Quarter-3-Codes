# Create an empty dictionary
student = {}

# Collect information from the user
name = input("Enter your name: ")
age = input("Enter your age: ")
subject = input("Enter your favorite subject: ")

# Store the information in the dictionary
student["name"] = name
student["age"] = age
student["subject"] = subject

# Display the student record
print("\nStudent Record:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Favorite Subject:", student["subject"])
