'''
Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the + operator and f-strings for output.
'''
name=input("Enter your name")
age=input("Enter your age")
fullname = name+" "+age
print(f"Hello! {name}, your are {age} years old")
