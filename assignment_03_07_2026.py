# Tasks / Requirements
# Create a Python script that uses a for loop to iterate over a list of numbers, printing each number and its square.
l = [1, 2, 3, 4, 5]
for n in l:
    print(f"{n}: {n**2}")
# Write a Python function that takes a string as input and uses a for loop to print each character in the string, along with its index.
st=input("Enter a string: ")
for index, char in enumerate(st):
    print(f"Index {index}: {char}")     
# Use a for loop to find and print the sum of all even numbers in a given list of integers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
for n in numbers:
    if n % 2 == 0:
        even_sum += n
print(f"Sum of even numbers: {even_sum}")
# Implement a Python program that utilizes a for loop to iterate over a dictionary, printing each key-value pair.
d = {"a": 1, "b": 2, "c": 3}
for key, value in d.items():
    print(f"{key}: {value}")
# Generate a list of numbers from 1 to 100 using a for loop, then use another loop to print the numbers that are divisible by 3 or 5.
numbers_1_to_100 = [n for n in range(1, 101)]
for n in numbers_1_to_100:
    if n % 3 == 0 or n % 5 == 0:
        print(n)
