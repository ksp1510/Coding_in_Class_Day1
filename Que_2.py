"""
Author: Kishankumar Sanjaybhai Patel
Course: Emerging Technologies
Student Id: C0805822
Coding in class
Question 2
"""

# Write a Python program which accepts the user's first and last name and print them in reverse order with a space
# between them.
print("Welcome to the program that takes first and last name from user and print it in reverse order\n")

fname = input("Enter your first name: ").capitalize()
lname = input("Enter your last name: ").capitalize()
name = fname+" "+lname
print(f"\nUser name is '{name}'")

print(f"\nReverse of user's name using reverse indexing:")
print(f"'{name[::-1].lower()}'")

print(f"\nReverse of user's name using for loop:")
name1 = ""
for x in name:
    name1 = x+name1
print(f"'{name1.lower()}'")

print("\nThank you for using the program")